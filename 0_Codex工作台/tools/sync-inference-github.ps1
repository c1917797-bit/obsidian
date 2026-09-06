param(
 [Parameter(Position=0,Mandatory=$true)]
 [ValidateSet('baseline','sync','status')]
 [string]$Command,
 [int]$TimeoutSec=20
)

$ErrorActionPreference='Stop'
$vaultRoot=(Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$stateDir=Join-Path $vaultRoot '1_AI情报溯源\状态'
$statePath=Join-Path $stateDir 'ai-inference-github-checkpoints.json'
$radarTool=Join-Path $vaultRoot '0_Codex工作台\tools\inference-radar.ps1'

$projects=@(
 @{Name='vLLM';Repo='vllm-project/vllm';Topic='serving'},
 @{Name='SGLang';Repo='sgl-project/sglang';Topic='serving'},
 @{Name='TensorRT-LLM';Repo='NVIDIA/TensorRT-LLM';Topic='serving'},
 @{Name='llama.cpp';Repo='ggml-org/llama.cpp';Topic='compression'},
 @{Name='FlashAttention';Repo='Dao-AILab/flash-attention';Topic='kernel'},
 @{Name='DeepSpeed';Repo='deepspeedai/DeepSpeed';Topic='distributed'},
 @{Name='Megatron-LM';Repo='NVIDIA/Megatron-LM';Topic='distributed'},
 @{Name='LMCache';Repo='LMCache/LMCache';Topic='memory'},
 @{Name='Mooncake';Repo='kvcache-ai/Mooncake';Topic='memory'},
 @{Name='DeepEP';Repo='deepseek-ai/DeepEP';Topic='distributed'}
)

function ConvertTo-ObjectHash($value){
  if($null -eq $value){ return $null }
  if($value -is [hashtable]){ return $value }
  if($value -is [System.Collections.IEnumerable] -and $value -isnot [string]){
    return @($value | ForEach-Object { ConvertTo-ObjectHash $_ })
  }
  if($value -is [psobject]){
    $h=@{}
    foreach($p in $value.PSObject.Properties){
      $h[$p.Name]=ConvertTo-ObjectHash $p.Value
    }
    return $h
  }
  return $value
}

function Get-State {
  if(Test-Path -LiteralPath $statePath){
    try {
      $raw = Get-Content -Raw -LiteralPath $statePath -Encoding UTF8
      $obj = ConvertFrom-Json -InputObject $raw -Depth 20
      return ConvertTo-ObjectHash $obj
    } catch {
      Write-Warning ('State load failed, reset state: ' + $_.Exception.Message)
    }
  }
  return @{schema_version=1;created_at=(Get-Date).ToString('s');updated_at=$null;projects=@{}}
}

function Save-State($state) {
  New-Item -ItemType Directory -Force -Path $stateDir|Out-Null
  $state.updated_at=(Get-Date).ToString('s')
  [IO.File]::WriteAllText($statePath,($state | ConvertTo-Json -Depth 12),[Text.UTF8Encoding]::new($true))
}

function Get-LatestRelease($project) {
  $uri='https://api.github.com/repos/'+$project.Repo+'/releases/latest'
  try {
    $result=Invoke-RestMethod -Uri $uri -Headers @{Accept='application/vnd.github+json';'User-Agent'='Codex-Obsidian-Inference-Radar'} -TimeoutSec $TimeoutSec
    return @{ok=$true;tag=[string]$result.tag_name;published=[string]$result.published_at;url=[string]$result.html_url;name=[string]$result.name;prerelease=[bool]$result.prerelease}
  } catch { return @{ok=$false;error=$_.Exception.Message} }
}

$state=Get-State
if(!$state.projects){$state.projects=@{}}

if($Command -eq 'status'){
  $rows=foreach($project in $projects){
    $saved = $null
    if($state.projects.ContainsKey($project.Repo)){
      $saved = $state.projects[$project.Repo]
    }
    $tag = if($saved){$saved.tag}else{''}
    $published = if($saved){$saved.published}else{''}
    $checked = if($saved){$saved.checked_at}else{''}

    [pscustomobject]@{
      Project=$project.Name
      Repo=$project.Repo
      Tag=$tag
      Published=$published
      Checked=$checked
    }
  }
  $rows | Format-Table -AutoSize
  exit 0
}

$changes=@()
foreach($project in $projects){
  $latest=Get-LatestRelease $project
  if(!$latest.ok){Write-Warning ($project.Name+': '+$latest.error);continue}
  $previous=$state.projects[$project.Repo]
  if($Command -eq 'sync' -and $previous -and $previous.tag -ne $latest.tag){
    $changes += @{Project=$project;Latest=$latest;Previous=$previous.tag}
  }
  $state.projects[$project.Repo]=@{
    name=$project.Name
    tag=$latest.tag
    published=$latest.published
    url=$latest.url
    release_name=$latest.name
    prerelease=$latest.prerelease
    checked_at=(Get-Date).ToString('s')
  }
  Write-Output ($project.Name+' '+$latest.tag)
}

Save-State $state
if($Command -eq 'baseline'){
  Write-Output ('BASELINE_SAVED='+$statePath)
  exit 0
}

foreach($change in $changes){
  $title=$change.Project.Name+' release '+$change.Latest.tag
  $card=& $radarTool new -Title $title -Source $change.Latest.url -Topic $change.Project.Topic
  $cardText=Get-Content -Raw -LiteralPath $card -Encoding UTF8
  $cardText=$cardText -replace 'source_type: paper','source_type: github-release' -replace 'evidence_score: 0','evidence_score: 2' -replace 'relevance_score: 0','relevance_score: 4' -replace 'impact_score: 0','impact_score: 2' -replace 'novelty_score: 0','novelty_score: 2' -replace 'urgency_score: 0','urgency_score: 2' -replace 'reproducibility_score: 0','reproducibility_score: 3' -replace 'overall_score: 0','overall_score: 2.5' -replace 'confidence: low','confidence: medium'
  $safeSummary = 'AutoDetection: Release change from '+$change.Previous+' to '+$change.Latest.tag+'. Release notes have not been reviewed; no performance conclusion is made.'
  $cardText=[regex]::Replace($cardText,'(?m)^## 事件`r?$','## 事件`r`n`r`n- '+$safeSummary,[Text.RegularExpressions.RegexOptions]::Multiline)
  [IO.File]::WriteAllText($card,$cardText,[Text.UTF8Encoding]::new($true))
  Write-Output ('CANDIDATE_CREATED='+$card)
}

Write-Output ('CHANGES='+$changes.Count)
