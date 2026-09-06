param(
 [Parameter(Position=0,Mandatory=$true)][ValidateSet('status','search','recent','new','validate')][string]$Command,
 [string]$Query,[string]$Title,[string]$Source='',[string]$Path,
 [ValidateRange(1,200)][int]$Limit=30
)
$ErrorActionPreference='Stop'
$vaultRoot=(Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$inboxRoot=Join-Path $vaultRoot '0_Codex工作台\Inbox'
$templatePath=Join-Path $vaultRoot '0_Codex工作台\Templates\Codex知识笔记模板.md'
function Get-Notes { Get-ChildItem -LiteralPath $vaultRoot -Recurse -File -Filter '*.md' | Where-Object {$_.FullName -notmatch '[\\/](\.obsidian|\.trash)[\\/]'} }
function Rel([string]$p) { $p.Substring($vaultRoot.Length+1) }
switch($Command) {
 'status' {
  $files=@(Get-Notes); $inbox=@(Get-ChildItem -LiteralPath $inboxRoot -File -Filter '*.md')
  [pscustomobject]@{Vault=$vaultRoot;MarkdownNotes=$files.Count;InboxNotes=$inbox.Count;LastModified=($files|Sort-Object LastWriteTime -Descending|Select-Object -First 1).LastWriteTime}|Format-List
 }
 'search' {
  if([string]::IsNullOrWhiteSpace($Query)){throw 'search requires -Query.'}
  $found=foreach($f in Get-Notes){
   $rel=Rel $f.FullName; $nm=$f.BaseName -like "*$Query*"
   $hits=@(Select-String -LiteralPath $f.FullName -SimpleMatch -Pattern $Query -Encoding UTF8 -ErrorAction SilentlyContinue|Select-Object -First 2)
   if($nm -or $hits.Count){[pscustomobject]@{Path=$rel;NameMatch=$nm;Evidence=(($hits|ForEach-Object {$_.Line.Trim()}) -join ' | ')}}
  }
  $found|Sort-Object -Property @{Expression='NameMatch';Descending=$true},Path|Select-Object -First $Limit|Format-Table -Wrap
 }
 'recent' { Get-Notes|Sort-Object LastWriteTime -Descending|Select-Object -First $Limit @{N='Modified';E={$_.LastWriteTime.ToString('yyyy-MM-dd HH:mm')}},@{N='Path';E={Rel $_.FullName}}|Format-Table -AutoSize }
 'new' {
  if([string]::IsNullOrWhiteSpace($Title)){throw 'new requires -Title.'}
  $invalid=[IO.Path]::GetInvalidFileNameChars(); $safe=-join($Title.ToCharArray()|ForEach-Object{if($invalid -contains $_){'_'}else{$_}})
  $target=Join-Path $inboxRoot ($safe+'.md'); if(Test-Path -LiteralPath $target){throw "Note already exists: $target"}
  $c=Get-Content -Raw -LiteralPath $templatePath -Encoding UTF8
  $c=$c.Replace('{{date}}',(Get-Date -Format 'yyyy-MM-dd')).Replace('{{title}}',$Title).Replace('{{source}}',$Source.Replace('"','\"'))
  [IO.File]::WriteAllText($target,$c,[Text.UTF8Encoding]::new($false)); $target
 }
 'validate' {
  if([string]::IsNullOrWhiteSpace($Path)){throw 'validate requires -Path.'}
  $target=if([IO.Path]::IsPathRooted($Path)){$Path}else{Join-Path $vaultRoot $Path}; $resolved=(Resolve-Path -LiteralPath $target).Path
  if(-not $resolved.StartsWith($vaultRoot,[StringComparison]::OrdinalIgnoreCase)){throw 'Path must stay inside the vault.'}
  $c=Get-Content -Raw -LiteralPath $resolved -Encoding UTF8; $issues=[Collections.Generic.List[string]]::new()
  if($c -notmatch '(?s)^---\s*.*?\s*---'){$issues.Add('Missing YAML frontmatter.')}
  foreach($s in @('## 来源事实','## Codex 分析','## 关联笔记','## 待验证问题')){if(-not $c.Contains($s)){$issues.Add("Missing section: $s")}}
  foreach($p in @('gh[pousr]_[A-Za-z0-9_]{20,}','AKIA[0-9A-Z]{16}','-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----','(?i)(password|passwd|token|api[_-]?key)\s*[:=]\s*[^\s<]{8,}')){if($c -match $p){$issues.Add('Possible credential or secret detected.');break}}
  if($issues.Count){$issues|ForEach-Object{Write-Error $_ -ErrorAction Continue};exit 1}else{'OK: note passed validation.'}
 }
}