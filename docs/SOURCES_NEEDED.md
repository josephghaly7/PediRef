# PediRef — values and rules not derivable from the bundled JSON

PediRef v9.1 renders the three source JSON files verbatim and adds a JSON-aware weight-threshold resolver for entries that have structured `vals` (kg lower-bound pairs) or `information[]` prose with weight bands. Anything that requires a clinical decision the JSON does not encode is listed here so a verified source can be added.

## Threshold tables interpreted from JSON

These rows are picked directly from the JSON's own `vals` kg cutoff pairs (or `information[]` prose). No external source is required for the matching itself; only the source numbers are JSON-as-supplied.

| Group | Item | Source in JSON |
|---|---|---|
| Peds | Cuffed ETT, Uncuffed ETT, Laryngoscope Blade, Glidescope VL, LMA, I-gel, King LTS, O2 Mask, Oral Airway, NP Airway, BVM, Vital Signs (HR, RR, SBP) | `vals` strings in the JSON |
| Adult | King LTS | `vals` in JSON |
| Adult | LMA, I-gel, ETT (women/men prose) | `information[]` prose patterns |

## Values that need a verified source

| Value | Where used | Notes |
|---|---|---|
| Broselow-Luten kg cutoffs for the Peds `vals` rows (e.g. cuffed ETT `0.899→2.5 mm`, `1.099→2.5–3.0 mm`, ...) | Peds Airway Equipment | PALS / Broselow-Luten tape official table |
| Adult LMA/I-gel/ETT sizes (Women 7.0–7.5 mm ID, Men 7.5–8.5 mm ID; Size 3 for 30–60 kg, Size 4 for 60–80 kg, Size 5 for >80 kg) | Adult Airway Equipment | ASA / Difficult Airway Society adult guidelines |
| Peds vital sign kg cutoffs (HR, RR, SBP) | Peds Vital Signs | PALS 2025 vital signs reference |
| Adult vital sign normal range (HR 60–100, RR 12–18, SBP 120) | Adult Vital Signs | UpToDate / AHA adult normal values |
| Hypotension thresholds (SBP < 70 + 2·age; SBP < 60 infants; SBP < 70 toddlers) | Peds Vital Signs → Hypotension | PALS 2025 |
| MAP normal ranges (40–55 mmHg at 1mo, 50–70 mmHg at 1–2y, 55–75 mmHg at 5–10y) | Peds Vital Signs → MAP | PALS 2025 |
| Temperature reference values (rectal 36.6–38°C, tympanic 35.8–38°C, oral 35.5–37.5°C, axillary 36.5–37.5°C) | Vital Signs → Temperature | AAP / standard pediatric temperature reference |
| ETT depth calculation (Adult: 21 cm women, 23 cm men; Peds: per Broselow-Luten row) | ETT Depth | ASA / PALS 2025 |
| SpO2 target by minute after birth (1 min 60–65%, 2 min 65–70%, 3 min 70–75%, 4 min 75–80%, 5 min 80–85%, 10 min 90–95%) | Neonate Oxygen Saturation | NRP 2025 |
| Devine IBW formula (Adult) | Adult IBW | Devine 1974 / standard references |
| Pediatric maintenance fluid 4-2-1 rule (4 mL/kg for first 10 kg + 2 mL/kg for next 10 kg + 1 mL/kg thereafter) | Peds Fluid/Blood Resuscitation | Standard pediatric maintenance fluid reference |
| Parkland burn formula constants (4 mL × kg × %TBSA) | Burns | ABA / ATLS Parkland |
| Ideal body weight switch-over (Peds → Adults at 43 kg or 40 kg) | Patients ≥43 kg | PALS 2025 (Peds max 40 kg) vs PediaSIM-style (43 kg) |
| Selection rule for an entry that has both a weight-based dosage AND a fixed-dose alternative (e.g. adult Fentanyl IV/IO/IN) | Adult Fentanyl IV/IO/IN, Lorazepam, Midazolam, Hydromorphone, Ketamine | Institutional convention / PALS |

