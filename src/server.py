"""HeatGuard API + demo dashboard server.

Run:  uvicorn server:app --reload --port 8000   (from the src/ directory)
      or use scripts/setup/run.ps1
Then open http://localhost:8000

No API key and no Anthropic dependency are required for the core demo.
"""
from __future__ import annotations

import os

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse

from heatguard import assess, estimate_wbgt, get_current_weather, list_sites
from heatguard.schedule import INTENSITIES

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, ".."))
_APP_INDEX = os.path.join(_REPO, "app", "index.html")

app = FastAPI(title="HeatGuard", version="0.1.0")


@app.get("/")
def index():
    return FileResponse(_APP_INDEX)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/sites")
def api_sites():
    return {"sites": list_sites()}


@app.get("/api/assess")
def api_assess(
    mode: str = Query("live", pattern="^(live|manual)$"),
    # live mode
    site: str = "dubai",
    # manual mode (either a direct WBGT, or weather values to estimate from)
    wbgt: float | None = None,
    tdb: float | None = None,
    rh: float | None = None,
    wind: float = 1.0,
    solar: float = 0.0,
    # shared
    intensity: str = "heavy",
    acclimatized: bool = True,
    shade: bool = False,
):
    """Return a work-rest-hydration schedule.

    mode=live   : fetch current weather for `site` from Open-Meteo, estimate WBGT.
    mode=manual : use a measured `wbgt`, or estimate from `tdb`/`rh`/`wind`/`solar`.
    """
    if intensity not in INTENSITIES and intensity not in ("veryheavy", "very heavy"):
        return JSONResponse({"error": f"unknown intensity '{intensity}'",
                             "allowed": INTENSITIES}, status_code=400)

    if mode == "manual":
        if wbgt is not None:
            return assess(wbgt=wbgt, intensity=intensity, acclimatized=acclimatized,
                          wbgt_source="manual")
        if tdb is not None and rh is not None:
            est = estimate_wbgt(tdb, rh, wind, solar, in_shade=shade)
            return assess(wbgt=est, intensity=intensity, acclimatized=acclimatized,
                          wbgt_source="estimated_from_manual_weather",
                          weather={"tdb": tdb, "rh": rh, "wind_ms": wind,
                                   "solar_wm2": solar, "in_shade": shade})
        return JSONResponse(
            {"error": "manual mode needs either 'wbgt' or both 'tdb' and 'rh'"},
            status_code=400,
        )

    # live mode
    try:
        weather = get_current_weather(site)
    except KeyError:
        return JSONResponse({"error": f"unknown site '{site}'"}, status_code=404)

    solar_val = 0.0 if shade else (weather.get("solar_wm2") or 0.0)
    est = estimate_wbgt(weather["tdb"], weather["rh"],
                        weather.get("wind_ms") or 1.0, solar_val, in_shade=shade)
    return assess(wbgt=est, intensity=intensity, acclimatized=acclimatized,
                  wbgt_source=f"estimated_from_weather:{weather['source']}",
                  weather=weather)
