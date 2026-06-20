"""HeatGuard — heat-stress work-rest-hydration scheduler.

Public surface:
    assess(...)        -> full schedule from WBGT or weather inputs
    estimate_wbgt(...) -> outdoor WBGT estimate from weather
    get_current_weather(site) / fetch_weather(lat, lon)
    SITES              -> catalog of demo cities/sites
"""
from .wbgt import estimate_wbgt, wbgt_shade, vapor_pressure_hpa
from .schedule import assess
from .weather import fetch_weather, get_current_weather
from .sites import SITES, list_sites, get_site

__all__ = [
    "assess",
    "estimate_wbgt",
    "wbgt_shade",
    "vapor_pressure_hpa",
    "fetch_weather",
    "get_current_weather",
    "SITES",
    "list_sites",
    "get_site",
]
