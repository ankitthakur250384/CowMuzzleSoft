<#
PowerShell helper to create a new Flutter Android app inside the repo under frontend/mobile.
Usage (from repo root):
  powershell -ExecutionPolicy Bypass -File scripts/create_flutter_app.ps1 -Name my_app -Org com.yourorg

This script only invokes the local `flutter` CLI, so ensure Flutter is installed and on PATH.
#>
param(
    [Parameter(Mandatory=$true)][string]$Name,
    [string]$Org = "com.example"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")
$target = Join-Path $repoRoot (Join-Path "frontend\mobile" $Name)

if (-not (Get-Command flutter -ErrorAction SilentlyContinue)) {
    Write-Error "flutter CLI not found. Install Flutter and add to PATH: https://flutter.dev/docs/get-started/install"
    exit 1
}

if (Test-Path $target) {
    Write-Error "Target path already exists: $target"
    exit 1
}

Write-Host "Creating Flutter app '$Name' at: $target" -ForegroundColor Green

# Run flutter create with provided org and project name
$cmd = "flutter create --org $Org --project-name $Name $target"
Write-Host "Running: $cmd"
$proc = Start-Process -FilePath flutter -ArgumentList @('create','--org',$Org,'--project-name',$Name,$target) -NoNewWindow -Wait -PassThru
if ($proc.ExitCode -ne 0) {
    Write-Error "flutter create failed with exit code $($proc.ExitCode)"
    exit $proc.ExitCode
}

Write-Host "Created app. To fetch dependencies run:" -ForegroundColor Cyan
Write-Host "  cd frontend\mobile\$Name" -ForegroundColor Yellow
Write-Host "  flutter pub get" -ForegroundColor Yellow
Write-Host "To run on Android device/emulator:" -ForegroundColor Cyan
Write-Host "  flutter devices" -ForegroundColor Yellow
Write-Host "  flutter run -d <device-id>" -ForegroundColor Yellow

exit 0
