# Pedi STAT Data — Captured, Parsed, and Compared to Our App

**Captured:** 2026-07-16 from JSON dumps (Pedi STAT app, QxMD)
**Our app:** 17 sections, ~123 drug rows, dose-verified against UMass 2026-2027
**Pedi STAT:** 24 pedi categories, 9 neonatal categories, 24 adult categories, 754 total drug entries with full dose + volume data

## Files
- `data_pedi.json` — raw Pedi STAT pedi dataset (216 KB)
- `data_neonatal.json` — raw Pedi STAT neonatal dataset (17 KB)
- `data_adult.json` — raw Pedi STAT adult dataset (215 KB) — STAT EM companion
- `flat_drugs_pedi.json` — flattened list of 379 pedi drug entries with dosages
- `flat_drugs_neonatal.json` — flattened list of 8 neonatal drug entries
- `flat_drugs_adult.json` — flattened list of 367 adult drug entries

## Pedi STAT Category Structure (Pedi)

| Category | Subcategories | Items | We have equivalent? |
|---|---|---|---|
| Vital Signs | Vital Signs, Pediatric Assessment Score | 7 | Partial — vitals only, no PAT score |
| Airway Intervention / Intubation | Equipment, Premeds, Induction, Paralytics, Sedation, Vent | 62 | Partial — drugs only, no equipment, no vent settings |
| Agitation | Guidelines, Meds | 23 | Partial — antipsychotics in Tox/Reversal only |
| Anaphylaxis / Allergic Reaction | all | 16 | Yes — Anaphylaxis section |
| Antiemetics | all | 14 | Yes — Antiemetics / GI section |
| Antimicrobials (IV/IM) | All | 16 | Yes — Antibiotics sections |
| Antimicrobials (Oral) | all | 23 | Yes — Antibiotics sections |
| Burns | Burn Size Estimation, Fluid Resuscitation | 3 | **No — gap (Parkland not yet in app)** |
| Cardiac Resuscitation | General, Asystole/PEA, Brady, Tachy, VF/VT | 38 | Yes — Resuscitation + RSI Pretreatment |
| Equipment | All | 22 | **No — gap (no equipment sizing in app)** |
| Fever | All | 4 | Partial — Antipyretics in antibiotics only |
| Fluid/Blood Resuscitation | All | 5 | Partial — IV Fluid Bolus in Resuscitation |
| Glasgow Coma Scale | — | 0 | Yes — GCS modal in tools |
| Hypoglycemia | All | 6 | Yes — Dextrose D10/D25/D50 in Resuscitation |
| Pain Management | All | 15 | Yes — Pain Management section |
| Pressure Support | All | 10 | Partial — Push-Dose Pressors, but no infusions (Dopamine/Dobutamine/Norepi/Milrinone) |
| Procedural Sedation | Procedural, Reversal | 21 | Yes — Procedural Sedation section |
| Respiratory | Croup Score, Croup, Asthma Score, Mild/Mod/Severe Asthma, Bronchiolitis | 39 | Partial — Asthma/Bronchospasm, no asthma severity tiers, no croup dose |
| Seizure / Status Epilepticus | Meds, Algorithm | 13 | Yes — Status Epilepticus section |
| Shock | all | 9 | Partial — covered in Resuscitation, but not as a section |
| Toxicology | Decon, Dextrose, Opiate OD, Acetaminophen OD, Cyanide, Sulfonylurea, Dialyzable, GAP acidosis, Non-GAP acidosis | 37 | Partial — Toxicology/Reversal section has 5 drugs |
| Trauma | All | 10 | **No — gap (no trauma section, no mannitol/3% NaCl/blood)** |
| CODE SHEET | Vitals, Airway, Resus, Seizure, Other, Print | 36 | **No — gap (no exportable code sheet)** |
| EMSC / EIIC | all | 1 | No — not relevant |

## TRUE GAPS — Categories We Don't Have At All

