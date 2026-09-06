param(
 [Parameter(Position=0,Mandatory=$true)]
 [ValidateSet('baseline','sync','status')]
 [string]$Command,
 [string]$SearchQuery = '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (ti:inference OR abs:inference OR ti:prefill OR abs:prefill OR ti:decoding OR abs:decoding OR all:"kv cache" OR all:kv-cache OR all:speculative OR all:MoE OR all:"tensor parallel" OR all:serving OR all:"LLM serving" OR all:"token throughput")',
 [int]$MaxResults=40,
 [int]$TimeoutSec=25
)
$ErrorActionPreference='Stop'
$vaultRoot=(Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$stateDir=Join-Path $vaultRoot '1_AI情报溯源\状态'
$statePath=Join-Path $stateDir 'ai-inference-arxiv-checkpoints.json'
$radarTool=Join-Path $vaultRoot '0_Codex工作台\tools\inference-radar.ps1'
$keywords=@('inference','prefill','decoding','kv cache','kv-cache','speculative','throughput','latency','tensor parallel','Mixture-of-Experts','MoE','trt','continuous batching','serving','kv cache reuse','kernel fusion')

function To-Hashtable($obj){
 if($null -eq $obj){ return @{} }
 if($obj -is [hashtable]){ return $obj }
 if($obj -is [System.Collections.IDictionary]){
  $h=@{}
  foreach($key in $obj.Keys){ $h[$key]=$obj[$key] }
  return $h
 }
 if($obj -is [psobject]){
  $h=@{}
  foreach($p in $obj.PSObject.Properties){ $h[$p.Name]=$p.Value }
  return $h
 }
 return @{}
}

function Get-State {
 if(Test-Path -LiteralPath $statePath){
  try {
   $raw=Get-Content -Raw -LiteralPath $statePath -Encoding UTF8
   $obj=ConvertFrom-Json -InputObject $raw -Depth 20
   return $obj
  } catch {
   Write-Warning ('State load failed, reset state: '+$_.Exception.Message)
  }
 }
 return @{schema_version=1;created_at=(Get-Date).ToString('s');updated_at=$null;seen=@{};last_published=$null;query=$SearchQuery}
}

function Save-State($state) {
 New-Item -ItemType Directory -Force -Path $stateDir|Out-Null
 $state.updated_at=(Get-Date).ToString('s')
 [IO.File]::WriteAllText($statePath,($state|ConvertTo-Json -Depth 10),[Text.UTF8Encoding]::new($true))
}

function Get-ArxivEntries {
 $uri='https://export.arxiv.org/api/query?search_query='+[uri]::EscapeDataString($SearchQuery)+'&start=0&max_results='+$MaxResults+'&sortBy=submittedDate&sortOrder=descending'
 try {
  $feed=Invoke-RestMethod -Uri $uri -TimeoutSec $TimeoutSec -Headers @{ 'User-Agent'='Codex-Inference-Arxiv-Radar' }
  return @($feed.feed.entry)
 } catch {
  throw ('Arxiv fetch failed: '+$_.Exception.Message)
 }
}

function ExtractText($value) {
 if($null -eq $value){ return '' }
 return (($value.ToString() -replace '\s+',' ').Trim())
}

function Is-Match($entry) {
 $text=(($entry.title)+' ' + ($entry.summary))
 $lower=$text.ToLowerInvariant()
 $matched=@()
 foreach($keyword in $keywords){
  if($lower -like ('*'+$keyword.ToLowerInvariant()+'*')){ $matched+=$keyword }
 }
 if($matched.Count -eq 0){ return @($false,@()) }
 return @($true,$matched)
}

$state=Get-State
$state.seen = To-Hashtable $state.seen
$state.query = $SearchQuery

if($Command -eq 'status'){
 $rows=foreach($pair in $state.seen.GetEnumerator()){
  [pscustomobject]@{PaperId=$pair.Name;Detected=if($pair.Value){$pair.Value}else{''}}
 }
 [pscustomobject]@{StateFile=$statePath;Schema=$state.schema_version;LastPublished=$state.last_published;TotalSeen=$rows.Count;ActiveQuery=$state.query}|Format-List
 if($rows.Count -gt 0){ $rows|Sort-Object Detected -Descending|Format-Table -AutoSize }
 exit 0
}

$entries=Get-ArxivEntries
$changes=@()
foreach($entry in $entries){
 $id=ExtractText($entry.id)
 if(-not $id){continue}
 $idKey=$id.ToLowerInvariant()
 $published=ExtractText($entry.published)
 $title=ExtractText($entry.title)
 $summary=ExtractText($entry.summary)
 $match, $matched = Is-Match $entry
 if(-not $match){ continue }
 if(-not $state.seen.ContainsKey($idKey)){
  $changes += @{
    Id=$idKey;
    Url=$id;
    Title=$title;
    Published=$published;
    Summary=$summary;
    Matched=$matched
  }
 }
 $state.seen[$idKey]=$published
 if(-not $state.last_published -or ([DateTime]$published) -gt ([DateTime]$state.last_published)){
  $state.last_published=$published
 }
}

if($Command -eq 'baseline'){
 Save-State $state
 Write-Output ('ARXIV_BASELINE_SAVED='+$statePath)
 exit 0
}

$created=0
if($Command -eq 'sync'){
 if($changes.Count -gt 0){
  foreach($item in $changes){
   $card=& $radarTool new -Title $item.Title -Source $item.Url -Topic serving
   $cardText=Get-Content -Raw -LiteralPath $card -Encoding UTF8
   $abstract=$item.Summary
   if($abstract.Length -gt 280){$abstract=$abstract.Substring(0,280)+'...'}
   $summaryLine='Auto-detected by arXiv monitor. Published='+$item.Published+'. Matched keywords: '+([string]::Join(', ',$item.Matched))+'. URL: '+$item.Url+'. Abstract: '+$abstract
   $cardText=$cardText -replace 'source_type: paper','source_type: arxiv-preprint' -replace 'evidence_score: 0','evidence_score: 2' -replace 'relevance_score: 0','relevance_score: 4' -replace 'impact_score: 0','impact_score: 2' -replace 'novelty_score: 0','novelty_score: 2' -replace 'urgency_score: 0','urgency_score: 2' -replace 'reproducibility_score: 0','reproducibility_score: 3' -replace 'overall_score: 0','overall_score: 2.5' -replace 'confidence: low','confidence: medium'
   $cardText=[regex]::Replace($cardText,'(?m)^## 事件`r?$','## 事件`r`n`r`n- '+$summaryLine,[Text.RegularExpressions.RegexOptions]::Multiline)
   [IO.File]::WriteAllText($card,$cardText,[Text.UTF8Encoding]::new($true))
   Write-Output ('ARXIV_CANDIDATE_CREATED='+$card)
   $created++
  }
 }
}

Save-State $state
Write-Output ('ARXIV_CHANGES='+$changes.Count)
Write-Output ('ARXIV_CREATED='+$created)
