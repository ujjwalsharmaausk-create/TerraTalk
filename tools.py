import json
from pathlib import Path


# -----------------------------
# Cached data loader
# -----------------------------

def load_region(filename: str) -> dict:
    data_path = Path(__file__).resolve().parent / "data" / filename

    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# Cached flood results
# -----------------------------

def flood_assam():
    return load_region("flood_assam.json")


def flood_bihar():
    return load_region("flood_bihar.json")


# -----------------------------
# NDVI / crop-stress functions
# -----------------------------

def ndvi(nir: float, red: float) -> float:
    denominator = nir + red

    if denominator == 0:
        return 0.0

    return round((nir - red) / denominator, 3)


def classify_crop_stress(previous_ndvi: float, current_ndvi: float) -> dict:
    drop = previous_ndvi - current_ndvi

    if drop < 0.10:
        level = "mild"
    elif drop < 0.20:
        level = "moderate"
    else:
        level = "severe"

    return {
        "previous_ndvi": round(previous_ndvi, 3),
        "current_ndvi": round(current_ndvi, 3),
        "ndvi_drop": round(drop, 3),
        "stress": level
    }


def crop_maharashtra():
    return load_region("crop_maharashtra.json")