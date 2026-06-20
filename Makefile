# HealthinClimate — dataset install
#
# Adapted from the hackathon starter (github.com/zachary95/hic-research-repo,
# now github.com/healthinclimateai/london2026-datasets). Downloads Met Office
# sub-local-authority temperature-change projections into data/raw/.
#
# NOTE: the URLs below are short-lived ArcGIS signed (SAS) links and EXPIRE
# about an hour after they are minted. If `make install` returns HTTP 403,
# the links are stale — regenerate them from the ArcGIS source and replace the
# values below (and in scripts/data/install-datasets.ps1).

DEST := data/raw

SUMMER_FILE := summer_maximum_temperature_change_projections_sub_local_authority_v1.geojson
WINTER_FILE := winter_average_temperature_change_projections_sub_local_authority_v1.geojson

SUMMER_URL := "https://stg-arcgisazurecdataprod.az.arcgis.com/exportfiles-4540-8329/summer_maximum_temperature_change_projections_sub_local_authority_v1_-7528077084752285682.geojson?sv=2025-05-05&st=2026-06-19T03%3A40%3A25Z&se=2026-06-19T04%3A45%3A25Z&sr=c&sp=r&sig=GxO0K8VKyX8sxZ2fUXHJvLsedMLaYlih2PuHzHDAPFc%3D"
WINTER_URL := "https://stg-arcgisazurecdataprod.az.arcgis.com/exportfiles-4540-8336/winter_average_temperature_change_projections_sub_local_authority_v1_1863846249976887751.geojson?sv=2025-05-05&st=2026-06-19T03%3A38%3A08Z&se=2026-06-19T04%3A43%3A08Z&sr=c&sp=r&sig=QiHKIeSWMuB4xImt9t2%2FV%2BxSSyxqJRsM3WL%2B9BtUrM0%3D"

.PHONY: install

install:
	mkdir -p $(DEST) \
		&& rm -f $(DEST)/$(SUMMER_FILE) \
		&& curl -fL --progress-bar -o $(DEST)/$(SUMMER_FILE) $(SUMMER_URL)
	mkdir -p $(DEST) \
		&& rm -f $(DEST)/$(WINTER_FILE) \
		&& curl -fL --progress-bar -o $(DEST)/$(WINTER_FILE) $(WINTER_URL)
