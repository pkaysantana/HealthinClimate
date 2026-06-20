# Datasets

Source: HealthinClimate London 2026 hackathon starter
([zachary95/hic-research-repo](https://github.com/zachary95/hic-research-repo),
archived — now [healthinclimateai/london2026-datasets](https://github.com/healthinclimateai/london2026-datasets)).

## Install

Raw datasets download into `data/raw/`.

```bash
# With make (Unix / WSL / Git Bash with make installed)
make install
```

```powershell
# Without make (Windows)
pwsh ./scripts/data/install-datasets.ps1
```

## Datasets

| File | Description |
| --- | --- |
| `summer_maximum_temperature_change_projections_sub_local_authority_v1.geojson` | Met Office summer maximum temperature-change projections, sub-local-authority geography |
| `winter_average_temperature_change_projections_sub_local_authority_v1.geojson` | Met Office winter average temperature-change projections, sub-local-authority geography |

## ⚠️ Expiring URLs

The download URLs are **short-lived ArcGIS signed (SAS) links** with roughly a
one-hour validity window. As of 2026-06-20 the starter's links have **expired**
(HTTP 403) — and the moved-to repo carries the same stale links.

To refresh: regenerate signed export URLs from the ArcGIS source, then update
the URL values in both:

- `Makefile`
- `scripts/data/install-datasets.ps1`

The expanded data sources (4+ additional) live in the moved-to repo above.
