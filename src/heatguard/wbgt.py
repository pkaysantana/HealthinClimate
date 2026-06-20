"""WBGT estimation from standard weather variables.

We do not have a black-globe / natural-wet-bulb sensor feed, so outdoor WBGT is
ESTIMATED. The manual mode (direct measured WBGT) exists precisely for when a
calibrated reading is available — this module is the best-effort fallback.

Model:
  * Shade (indoor) WBGT via the Australian BoM approximation:
        WBGT = 0.567*Ta + 0.393*e + 3.94
    where e is water-vapour pressure (hPa). This captures temperature + humidity
    with no solar load.
  * A transparent solar adjustment is added when the worker is in direct sun,
    scaled by shortwave radiation and damped by wind. Clamped to keep it sane.

References: Australian Bureau of Meteorology WBGT estimate; Lemke & Kjellstrom
(2012) on outdoor solar adjustment. Treated as an approximation, not a sensor.
"""
from __future__ import annotations

import math


def vapor_pressure_hpa(tdb: float, rh: float) -> float:
    """Water-vapour pressure (hPa) from dry-bulb temp (C) and relative humidity (%)."""
    rh = max(0.0, min(100.0, rh))
    es = 6.105 * math.exp(17.27 * tdb / (237.7 + tdb))  # saturation pressure, hPa
    return (rh / 100.0) * es


def wbgt_shade(tdb: float, rh: float) -> float:
    """Shade / indoor WBGT (no solar load), BoM approximation."""
    e = vapor_pressure_hpa(tdb, rh)
    return 0.567 * tdb + 0.393 * e + 3.94


def solar_adjustment(solar_wm2: float, wind_ms: float) -> float:
    """Extra WBGT (C) from direct solar load, damped by wind. Clamped to [0, 6]."""
    if solar_wm2 <= 0:
        return 0.0
    wind = max(wind_ms, 0.3)  # avoid divide-by-tiny in dead-still air
    adj = (solar_wm2 / 1000.0) * 4.0 / (wind ** 0.3)
    return max(0.0, min(adj, 6.0))


def estimate_wbgt(
    tdb: float,
    rh: float,
    wind_ms: float = 1.0,
    solar_wm2: float = 0.0,
    in_shade: bool = False,
) -> float:
    """Estimate outdoor WBGT (C) from weather. Rounded to 1 decimal."""
    base = wbgt_shade(tdb, rh)
    if not in_shade:
        base += solar_adjustment(solar_wm2, wind_ms)
    return round(base, 1)
