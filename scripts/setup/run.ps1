# HeatGuard launcher (Windows / PowerShell)
# Creates a venv on first run, installs deps, then starts the API + dashboard.
# No API key required.
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

if (-not (Test-Path "$repo\.venv")) {
    python -m venv "$repo\.venv"
    & "$repo\.venv\Scripts\python.exe" -m pip install --upgrade pip
    & "$repo\.venv\Scripts\python.exe" -m pip install -r "$repo\requirements.txt"
}

Write-Host "HeatGuard -> http://localhost:8000" -ForegroundColor Green
& "$repo\.venv\Scripts\python.exe" -m uvicorn server:app --app-dir "$repo\src" --host 0.0.0.0 --port 8000
