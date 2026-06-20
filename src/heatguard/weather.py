"""Live weather adapter — Open-Meteo Forecast API (no API key required).

Fallback chain for resilience during a live demo:
    1. Open-Meteo current weather  (source="open-meteo")
    2. Last good cached fetch for this site, data/cached/<site>.json (source="cache")
    3. Bundled offline sample, data/samples/cached_weather.json (source="sample")

Uses only the Python standard library so the core demo needs no extra deps
and no secrets.
"""
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone

API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT_S = 6

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.abspath(os.path.join(_HERE, "..", ".."))
CACHE_DIR = os.path.join(_REPO, "data", "cached")
SAMPLE_FILE = os.path.join(_REPO, "data", "samples", "cached_weather.json")

_CURRENT_VARS = [
    "temperature_2m",
    "relative_humidity_2m",
    "wind_speed_10m",
    "shortwave_radiation",
    "cloud_cover",
    "is_day",
    "apparent_temperature",
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _normalize(current: dict, *, source: str, site: str | None, lat: float, lon: float) -> dict:
    """Map raw Open-Meteo 'current' block to our internal weather schema."""
    return {
        "source": source,
        "site": site,
        "lat": lat,
        "lon": lon,
        "fetched_at": _now_iso(),
        "observed_at": current.get("time"),
        "tdb": current.get("temperature_2m"),
        "rh": current.get("relative_humidity_2m"),
        "wind_ms": current.get("wind_speed_10m"),
        "solar_wm2": current.get("shortwave_radiation", 0.0) or 0.0,
        "cloud_cover": current.get("cloud_cover"),
        "is_day": bool(current.get("is_day", 1)),
        "apparent_temp": current.get("apparent_temperature"),
    }


def fetch_weather(lat: float, lon: float, *, site: str | None = None) -> dict:
    """Fetch current weather from Open-Meteo, falling back to cache then sample."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ",".join(_CURRENT_VARS),
        "wind_speed_unit": "ms",
        "timezone": "auto",
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HeatGuard/0.1"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
        current = raw.get("current") or {}
        if current.get("temperature_2m") is None:
            raise ValueError("Open-Meteo response missing temperature")
        weather = _normalize(current, source="open-meteo", site=site, lat=lat, lon=lon)
        _write_cache(site, weather)
        return weather
    except Exception as exc:  # network down, timeout, bad payload -> degrade gracefully
        fallback = _load_cache(site) or _load_sample(lat, lon, site)
        fallback["fallback_reason"] = f"{type(exc).__name__}: {exc}"
        return fallback


def get_current_weather(site_id: str) -> dict:
    """Convenience: fetch by known site id (see sites.SITES)."""
    from .sites import get_site

    s = get_site(site_id)
    return fetch_weather(s["lat"], s["lon"], site=site_id)


# --- cache / sample helpers -------------------------------------------------

def _write_cache(site: str | None, weather: dict) -> None:
    if not site:
        return
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(os.path.join(CACHE_DIR, f"{site}.json"), "w", encoding="utf-8") as fh:
            json.dump(weather, fh, indent=2)
    except OSError:
        pass  # caching is best-effort; never fail the request over it


def _load_cache(site: str | None) -> dict | None:
    if not site:
        return None
    path = os.path.join(CACHE_DIR, f"{site}.json")
    if not os.path.exists(path):
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        data["source"] = "cache"
        return data
    except (OSError, json.JSONDecodeError):
        return None


def _load_sample(lat: float, lon: float, site: str | None) -> dict:
    try:
        with open(SAMPLE_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        data = {"tdb": 40.0, "rh": 25.0, "wind_ms": 1.5, "solar_wm2": 850.0,
                "cloud_cover": 10, "is_day": True, "apparent_temp": 48.0}
    data.update({"source": "sample", "site": site, "lat": lat, "lon": lon,
                 "fetched_at": _now_iso()})
    return data
