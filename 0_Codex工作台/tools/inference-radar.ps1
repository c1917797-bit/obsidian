param(
    [Parameter(Position=0,Mandatory=$true)]
    [ValidateSet('status','new','validate','rank','digest')]
    [string]$Command,
    [string]$Title,
    [string]$Source,
    [ValidateSet('serving','kernel','memory','compression','distributed','hardware-economics','other')]
    [string]$Topic='other',
    [string]$Path,
    [ValidateRange(1,200)][int]$Limit=20,
    [ValidateSet('today','week')][string]$Window='today',
    [string]$Status='',
    [double]$MinOverall=0
)
$ErrorActionPreference='Stop'
$vaultRoot=(Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$radarRoot=Join-Path $vaultRoot '3_AI情报日历\Inbox\InferenceRadar'
$templatePath=Join-Path $vaultRoot '0_Codex工作台\Templates\AI推理信号卡模板.md'
$reportDate=(Get-Date)

function Field($content,$name){
    $m=[regex]::Match($content,'(?m)^'+[regex]::Escape($name)+':\s*"?([^"\r\n]*)"?\s*$')
    if($m.Success){$m.Groups[1].Value.Trim()}else{''}
}

function ParseInt([string]$text, [int]$default=0){
    if([string]::IsNullOrWhiteSpace($text)){ return $default }
    try { return [int]$text } catch { return $default }
}

function ParseDouble([string]$text, [double]$default=0){
    if([string]::IsNullOrWhiteSpace($text)){ return $default }
    try { return [double]$text } catch { return $default }
}

function ParseDateLoose([string]$v){
    if([string]::IsNullOrWhiteSpace($v)){ return $null }
    try { return [datetime]$v } catch { return $null }
}

function CardTitle($content,[string]$fallback){
    $m=[regex]::Match($content,'(?m)^#\s+(.+)$')
    if($m.Success){$m.Groups[1].Value.Trim()}else{$fallback}
}

function Cards {
    Get-ChildItem -LiteralPath $radarRoot -File -Filter '*.md' -Recurse |
      Where-Object { $_.Name -ne 'README.md' -and $_.Name -notlike '问题清单*' -and $_.Name -notlike '*归档*' }
}

function Inspect($target){
    $content=Get-Content -Raw -LiteralPath $target
    $issues=@()
    foreach($field in @('type','date','discovered','source_type','primary_source','topic','status','evidence_score','overall_score','confidence','decision')){
        if([string]::IsNullOrWhiteSpace((Field $content $field))){$issues+="Missing field: $field"}
    }
    foreach($section in @('## 事件','## 一手证据','## 定量结果','## 适用边界','## Codex 判断','## 下一步')){
        if(-not $content.Contains($section)){$issues+="Missing section: $section"}
    }
    if((Field $content 'primary_source') -notmatch '^https://'){
        $issues+='primary_source must be an HTTPS original source.'
    }
    $e=ParseInt (Field $content 'evidence_score')
    if($e -lt 2 -and $content -match '显著提升|重大突破|行业领先|大幅降低'){
        $issues+='Strong claim used with evidence_score below 2.'
    }
    [pscustomobject]@{Valid=($issues.Count -eq 0);Issues=$issues}
}

function Build-CardRow($file){
    $content=Get-Content -Raw -LiteralPath $file.FullName
    [pscustomobject]@{
        Path=$file.FullName
        RelPath=$file.FullName.Substring($vaultRoot.Length+1)
        Title=(CardTitle $content $file.BaseName)
        Discovered=ParseDateLoose (Field $content 'discovered')
        Topic=(Field $content 'topic')
        Status=(Field $content 'status')
        Evidence=(ParseInt (Field $content 'evidence_score'))
        Overall=(ParseDouble (Field $content 'overall_score'))
        Decision=(Field $content 'decision')
        Confidence=(Field $content 'confidence')
        Source=(Field $content 'primary_source')
        Content=$content
    }
}

function Render-Digest([string]$outPath,[string]$mode,[string]$statusFilter,[double]$overallFloor){
    $rows=@()
    foreach($file in Cards){
        $rows += Build-CardRow $file
    }

    $rows = $rows | Where-Object { $_.Status -ne '' }
    $startDate = switch($mode){
        'week' { $reportDate.Date.AddDays(-6) }
        default { $reportDate.Date }
    }
    $endDate = $reportDate.Date.AddDays(1)

    $inWindow = $rows | Where-Object { $_.Discovered -ne $null -and $_.Discovered -ge $startDate -and $_.Discovered -lt $endDate }
    if($statusFilter){ $inWindow = $inWindow | Where-Object { $_.Status -eq $statusFilter } }
    if($overallFloor -gt 0){ $inWindow = $inWindow | Where-Object { $_.Overall -ge $overallFloor } }

    $sorted = $inWindow | Sort-Object @{Expression='Overall';Descending=$true},@{Expression='Evidence';Descending=$true}
    $top = $sorted | Select-Object -First $Limit

    $out=@()
    $out += "# AI Inference Brief ($(Get-Date -Format 'yyyy-MM-dd'))"
    $out += ""
    $out += "窗口: $mode / 生成时间: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    $out += ""
    if($top.Count -eq 0){
        $out += "无满足条件的卡片。"
    } else {
        $out += "## 关键候选"
        $out += ""
        foreach($r in $top){
            $ts = if($r.Discovered){$r.Discovered.ToString('yyyy-MM-dd')} else { '时间缺失' }
            $out += "- $($r.Title)（$ts）"
            $out += "  - topic: $($r.Topic) / status: $($r.Status)"
            $out += "  - score: overall=$($r.Overall) evidence=$($r.Evidence) confidence=$($r.Confidence)"
            if($r.Decision){ $out += "  - decision: $($r.Decision)"}
            if($r.Source){ $out += "  - source: $($r.Source)"}
            $out += "  - path: $($r.RelPath)"
            $out += ""
        }
    }
    $out += "## 操作建议"
    $out += "- 先把 `status=verify` 且 evidence<2 的卡补齐一手可复核证据，再决定是否升级。"
    $out += "- 对 `overall>=4 && evidence>=2` 的卡，建立对应复现实验记录和回归窗口。"
    [IO.File]::WriteAllText($outPath,($out -join "`r`n"),[Text.UTF8Encoding]::new($true))
    Write-Output $outPath
}

switch($Command){
'status'{
  $cards=@(Cards)
  $valid=0
  foreach($card in $cards){if((Inspect $card.FullName).Valid){$valid++}}
  [pscustomobject]@{Vault=$vaultRoot;Cards=$cards.Count;Valid=$valid;Inbox=$radarRoot}|Format-List
}
'new'{
  if(!$Title){throw 'new requires -Title'}
  if($Source -notmatch '^https://'){throw 'new requires an HTTPS original -Source'}
  $folder=Join-Path $radarRoot (Get-Date -Format 'yyyy-MM')
  New-Item -ItemType Directory -Force -Path $folder|Out-Null
  $safe=$Title -replace '[\\/:*?"<>|]','_'
  $target=Join-Path $folder ((Get-Date -Format 'yyyy-MM-dd')+'_'+$safe+'.md')
  if(Test-Path $target){throw 'Signal already exists'}
  $content=Get-Content -Raw $templatePath
  $content=$content.Replace('{{date}}',(Get-Date -Format 'yyyy-MM-dd')).Replace('{{timestamp}}',(Get-Date).ToString('s')).Replace('{{source}}',$Source).Replace('{{title}}',$Title).Replace('{{topic}}',$Topic)
  [IO.File]::WriteAllText($target,$content,[Text.UTF8Encoding]::new($false))
  $target
}
'validate'{
  if(!$Path){throw 'validate requires -Path'}
  $target=if([IO.Path]::IsPathRooted($Path)){$Path}else{Join-Path $vaultRoot $Path}
  $target=(Resolve-Path $target).Path
  if(-not $target.StartsWith($vaultRoot,[StringComparison]::OrdinalIgnoreCase)){throw 'Path outside vault'}
  $result=Inspect $target
  if($result.Valid){'OK'}else{$result.Issues|ForEach-Object{Write-Error $_ -ErrorAction Continue};exit 1}
}
'rank'{
  $rows=foreach($card in Cards){
      $content=Get-Content -Raw $card.FullName
      [pscustomobject]@{
          Score=ParseDouble (Field $content 'overall_score')
          Evidence=ParseInt (Field $content 'evidence_score')
          Topic=Field $content 'topic'
          Status=Field $content 'status'
          Path=$card.FullName.Substring($vaultRoot.Length+1)
      }
  }
  $rows|Sort-Object Score -Descending|Select-Object -First $Limit|Format-Table -AutoSize
}
'digest'{
  $file=Join-Path $radarRoot ("AI推理简报_"+$reportDate.ToString('yyyy-MM-dd')+".md")
  Render-Digest -outPath $file -mode $Window -statusFilter $Status -overallFloor $MinOverall
  "REPORT_WRITTEN=$file"
}
}


