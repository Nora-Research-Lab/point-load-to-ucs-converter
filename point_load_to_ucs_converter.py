"""Plain Python logic for converting point load strength index to UCS."""

import math
from typing import Optional, Tuple

CUSTOM_LABEL = "Custom k factor"

ROCK_TYPE_K = {
    "General (k=24)": 24.0,
    "Low-porosity sandstone (k=20)": 20.0,
    "Limestone/dolomite (k=20)": 20.0,
    "Granite/gneiss (k=25)": 25.0,
    "Basalt/diabase (k=22)": 22.0,
}

ROCK_TYPE_OPTIONS = [*ROCK_TYPE_K, CUSTOM_LABEL]
DEFAULT_ROCK_TYPE = "General (k=24)"


def _to_float(value, name: str) -> float:
    if value is None:
        raise ValueError(f"{name} must be provided.")

    if isinstance(value, bool):
        raise ValueError(f"{name} must be a number.")

    try:
        if isinstance(value, str):
            cleaned = value.strip().replace(",", ".")
            if not cleaned:
                raise ValueError(f"{name} must be a number.")
            return float(cleaned)
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a number.")


def _is_finite_number(value) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)


def get_k_factor(rock_type: str, custom_k: Optional[float] = None) -> float:
    if rock_type == CUSTOM_LABEL:
        k = _to_float(custom_k, "Custom k factor")
        if not _is_finite_number(k) or k < 15.0 or k > 30.0:
            raise ValueError("Custom k factor must be between 15 and 30.")
        return float(k)

    if rock_type not in ROCK_TYPE_K:
        raise ValueError("Select a valid rock type.")

    return float(ROCK_TYPE_K[rock_type])


def classify_ucs(ucs: float) -> str:
    if not _is_finite_number(ucs):
        raise ValueError("UCS must be finite.")

    if ucs < 1.0:
        return "Extremely weak"
    if ucs < 5.0:
        return "Very weak"
    if ucs < 25.0:
        return "Weak"
    if ucs < 50.0:
        return "Medium strong"
    if ucs < 100.0:
        return "Strong"
    if ucs < 250.0:
        return "Very strong"
    return "Extremely strong"


def compute_point_load_to_ucs(
    is50,
    rock_type: str,
    custom_k: Optional[float] = None,
) -> Tuple[bool, str]:
    try:
        value = _to_float(is50, "Point load index")
        if not math.isfinite(value) or value <= 0.0:
            raise ValueError("Point load index must be a finite number greater than 0.")

        k = get_k_factor(rock_type, custom_k)
        ucs = k * value
        classification = classify_ucs(ucs)

        return True, f"UCS = {ucs:.2f} MPa – Classification: {classification}"

    except ValueError as exc:
        return False, f"Error: {exc}"
