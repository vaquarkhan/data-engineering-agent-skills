$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$targetDir = if ($args.Count -ge 1) { $args[0] } else { (Get-Location).Path }
$toolMode = if ($args.Count -ge 2) { $args[1] } else { "auto" }

Write-Host "Bootstrapping Data Engineering Agent Skills"
Write-Host "Target: $targetDir"
Write-Host "Tool mode: $toolMode"

python (Join-Path $repoRoot "scripts\install_toolkit.py") --tool $toolMode --target $targetDir
Write-Host "Bootstrap complete."
