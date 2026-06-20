<#
.SYNOPSIS
    Downloads the HealthinClimate starter datasets into data/raw/.

.DESCRIPTION
    PowerShell equivalent of `make install` for machines without `make`
    (e.g. Windows). Fetches the Met Office sub-local-authority temperature-
    change projection GeoJSON files.

    NOTE: the URLs are short-lived ArcGIS signed (SAS) links that expire ~1h
    after minting. A 403 means they are stale — regenerate from the ArcGIS
    source and replace the values below (and in the Makefile).

.EXAMPLE
    pwsh ./scripts/data/install-datasets.ps1
#>

$ErrorActionPreference = 'Stop'

# Resolve repo root (two levels up from scripts/data/) so the script works
# regardless of the current working directory.
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot '..\..')
$Dest = Join-Path $RepoRoot 'data\raw'

$Datasets = @(
    @{
        File = 'summer_maximum_temperature_change_projections_sub_local_authority_v1.geojson'
        Url  = 'https://stg-arcgisazurecdataprod.az.arcgis.com/exportfiles-4540-8329/summer_maximum_temperature_change_projections_sub_local_authority_v1_-7528077084752285682.geojson?sv=2025-05-05&st=2026-06-19T03%3A40%3A25Z&se=2026-06-19T04%3A45%3A25Z&sr=c&sp=r&sig=GxO0K8VKyX8sxZ2fUXHJvLsedMLaYlih2PuHzHDAPFc%3D'
    },
    @{
        File = 'winter_average_temperature_change_projections_sub_local_authority_v1.geojson'
        Url  = 'https://stg-arcgisazurecdataprod.az.arcgis.com/exportfiles-4540-8336/winter_average_temperature_change_projections_sub_local_authority_v1_1863846249976887751.geojson?sv=2025-05-05&st=2026-06-19T03%3A38%3A08Z&se=2026-06-19T04%3A43%3A08Z&sr=c&sp=r&sig=QiHKIeSWMuB4xImt9t2%2FV%2BxSSyxqJRsM3WL%2B9BtUrM0%3D'
    }
)

New-Item -ItemType Directory -Force -Path $Dest | Out-Null

foreach ($ds in $Datasets) {
    $out = Join-Path $Dest $ds.File
    Write-Host "Downloading $($ds.File) ..."
    if (Test-Path $out) { Remove-Item $out -Force }
    try {
        Invoke-WebRequest -Uri $ds.Url -OutFile $out -MaximumRedirection 5
        Write-Host "  -> saved to $out"
    }
    catch {
        Write-Warning "  Failed to download $($ds.File): $($_.Exception.Message)"
        Write-Warning "  The signed URL has likely expired (HTTP 403). Refresh it from the ArcGIS source."
    }
}
