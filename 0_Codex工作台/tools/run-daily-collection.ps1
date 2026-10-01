param(
  [Parameter(Position=0)]
  [ValidateSet('full','arxiv','github','pipeline','radar','setup-task')]
  [string]$Command = 'full',
  [switch]$SkipPipeline
)

<#
  每日采集统一入口
  顺序：arXiv 同步 → GitHub 同步 → 情报流水线(main.py daily，可选) → 雷达 digest
  每次运行在 1_AI情报溯源/状态/daily-collection-state.json 记录 last_seen / fetched_at；
  source_published 由各同步工具的 checkpoint 维护（arxiv.last_published / github.published）。
#>
$ErrorActionPreference = 'Continue'
$tools = Split-Path -Parent $MyInvocation.MyCommand.Path
$vault = (Resolve-Path (Join-Path $tools '..\..')).Path
$stateDir = Join-Path $vault '1_AI情报溯源\状态'
$statePath = Join-Path $stateDir 'daily-collection-state.json'
$osDir = Join-Path $vault '2_AI情报织网\ai-intelligence-os'

function Get-Now { (Get-Date).ToString('yyyy-MM-ddTHH:mm:ss') }

function Load-State {
  if (Test-Path -LiteralPath $statePath) {
    try { return (Get-Content -Raw -LiteralPath $statePath -Encoding UTF8 | ConvertFrom-Json) } catch {}
  }
  return [pscustomobject]@{ schema_version=1; last_run=$null; last_seen=$null; history=@() }
}

function Save-State($state) {
  New-Item -ItemType Directory -Force -Path $stateDir | Out-Null
  $state.last_seen = Get-Now
  [IO.File]::WriteAllText($statePath, ($state | ConvertTo-Json -Depth 8), [Text.UTF8Encoding]::new($true))
}

function Run-Tool($script, $params, $label) {
  Write-Host "== [$label] $(Get-Now) ==" -ForegroundColor Cyan
  $logDir = Join-Path $env:TEMP 'opencode\dailycollect'
  New-Item -ItemType Directory -Force -Path $logDir | Out-Null
  $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
  $outLog = Join-Path $logDir ($label + '_' + $stamp + '.log')
  $errLog = $outLog + '.err'
  try {
    $cmdArgs = @('-NoProfile','-ExecutionPolicy','Bypass','-File',$script) + @($params)
    $p = Start-Process -FilePath 'powershell.exe' -ArgumentList $cmdArgs -RedirectStandardOutput $outLog -RedirectStandardError $errLog -Wait -WindowStyle Hidden -PassThru
    if (Test-Path -LiteralPath $outLog) { Get-Content -LiteralPath $outLog -Encoding UTF8 | ForEach-Object { Write-Output "   $_" } }
    if (Test-Path -LiteralPath $errLog) { $e = Get-Content -LiteralPath $errLog -Encoding UTF8 | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }; if ($e) { $e | ForEach-Object { Write-Warning "   $_" } } }
    return ($p.ExitCode -eq 0)
  } catch {
    Write-Warning "   [$label] 失败: $($_.Exception.Message)"
    return $false
  }
}

$state = Load-State
$steps = @()

switch ($Command) {
  'full' {
    $steps += @{ Name='arXiv同步';    Ok=(Run-Tool (Join-Path $tools 'sync-inference-arxiv.ps1')  @('sync') 'arXiv同步') }
    $steps += @{ Name='GitHub同步';   Ok=(Run-Tool (Join-Path $tools 'sync-inference-github.ps1') @('sync') 'GitHub同步') }
    if (-not $SkipPipeline) {
      if ($env:MINIMAX_API_KEY) {
        $steps += @{ Name='情报流水线'; Ok=(Run-Tool (Join-Path $osDir 'run_daily.ps1') @() '情报流水线') }
      } else {
        Write-Warning '   未设置 MINIMAX_API_KEY，跳过情报流水线(main.py daily)'
        $steps += @{ Name='情报流水线'; Ok=$false }
      }
    }
    $steps += @{ Name='雷达digest';   Ok=(Run-Tool (Join-Path $tools 'inference-radar.ps1') @('digest') '雷达digest') }
  }
  'arxiv'    { $steps += @{ Name='arXiv同步'; Ok=(Run-Tool (Join-Path $tools 'sync-inference-arxiv.ps1') @('sync') 'arXiv同步') } }
  'github'   { $steps += @{ Name='GitHub同步'; Ok=(Run-Tool (Join-Path $tools 'sync-inference-github.ps1') @('sync') 'GitHub同步') } }
  'pipeline' { $steps += @{ Name='情报流水线'; Ok=(Run-Tool (Join-Path $osDir 'run_daily.ps1') @() '情报流水线') } }
  'radar'    { $steps += @{ Name='雷达digest'; Ok=(Run-Tool (Join-Path $tools 'inference-radar.ps1') @('digest') '雷达digest') } }
  'setup-task' {
    $self = $MyInvocation.MyCommand.Path
    $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$self`" full"
    $trigger = New-ScheduledTaskTrigger -Daily -At 08:00
    $settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopIfGoingOnBatteries
    Register-ScheduledTask -TaskName 'IntelligenceInference_DailyCollect' -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null
    Write-Output '已注册 Windows 计划任务：IntelligenceInference_DailyCollect（每天 08:00）'
    return
  }
}

$now = Get-Now
$record = [ordered]@{ run_at=$now; fetched_at=$now; steps=$steps }
$state.last_run = $now
$state.history = @($record) + @($state.history | Where-Object { $_ -is [pscustomobject] }) | Select-Object -First 20
Save-State $state

$failed = $steps | Where-Object { -not $_.Ok }
Write-Host ''
Write-Host "== 每日采集完成：$($steps.Count - $failed.Count)/$($steps.Count) 步成功 ==" -ForegroundColor $(if($failed.Count){'Yellow'}else{'Green'})
if ($failed.Count) { $failed | ForEach-Object { Write-Warning "   失败步骤: $($_.Name)" } }