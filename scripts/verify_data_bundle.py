#!/usr/bin/env python3
"""Verify PediRef's bundled JSON payloads against data/*.json."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

FILES = {
    "PEDI": ROOT / "data/data_pedi.json",
    "NEONATAL": ROOT / "data/data_neonatal.json",
    "ADULT": ROOT / "data/data_adult.json",
}


def source_object(path: Path):
    obj = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(obj, dict) and "pedistat" in obj:
        obj = json.loads(obj["pedistat"])
    return obj


def compact_hash(obj):
    raw = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def counts(obj):
    categories = obj.get("categories", [])
    subcategories = sum(len(c.get("subCategories", [])) for c in categories)
    items = sum(
        len(sc.get("items", []))
        for c in categories
        for sc in c.get("subCategories", [])
    )
    dosages = sum(
        len(item.get("dosages", []))
        for c in categories
        for sc in c.get("subCategories", [])
        for item in sc.get("items", [])
    )
    return len(categories), subcategories, items, dosages


for label, path in FILES.items():
    source = source_object(path)
    match = re.search(rf"const DATA_{label} = (\{{.*?\}});\n", HTML, re.S)
    if not match:
        raise SystemExit(f"missing DATA_{label} bundle")
    bundled = json.loads(match.group(1))
    if bundled != source:
        raise SystemExit(f"DATA_{label} does not match {path}")
    c = counts(source)
    print(f"{label}: categories={c[0]} subcategories={c[1]} items={c[2]} dosages={c[3]} hash={compact_hash(source)}")

print("PASS: all bundled JSON objects exactly match data/*.json")
