"""Work-rest-hydration scheduling from WBGT.

Thresholds follow the ACGIH TLV / Action-Limit WBGT screening tables, which give
the allowable proportion of work within each hour by metabolic intensity and
acclimatization state. We map the allowable band to concrete work/rest minutes,
a risk flag, and an hydration target.
"""
from __future__ import annotations

# For each intensity: ordered bands (work_pct, ceiling_wbgt_C).
# A band applies if WBGT <= its ceiling; the first matching band (highest work%)
# wins. ceiling None means the band is not available at that intensity.
# Source: ACGIH TLV (acclimatized) and Action Limit (unacclimatized) WBGT tables.
_TABLE = {
    "acclimatized": {
        "light":      [(100, 31.0), (75, 31.0), (50, 32.0), (25, 32.5)],
        "moderate":   [(100, 28.0), (75, 29.0), (50, 30.0), (25, 31.5)],
        "heavy":      [(100, None), (75, 27.5), (50, 29.0), (25, 30.5)],
        "very_heavy": [(100, None), (75, None), (50, 28.0), (25, 30.0)],
    },
    "unacclimatized": {
        "light":      [(100, 28.0), (75, 28.5), (50, 29.5), (25, 30.0)],
        "moderate":   [(100, 25.0), (75, 26.0), (50, 27.0), (25, 29.0)],
        "heavy":      [(100, None), (75, 24.0), (50, 25.5), (25, 28.0)],
        "very_heavy": [(100, None), (75, None), (50, 24.5), (25, 27.0)],
    },
}

# work_pct -> (work_minutes_per_hour, flag). 0 = cease work.
_BAND = {
    100: (55, "green"),
    75:  (45, "yellow"),
    50:  (30, "amber"),
    25:  (15, "red"),
    0:   (0,  "black"),
}

# Baseline hydration (L/hr) by intensity; bumped by heat. Capped at 1.4 L/hr
# (sustained intake above ~1.5 L/hr risks hyponatremia per OSHA guidance).
_HYDRATION_BASE = {"light": 0.4, "moderate": 0.6, "heavy": 0.8, "very_heavy": 1.0}

INTENSITIES = list(_HYDRATION_BASE.keys())


def _normalize_intensity(intensity: str) -> str:
    key = (intensity or "").strip().lower().replace("-", "_").replace(" ", "_")
    if key in ("veryheavy", "very_heavy"):
        return "very_heavy"
    return key if key in _HYDRATION_BASE else "moderate"


def _work_band(wbgt: float, intensity: str, acclimatized: bool) -> int:
    table = _TABLE["acclimatized" if acclimatized else "unacclimatized"][intensity]
    for work_pct, ceiling in table:
        if ceiling is not None and wbgt <= ceiling:
            return work_pct
    return 0  # above all ceilings -> cease work


def _hydration(intensity: str, wbgt: float) -> float:
    rate = _HYDRATION_BASE[intensity]
    if wbgt >= 28:
        rate += 0.2
    if wbgt >= 30:
        rate += 0.2
    return round(min(rate, 1.4), 2)


def assess(
    *,
    wbgt: float,
    intensity: str = "moderate",
    acclimatized: bool = True,
    wbgt_source: str = "manual",
    weather: dict | None = None,
) -> dict:
    """Build a work-rest-hydration schedule for a given WBGT.

    wbgt        : WBGT in C (measured or estimated).
    intensity   : light | moderate | heavy | very_heavy.
    acclimatized: worker heat-acclimatization state.
    wbgt_source : provenance label ("manual", "estimated_from_weather", ...).
    weather     : optional weather payload echoed back for the UI.
    """
    intensity = _normalize_intensity(intensity)
    wbgt = round(float(wbgt), 1)

    work_pct = _work_band(wbgt, intensity, acclimatized)
    work_min, flag = _BAND[work_pct]
    rest_min = 60 - work_min

    if work_pct == 0:
        rec = "STOP outdoor work — WBGT exceeds the safe limit for this workload."
    elif work_pct == 100:
        rec = "Continuous work permitted; maintain routine hydration and monitoring."
    else:
        rec = (f"Limit work to {work_min} min/hr with {rest_min} min rest in shade; "
               f"enforce hydration breaks.")

    return {
        "wbgt_c": wbgt,
        "wbgt_source": wbgt_source,
        "intensity": intensity,
        "acclimatized": acclimatized,
        "flag": flag,
        "work_pct": work_pct,
        "work_minutes_per_hour": work_min,
        "rest_minutes_per_hour": rest_min,
        "hydration_l_per_hour": _hydration(intensity, wbgt),
        "recommendation": rec,
        "weather": weather,
    }
