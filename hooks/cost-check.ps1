$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspace = if ($args.Count -gt 0) { $args[0] } else { (Get-Location).Path }
python (Join-Path $scriptDir "..\scripts\hook_runner.py") cost-check $workspace
