param(
    [ValidateSet("scan","report")][string]$Command = "scan",
    [int]$MaxAgeDays = 30
)

$ErrorActionPreference = 'Stop'
$vaultRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$calendarDir = Get-ChildItem -LiteralPath $vaultRoot -Directory | Where-Object { $_.Name -like '3_AI*' } | Select-Object -First 1
if(-not $calendarDir){ throw 'Cannot find calendar folder.' }

$radarRoot = Join-Path $calendarDir.FullName 'Inbox\InferenceRadar'
$reportPath = Join-Path $radarRoot '问题清单.md'

function FieldVal($content, $name){
    $pattern = '(?m)^' + [regex]::Escape($name) + ':\s*"?([^"\r\n]*)"?\s*$'
    $m = [regex]::Match($content, $pattern)
    if($m.Success){ return $m.Groups[1].Value.Trim() }
    return ""
}

function HasUnverifiedText($content) {
    $patterns = @(
        '待核验',
        '待补充',
        '待确认',
        '待核对',
        '待补齐',
        '待验证',
        'TODO'
    )
    foreach($p in $patterns){
        if($content -match $p){ return $true }
    }
    return $false
}

if(-not (Test-Path -LiteralPath $radarRoot)){
    Write-Output "TOTAL=0"
    Write-Output "BAD=0"
    Write-Output "STALE=0"
    Write-Output "DUPLICATE=0"
    exit 0
}

$allFiles = Get-ChildItem -LiteralPath $radarRoot -File -Filter '*.md' -Recurse |
  Where-Object { $_.Name -notin @('README.md','问题清单.md') }

$files = foreach($f in $allFiles){
  $content = Get-Content -Raw -LiteralPath $f.FullName
  if($content -match '(?m)^type:\s*'){ $f }
}

$rows = @()
$titleBuckets = @{}

foreach($f in $files){
    $content = Get-Content -Raw -LiteralPath $f.FullName
    $issues = @()

    $required = @('type','date','discovered','source_type','primary_source','topic','status','evidence_score','overall_score','confidence','decision')
    $missing = @()
    foreach($k in $required){ if([string]::IsNullOrWhiteSpace((FieldVal $content $k))){ $missing += $k } }

    $primary = FieldVal $content 'primary_source'
    if(-not [string]::IsNullOrWhiteSpace($primary) -and $primary -notmatch '^https://'){ $issues += 'primary_source_not_https' }

    $evidence = 0
    [void][int]::TryParse((FieldVal $content 'evidence_score'), [ref]$evidence)
    if($evidence -eq 0){ $issues += 'evidence_zero' }

    if(HasUnverifiedText $content){ $issues += 'unverified_placeholder' }

    $status = FieldVal $content 'status'
    if(-not ($status -in @('candidate','monitor','ignore','deep_read','replicate','insight'))){
        $issues += 'invalid_status'
    }

    $ageDays = $null
    $ds = FieldVal $content 'discovered'
    if($ds){
        try { $ageDays = [int]((Get-Date) - [DateTime]::Parse($ds)).TotalDays }
        catch {}
    }

    $title = [regex]::Match($content, '(?m)^#\s+(.+)$')
    $titleText = if($title.Success){ $title.Groups[1].Value.Trim() } else { $f.Name }

    if($missing.Count -gt 0){ $issues += 'missing_fields' }

    $rows += [pscustomobject]@{
        Path = $f.FullName
        Title = $titleText
        Status = $status
        AgeDays = $ageDays
        Issues = $issues
        Missing = ($missing -join ',')
    }

    if($titleBuckets.ContainsKey($titleText)){
        $titleBuckets[$titleText] += @($f.FullName)
    } else { $titleBuckets[$titleText] = @($f.FullName) }
}

$bad = $rows | Where-Object { $_.Issues.Count -gt 0 }
$stale = $rows | Where-Object { $_.Status -eq 'candidate' -and $_.AgeDays -ne $null -and $_.AgeDays -gt $MaxAgeDays }
$dups = $titleBuckets.GetEnumerator() | Where-Object { $_.Value.Count -gt 1 }

if($Command -eq 'scan'){
    Write-Output "TOTAL=$($rows.Count)"
    Write-Output "BAD=$($bad.Count)"
    Write-Output "STALE=$($stale.Count)"
    Write-Output "DUPLICATE=$($dups.Count)"
    exit 0
}

$out = @()
$out += '# AI Inference Quality Issue Report'
$out+= "- Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$out+= "- Total cards: $($rows.Count)"
$out+= "- Bad cards: $($bad.Count)"
$out+= "- Candidate older than $MaxAgeDays days: $($stale.Count)"
$out+= "- Duplicate titles: $($dups.Count)"
$out += ''
$out+= '## Bad cards'
foreach($r in ($bad | Sort-Object Path)){
    $out += "- $($r.Title) | $($r.Path)"
    foreach($i in $r.Issues){ $out += "  - $i" }
    if($r.Missing){ $out += "  - missing: $($r.Missing)" }
}
$out+= ''
$out+= '## Duplicate titles'
foreach($d in $dups){
    $out += "- $($d.Key)"
    foreach($p in $d.Value){$out += "  - $p"}
}
$out+= ''
$out+= "## Candidate cards older than $MaxAgeDays days"
foreach($r in ($stale | Sort-Object AgeDays -Descending)){
    $out += "- $($r.Title) ($($r.AgeDays)d)"
}

New-Item -ItemType Directory -Force -Path (Split-Path $reportPath -Parent) | Out-Null
[IO.File]::WriteAllText($reportPath, ($out -join "`r`n"), [Text.UTF8Encoding]::new($true))
Write-Output "REPORT_WRITTEN=$reportPath"

