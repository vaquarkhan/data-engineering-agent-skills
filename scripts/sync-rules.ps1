param(
  [Parameter(Mandatory = $true)]
  [string]$Target
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$InstallScript = Join-Path $ScriptDir "install.sh"

if (-not (Test-Path $InstallScript)) {
  throw "install.sh not found at $InstallScript"
}

bash $InstallScript --tool all --target $Target --force
if ($LASTEXITCODE -ne 0) {
  exit $LASTEXITCODE
}
