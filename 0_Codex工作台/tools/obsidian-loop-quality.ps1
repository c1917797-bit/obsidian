param(
  [Parameter(Position=0, Mandatory=$true)]
  [ValidateSet('status','quality','report')]
  [string]$Command,
  [ValidateSet('all','workbench')]
  [string]$Scope='workbench',
  [ValidateRange(1,200)]
  [int]$Limit=50
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$vaultRoot = (Resolve-Path (Join-Path $scriptDir '..\..')).Path
$workbenchRoot = (Resolve-Path (Join-Path $scriptDir '..')).Path
$workbenchName = Split-Path $workbenchRoot -Leaf
$guardRoot = Join-Path $workbenchRoot 'quality-guardian'
$statePath = Join-Path $guardRoot 'quality-gate-state.json'

function Get-Notes {
  param([string]$RootPath)
  if(-not (Test-Path -LiteralPath $RootPath)){ return @() }
  Get-ChildItem -LiteralPath $RootPath -Recurse -File -Filter '*.md' |
    Where-Object {
      $_.FullName -notmatch '[\\/]\.obsidian[\\/]' -and
      $_.FullName -notmatch '[\\/]\.trash[\\/]' -and
      $_.FullName -notmatch '[\\/]quality-guardian[\\/]' -and
      $_.FullName -notmatch '[\\/]Skills[\\/]'
    }
}

function Parse-Frontmatter {
  param([string]$Content)
  if(-not $Content.StartsWith('---')){ return $null }
  $end = $Content.IndexOf("`n---", 3)
  if($end -lt 0){ return $null }
  return $Content.Substring(3, $end - 3)
}

function Has-Section {
  param([string]$Content, [string]$Header)
  return $Content -match ('(?m)^' + [regex]::Escape($Header) + '\s*$')
}

function Score-Issue {
  param([string]$FilePath, [string]$Content)

  $problems = @()
  $fm = Parse-Frontmatter $Content

  if([string]::IsNullOrWhiteSpace($fm)){
    $problems += [pscustomobject]@{ code='P1'; text='Missing YAML frontmatter' }
  }

  if($Content -notmatch '(?m)^#\s+'){
    $problems += [pscustomobject]@{ code='P1'; text='Missing title heading (# ...)' }
  }

  $relativePath = $FilePath.Substring($vaultRoot.Length + 1)
  if($relativePath -like "$workbenchName\Inbox\*"){
    $requiredSections = @('## Source Facts', '## Codex Analysis', '## Linked Notes', '## Open Questions')
    foreach($s in $requiredSections){
      if(-not (Has-Section $Content $s)){
        $problems += [pscustomobject]@{ code='P2'; text="Missing section: $s" }
      }
    }
  }

  $suspiciousPatterns = @(
    'gh[pousr]_[A-Za-z0-9_]{20,}',
    'AKIA[0-9A-Z]{16}',
    '-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----',
    '(?i)(password|passwd|token|api[_-]?key)\s*[:=]\s*[^\s<]{8,}'
  )

  foreach($pattern in $suspiciousPatterns){
    if($Content -match $pattern){
      $problems += [pscustomobject]@{ code='P0'; text='Possible secret/credential pattern detected' }
      break
    }
  }

  return $problems
}

function Make-ReportPath {
  if(-not (Test-Path -LiteralPath $guardRoot)){
    New-Item -ItemType Directory -Force -Path $guardRoot | Out-Null
  }
  return Join-Path $guardRoot ("quality-audit-" + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.md')
}

$notes = if($Scope -eq 'workbench'){ Get-Notes $workbenchRoot } else { Get-Notes $vaultRoot }
$notes = @($notes)

$allIssues = foreach($note in $notes){
  $content = Get-Content -Raw -LiteralPath $note.FullName -Encoding UTF8
  $issues = @(Score-Issue $note.FullName $content)
  if($issues.Count -eq 0){ continue }

  [pscustomobject]@{
    path = $note.FullName.Substring($vaultRoot.Length + 1)
    severity = ($issues | ForEach-Object { $_.code } | Sort-Object | Select-Object -First 1)
    count = $issues.Count
    issues = ($issues | ForEach-Object { $_.text })
  }
}

$titleMap = @{}
foreach($note in $notes){
  if($note.FullName -match '[\\/]Templates[\\/]'){ continue }
  $content = Get-Content -Raw -LiteralPath $note.FullName -Encoding UTF8
  $titleMatch = [regex]::Match($content, '(?m)^#\s*(.+)$')
  if(-not $titleMatch.Success){ continue }
  $title = $titleMatch.Groups[1].Value.Trim()
  if([string]::IsNullOrWhiteSpace($title)){ continue }

  if(-not $titleMap.ContainsKey($title)){
    $titleMap[$title] = @()
  }
  $titleMap[$title] += $note.FullName.Substring($vaultRoot.Length + 1)
}

$duplicateTitles = @()
foreach($entry in $titleMap.GetEnumerator()){
  if($entry.Value.Count -gt 1){
    $duplicateTitles += [pscustomobject]@{
      title = $entry.Key
      paths = $entry.Value
    }
  }
}

$summary = [pscustomobject]@{
  generated_at = (Get-Date).ToString('s')
  scope = $Scope
  note_count = $notes.Count
  bad_note_count = $allIssues.Count
  p0 = ($allIssues | Where-Object { $_.severity -eq 'P0' } | Measure-Object).Count
  p1 = ($allIssues | Where-Object { $_.severity -eq 'P1' } | Measure-Object).Count
  p2 = ($allIssues | Where-Object { $_.severity -eq 'P2' } | Measure-Object).Count
  duplicate_title_count = $duplicateTitles.Count
}

function Write-State {
  param([pscustomobject]$summaryObj, [array]$issueRows)
  if(-not (Test-Path -LiteralPath $guardRoot)){
    New-Item -ItemType Directory -Force -Path $guardRoot | Out-Null
  }

  $state = [ordered]@{
    generated_at = $summaryObj.generated_at
    scope = $summaryObj.scope
    metrics = [ordered]@{
      note_count = $summaryObj.note_count
      bad_note_count = $summaryObj.bad_note_count
      p0_count = $summaryObj.p0
      p1_count = $summaryObj.p1
      p2_count = $summaryObj.p2
      duplicate_title_count = $summaryObj.duplicate_title_count
    }
    issues = @()
    duplicate_titles = @()
  }

  foreach($i in $issueRows){
    $state.issues += [ordered]@{
      path = $i.path
      severity = $i.severity
      count = $i.count
      items = $i.issues
    }
  }

  foreach($d in $duplicateTitles){
    $state.duplicate_titles += [ordered]@{ title = $d.title; paths = $d.paths }
  }

  $state | ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 -LiteralPath $statePath
}

switch($Command){
  'status' {
    Write-Output ("TOTAL_NOTES={0}" -f $summary.note_count)
    Write-Output ("BAD_NOTES={0}" -f $summary.bad_note_count)
    Write-Output ("P0={0}" -f $summary.p0)
    Write-Output ("P1={0}" -f $summary.p1)
    Write-Output ("P2={0}" -f $summary.p2)
    Write-Output ("DUPLICATE_TITLES={0}" -f $summary.duplicate_title_count)

    if($summary.duplicate_title_count -gt 0){
      Write-Output ('Duplicate title sample: ' + (($duplicateTitles | Select-Object -First 3 | ForEach-Object { $_.title }) -join '; '))
    }

    if($summary.bad_note_count -gt 0){
      foreach($i in ($allIssues | Sort-Object severity, path | Select-Object -First $Limit)){
        Write-Output ("- [{0}] {1}: {2}" -f $i.severity, $i.path, ($i.issues[0]))
      }
    }
  }

  'quality' {
    $report = Make-ReportPath
    $lines = @()
    $lines += '# Obsidian Quality Guardian Report'
    $lines += "GeneratedAt: $($summary.generated_at)"
    $lines += "Scope: $($summary.scope)"
    $lines += ''
    $lines += '## Metrics'
    $lines += "- total_notes: $($summary.note_count)"
    $lines += "- bad_notes: $($summary.bad_note_count)"
    $lines += "- p0: $($summary.p0)"
    $lines += "- p1: $($summary.p1)"
    $lines += "- p2: $($summary.p2)"
    $lines += "- duplicate_titles: $($summary.duplicate_title_count)"

    if($allIssues.Count -gt 0){
      $lines += ''
      $lines += '## Priority Fix List'
      foreach($i in ($allIssues | Sort-Object severity, path | Select-Object -First $Limit)){
        $lines += "### $($i.path)  [$($i.severity)]"
        foreach($it in $i.issues){
          $lines += "- $it"
        }
      }
    }
    else {
      $lines += ''
      $lines += 'No issues found in this scope.'
    }

    if($duplicateTitles.Count -gt 0){
      $lines += ''
      $lines += '## Duplicate Titles'
      foreach($d in $duplicateTitles){
        $lines += ('- ' + $d.title)
        foreach($p in $d.paths){
          $lines += ('  - ' + $p)
        }
      }
    }

    $lines += ''
    $lines += '## Borrowed from Codex workspace'
    $lines += '- Use status+quality two-step checks for periodic review loops.'
    $lines += '- Separate incident records with severity for follow-up tracking.'
    $lines += '- Keep temporary data outside vault and only keep final notes in vault.'

    Set-Content -LiteralPath $report -Value ($lines -join "`r`n") -Encoding UTF8

    Write-Output ("REPORT=" + $report)
    Write-State $summary $allIssues
  }

  'report' {
    if(Test-Path -LiteralPath $statePath){
      Get-Content -LiteralPath $statePath -Raw
    }
    else {
      'NO_STATE'
    }
  }
}