1. **Equipment** (22 items) — ETT size, depth, laryngoscope blade, suction catheter, NG tube, foley, chest tube, central line, IV catheter, BP cuff, Broselow data
2. **Burns** (3 items) — Burn size estimation, fluid resuscitation (Parkland)
3. **Trauma** (10 items) — Hypotension, blood products, IV fluids, hypertonic saline, mannitol
4. **CODE SHEET** (36 items) — Exportable, printable bedside summary
5. **Ventilator Settings** (4 items) — Tidal volume by age
6. **Agitation** (8 drug items) — antipsychotics (Haldol, Droperidol, Olanzapine, Ziprasidone)

## DOSE DISCREPANCIES — Where They Differ From UpToDate / PALS

| Drug | Pedi STAT | UpToDate / PALS 2025 | Our app | Verdict |
|---|---|---|---|---|
| Atropine IV (max) | 1 mg single dose | 0.5 mg single dose | 0.5 mg | Pedi STAT WRONG — their airway page says 1 mg, their cardiac page says 0.5 mg. Internal inconsistency. |
| Midazolam IV induction | 0.1 mg/kg | 0.1-0.2 mg/kg | varies | OK |
| Fentanyl IN | 1.5-2 mcg/kg | 1-2 mcg/kg, then 0.3-0.5 mcg/kg | 1.5 mcg/kg, then 0.3-0.5 mcg/kg | OK |
| Succinylcholine IV | 1.5 mg/kg (2 mg/kg in some sources) | 1-2 mg/kg | TBD | OK |
| Adenosine 1st | 0.1 mg/kg (max 6 mg) | 0.1 mg/kg (max 6 mg) | 0.1 mg/kg | OK |
| Adenosine 2nd | 0.2 mg/kg (max 12 mg) | 0.2 mg/kg (max 12 mg) | 0.2 mg/kg | OK |
| Amiodarone perfusing | 5 mg/kg over 20-60 min | 5 mg/kg over 20-60 min | 5 mg/kg | OK |
| Levetiracetam (status) | 60 mg/kg | 60 mg/kg (ESETT 2019/2020) | 60 mg/kg | OK |
| Calcium Chloride 10% | 20 mg/kg, max 2000 mg | 20 mg/kg, max 1 g child / 2 g adult | 20 mg/kg | OK |
| Calcium Gluconate 10% | 60 mg/kg | 60 mg/kg (3× CaCl) | 60 mg/kg | OK |
| Sodium Bicarb | 1 mEq/kg slow | 1 mEq/kg slow | 1 mEq/kg | OK |
| Acetaminophen IV | 12.5 mg/kg | 15 mg/kg | TBD | **Verify** — older PDR says 12.5; new FDA label says 15 |
| Dexamethasone (croup) | 0.6 mg/kg max 16 mg | 0.6 mg/kg max 16 mg | 0.6 mg/kg | OK |
| Methylprednisolone (asthma) | 1-2 mg/kg max 60 mg | 1-2 mg/kg max 60 mg | 1-2 mg/kg | OK |
| Diphenhydramine (anaphylaxis) | 1-2 mg/kg | 1-2 mg/kg | 1-2 mg/kg | OK |
| Diphenhydramine (antiemetic) | 0.625-1.25 mg/kg | n/a (off-label) | TBD | OK |
| Naloxone (opiate OD) | 0.1 mg/kg IV/IM/ETT or 0.4-2 mg flat, IN 2-4 mg | 0.1 mg/kg IV/IM, IN 2-4 mg | 0.1 mg/kg | OK |
| Hypertonic Saline 3% | 3-5 mL/kg | 3-5 mL/kg | TBD | OK |
| Mannitol | 0.5-1 g/kg | 0.25-1 g/kg | 0.5-1 g/kg | OK |
| Rocuronium RSI | 0.6-1.2 mg/kg (1.2 for RSI) | 1 mg/kg (RSI), 0.6 mg/kg (intubation) | 1 mg/kg | OK |
| Phenobarbital load | 15-20 mg/kg | 15-20 mg/kg | 20 mg/kg | OK |
| Fosphenytoin load | 20 PE/kg | 20 PE/kg | 20 PE/kg | OK |

## NEONATAL DATA (Pedi STAT Neonatal section)

