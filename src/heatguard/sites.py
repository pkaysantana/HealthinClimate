"""Demo site catalog: hot-climate outdoor-work locations with coordinates.

Coordinates are public knowledge; timezone is resolved by Open-Meteo (timezone=auto).
Kept small and hardcoded so the demo has a reliable city dropdown with no geocoding call.
"""
from __future__ import annotations

# id -> (display name, latitude, longitude)
SITES: dict[str, dict] = {
    "dubai":     {"name": "Dubai, UAE",            "lat": 25.20, "lon": 55.27},
    "doha":      {"name": "Doha, Qatar",           "lat": 25.29, "lon": 51.53},
    "riyadh":    {"name": "Riyadh, Saudi Arabia",  "lat": 24.71, "lon": 46.68},
    "kuwait":    {"name": "Kuwait City, Kuwait",   "lat": 29.38, "lon": 47.99},
    "delhi":     {"name": "New Delhi, India",      "lat": 28.61, "lon": 77.21},
    "lagos":     {"name": "Lagos, Nigeria",        "lat": 6.52,  "lon": 3.38},
    "accra":     {"name": "Accra, Ghana",          "lat": 5.60,  "lon": -0.19},
    "phoenix":   {"name": "Phoenix, USA",          "lat": 33.45, "lon": -112.07},
    "singapore": {"name": "Singapore",             "lat": 1.35,  "lon": 103.82},
    "london":    {"name": "London, UK",            "lat": 51.51, "lon": -0.13},
}


def list_sites() -> list[dict]:
    """Return [{id, name, lat, lon}, ...] for the frontend dropdown."""
    return [{"id": k, **v} for k, v in SITES.items()]


def get_site(site_id: str) -> dict:
    """Look up a site by id, raising KeyError if unknown."""
    return SITES[site_id]