## STAT EM data discrepancies (open — Jul 23 2026)

Greg confirmed on 2026-07-23 that PediRef's `data_pedi.json` was taken from STAT EM, so values should be identical. STAT EM screenshots at 6 kg disagree on three vitals:

| Vital | STAT EM value (6 kg) | PediRef JSON row covering 6 kg | JSON value | Difference |
|---|---|---|---|---|
| Heart Rate | 100-190 bpm | `4,100-205 bpm` (band 4–10.999) | 100-205 bpm | STAT EM upper bound is 15 lower than JSON |
| Respiratory Rate | 30-53 rpm | none (first band starts at 11) | unranked at 6 kg | STAT EM shows the next-band-up value; JSON has no sub-11 row |
| Systolic BP | 72-104 mmHg | `5,67-84 mmHg` (band 5–10.999) | 67-84 mmHg | STAT EM lower bound is 5 higher, upper bound 20 higher |

Three hypotheses (need Greg to disambiguate by sending more STAT EM screenshots at other weights):

1. **STAT EM uses a different JSON version.** Their current app may have a JSON that drops the `4-11` and `5-11` rows entirely. Compare their values at 6 kg, 13 kg, 25 kg, 60 kg against ours to determine whether the disagreements are systematic (same offset) or specific to sub-11 kg children.
2. **STAT EM has a "Pediatric" vs "Infant" tab** the screenshot did not reveal. The `4-11` / `5-11` rows in our JSON may belong to an Infant table STAT EM doesn't show on the same screen.
3. **Our `4-11` / `5-11` rows were added later from a PALS card, not from STAT EM.** The `100-205` HR upper bound is higher than typical PALS newborn HR max (180), suggesting the row may have been mis-keyed.

**Do NOT change `data/data_pedi.json` until Greg confirms which hypothesis is correct.** Awaiting follow-up screenshots.

### Resolved
- **2026-07-23:** Greg confirmed PediRef must match STAT EM, the industry standard. The data files are byte-for-byte identical (verified 2026-07-23 by walking both JSONs recursively — 0 differences across all 24 categories). The mismatch was the picker logic in `pickThreshold()`: PediRef used "largest lo ≤ weight" (mathematically correct: the row whose range covers the weight), STAT EM uses "smallest lo ≥ weight" (round up to the next band). Picker rule changed to STAT EM's in `index.html` function `pickThreshold()` — see commit pushing with this update. JSON files were not modified; the discrepancy was entirely in the picker, not in the data. Title bumped to v10.1 "STAT EM Picker Rule", sw.js cache bumped to pediref-v15_19.

## Items where the JSON encodes a marker but no source-backed meaning

| Marker | Where | Meaning we infer |
|---|---|---|
| `ibw: true` | Adult induction / sedation / analgesia drugs | "Use Ideal Body Weight, not entered weight." This is read from UpToDate; needs institutional confirmation. |
| `multipliers: []` (empty) | Adult fixed-dose entries | "This is a fixed dose, not per-kg." Inferred from JSON convention. |

## Items we explicitly did NOT add

- Push-dose pressors in adult (per PediRef rule, removed in v8; literature supports infusion only).
- Any text Greg did not approve.

## How to add a new value

1. Add the value to `data/*.json` (canonical source).
2. Run `python3 scripts/verify_data_bundle.py` to confirm the bundle matches.
3. Reload the page. The new entry appears with no extra work.
4. If the entry needs a new derivation rule (e.g. an age-based formula, IBW-based formula), add it to `renderItem` or `calculatedDose` in `index.html` and document it here.

## Items Greg needs to source

The threshold row "selected" pick and the per-kg × weight dose math are derived **purely from the JSON**. They are not cross-referenced to a clinical reference yet. Before relying on the displayed number for clinical use, Greg needs to confirm the JSON's `vals` and `information[]` values match a published reference (e.g. PALS 2025, Broselow-Luten, NRP 2025, ASA adult airway). Anything Greg finds that disagrees with the JSON should be added to this file with the citation, then propagated into `data/*.json`.