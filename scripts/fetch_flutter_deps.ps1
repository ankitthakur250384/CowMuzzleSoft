# PowerShell script to run `flutter pub get` for mobile Flutter app(s)
# Run this from the repository root or any path — script resolves repo root relative to its own location.

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")

# Paths to run flutter pub get in
$paths = @(
    "frontend\mobile\flutter_app",
    "frontend\mobile"
)

foreach ($p in $paths) {
    $full = Join-Path $repoRoot $p
    if (Test-Path $full) {
        Push-Location $full
        if (Test-Path (Join-Path $full "pubspec.yaml")) {
            Write-Host "Running: flutter pub get in $full"
            try {
                flutter pub get
            } catch {
                Write-Host "Failed to run 'flutter pub get' in $full. Make sure Flutter is installed and on PATH." -ForegroundColor Red
            }
        } else {
            Write-Host "No pubspec.yaml in $full — skipping." -ForegroundColor Yellow
        }
        Pop-Location
    } else {
        Write-Host "Path not found: $full" -ForegroundColor Yellow
    }
}