Critical data we don't have:
- **Neonatal Resuscitation Algorithm** (NRP) — 4 steps with HR-driven decision tree
- **Gestational Age Estimates** — weight + ETT + depth + epi dose at each week (23-43 weeks)
- **Umbilical Catheter Sizing** — UAC: (kg×3)+9 cm; UVC: (UAC/2)+1 cm
- **Preductal O2 Saturation Targets** — 60-65% at 1 min, 90-95% at 10 min
- **APGAR Score** (empty in their data — placeholder)
- **Crashing Neonate DDX** — "THE MISFITS" mnemonic (Trauma, Heart, Electrolytes, Metabolic, Inborn errors, Sepsis, Formula, Intestinal, Toxins, Seizures)
- **Neonatal Seizure Algorithm** — Phenobarb 20 mg/kg → repeat 10-20 → Fosphenytoin 20 PE/kg → Levetiracetam 60 mg/kg → Midazolam 0.05-0.1 mg/kg

## ADULT DATA (STAT EM companion — full ED coverage)

24 categories, 367 drug entries. Includes:
- Atrial fibrillation management
- Anticoagulation reversal (Factor Xa, DOAC, heparin, warfarin, anti-platelet)
- Obstetrical emergencies (preeclampsia, eclampsia, PPH)
- Alcohol withdrawal (CIWA-Ar)
- Pressure management (full hypertensive emergency protocols)
- 16 toxicology subcategories (vs our 5)

Not relevant for our pedi app but useful if we ever add an "adult" tab.

## FORMATTING INSIGHTS (How Pedi STAT Displays Things)

From the JSON structure, each drug entry has:
- `formula` — primary dose expression (e.g., "0.02 mg/kg")
- `range1`, `range2` — for range doses with sliders
- `max` — single-dose max
- `volumes[]` — pre-computed volume options at common concentrations (e.g., for Epi 1:10,000: shows mL at 0.1, 0.05, 0.4, 1 mg/mL)
- `segments[]` — slider snap points
- `multipliers[]` — `["kg"]` for weight-based, `["dose"]` for volume-from-dose
- `information[]` — human-readable clinical notes (max, route, frequency, contraindications)
- `steps[]` (algorithm items) — for protocol flows with `title: true/false`

Their volume calc is multi-concentration: instead of just one "give X mL", they show "give X mL if conc is 0.1 mg/mL, Y mL if conc is 0.05 mg/mL, Z mL if conc is 1 mg/mL". This is genuinely useful — covers the case where the pharmacy sends a different concentration than you expected.

## RECOMMENDATIONS (Prioritized)

### Tier 1 — Quick wins (1-2 hours each, high value)
- [ ] Add **Ventilator Settings** section (Tidal Volume by age, 4-6 mL/kg)
- [ ] Add **Croup** drug sub-section (Dexamethasone 0.6 mg/kg, racemic epi 0.5 mL)
- [ ] Add **Asthma severity tiers** (Mild/Mod/Severe) so user picks severity, gets tier-specific doses
- [ ] Add **Agitation meds** (Haldol, Droperidol, Olanzapine) to Tox/Reversal

### Tier 2 — Major additions (half day each)
- [ ] **Neonatal Resuscitation Algorithm** (NRP step-by-step)
- [ ] **Gestational Age Estimates** table (23-43 weeks, weight, ETT, depth, epi)
- [ ] **Equipment section** (22 items: ETT, foley, chest tube, NG, IV, BP cuff by weight/age)
- [ ] **Trauma section** (Hypotension, blood products, hypertonic saline, mannitol, 3% NaCl)
- [ ] **Burn/Parkland** calculator

### Tier 3 — Big builds (multi-day)
- [ ] **CODE SHEET** — print/export view that summarizes everything for one weight
- [ ] **Pediatric Assessment Triangle** tool
- [ ] **Acetaminophen IV** add (and verify 12.5 vs 15 mg/kg with newer FDA label)
- [ ] **Organophosphate** sub-indication on Atropine (per UpToDate)

### Tier 4 — Nice to have
- [ ] **Agitation/Psych** section (currently rolled into Tox)
- [ ] **Multi-concentration volume display** (their nice-to-have pattern)

## NEXT STEPS

1. Pick a Tier 1 item to tackle next (lowest effort, highest user value)
2. For each, write the dose data + add a row in our app
3. Source-verify with UMass / UpToDate / PALS as we go
4. Repeat for each tier
