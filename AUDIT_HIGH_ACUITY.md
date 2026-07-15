# AUDIT REPORT — PediRef v4 — HIGH-ACUITY Peds ED Medications
**File audited:** `/home/ubuntu/pedi-stat/index.html` (lines 418–488)
**Auditor:** Hermes subagent (delegated task)
**Date of audit:** July 14, 2026
**Scope:** RSI — Pretreatment, RSI — Induction, RSI — Paralysis, RSI — Post-Intubation Sedation, Resuscitation, Anaphylaxis, Status Epilepticus, Procedural Sedation, Push-Dose Pressors
**Out of scope:** Asthma/Pain/Antiemetics/Antibiotics, algorithm cards below the MEDS array.

---

## METHODOLOGY
- Read `index.html` lines 418–488 in full (the MEDS array entries in scope).
- Verified each entry against AHA PALS 2025 published algorithms (Lasa et al. 2025, AHA Part 8; AHA PALS Cardiac Arrest Algorithm 250123; AHA PALS Bradycardia Algorithm 250121; AHA PALS Tachycardia Algorithm 250117), Harriet Lane Handbook 22nd ed., Lexicomp pediatric drug information, AAP policy statements / Pediatric Care Online, FDA-approved labeling (Diastat, fosphenytoin Pfizer label, famotidine 2025 label, fentanyl citrate label, etomidate Amidate label), and Broselow 2019 tape ranges.
- For each entry I checked: per-kg dose (low & high), route list completeness, max dose, min dose, concentration, and any prep math (push-dose).
- Where a "PALS 2025" or "Harriet Lane 22e" claim could not be triangulated to a primary source, I labeled it **UNCERTAIN** rather than inventing a citation.

---

## PER-ENTRY FINDINGS

### RSI — Pretreatment

**1. Atropine — Bradycardia / <1 yr (line 420)**
- Current: `0.01–0.02 mg/kg IV/IO, 0.1 mg/ml conc`, note says "no minimum dose for pretreatment"
- ⚠️ **Note text contradicts the 2025 PALS Bradycardia Algorithm.** The published 2025 algorithm (cpr.heart.org PALS Bradycardia 250121 long description) states: *"Atropine IV/IO dose: 0.02 mg/kg. May repeat once. Minimum dose 0.1 mg and maximum single dose 0.5 mg."* The "no minimum" line in the note is INCORRECT for the bradycardia indication. The 0.1 mg minimum only applies to the bradycardia setting, not to pretreatment per se, but the comment as written is misleading.
- **Source:** AHA PALS Bradycardia With a Pulse Algorithm 2025 (cpr.heart.org/-/media/CPR-Files/.../Algorithm-PALS-Bradycardia-250121.pdf)
- **Patched note (recommend):** change to: *"Per 2025 AHA PALS: 0.02 mg/kg IV/IO. Minimum 0.1 mg, maximum single dose 0.5 mg. May repeat once."*

**2. Lidocaine — ↑ICP (line 421)**
- Current: `1–1.5 mg/kg IV/IO, 20 mg/ml (2%), max 100 mg, give 2–3 min before laryngoscopy`
- ✅ **Correct.** 1.5 mg/kg (max 100 mg) IV 2–3 min pre-laryngoscopy is the pediatric pretreatment dose for ICP blunting.
- **Source:** UNC PED RSI Checklist 2025; Clinician.com 2024 pediatric RSI review; standard EM pharmacology.

**3. Fentanyl — Blunt sympathetic (line 422)**
- Current: `1–3 mcg/kg IV/IO, 50 mcg/ml, max 100 mcg, give over 1–2 min`
- ✅ **Correct.** Fentanyl 2–3 mcg/kg IV given ≥1 min before laryngoscopy is standard. Range 1–3 mcg/kg is acceptable (lower end with hypotension or with opioid-tolerant patients).
- **Source:** wikEM RSI; UNC PED RSI Checklist; FDA fentanyl citrate label (children 2–12 yr: 2–3 mcg/kg).

---

### RSI — Induction

**4. Etomidate (line 425)**
- Current: `0.3 mg/kg IV/IO, 2 mg/ml, max 20 mg, "Adrenal suppression — avoid in sepsis"`
- ✅ **Dose correct.** Etomidate 0.2–0.3 mg/kg IV (max 20 mg) over 30–60 sec is standard for pediatric RSI.
- **Source:** AAP Pediatric Care Online Etomidate monograph; FDA Amidate (etomidate) label; wikEM RSI.
- ⚠️ **"Avoid in sepsis" note:** the literature is mixed. A 2025 retrospective (Mendez et al., PMC11945125) did not find increased adrenal insufficiency in children given single-dose etomidate in the ED. PEM Playbook consensus still favors **ketamine** in sepsis. The current note is *directionally correct* per current PEM practice but is stronger than the data supports. Could soften to: *"Adrenal suppression risk (single dose, 4–8 h) — prefer ketamine in sepsis."* — **Minor/stylistic, not a CRITICAL ERROR.**

**5. Ketamine (line 426)**
- Current: `1–2 mg/kg IV/IO, 50 or 100 mg/ml, "1 mg/kg for hypotension; 2 mg/kg for full dissociation"`
- ✅ **Dose correct.** IV 1–2 mg/kg is the RSI induction dose; analgesia sub-dissociative is 0.1–0.3 mg/kg (not in this entry, only in Procedural Sedation section).
- **Source:** AAP; Green et al. 2011 Ann Emerg Med; Lexicomp.

**6. Propofol (line 427)**
- Current: `2–3 mg/kg IV/IO, 10 mg/ml, "Avoid if hypotensive (SBP < 70+2×age)"`
- ✅ **Dose correct** for induction. The BP threshold is the standard pediatric hypotension formula. (Note: 70+2×age is the *systolic* BP 5th percentile formula, which is correct.)
- **Source:** Lexicomp; AAP.

**7. Midazolam — "Rarely used alone" (line 428)**
- Current: `0.1–0.3 mg/kg IV/IO, 5 mg/ml, max 5 mg`
- ✅ **Dose correct** (0.1–0.3 mg/kg RSI; max 10 mg per some sources, 5 mg per others; 5 mg is a safe conservative cap).
- **Source:** Sagarin 2003; UNC PED RSI chart; wikEM.

---

### RSI — Paralysis

**8. Succinylcholine (line 431)**
- Current: `1–2 mg/kg IV/IO, 20 mg/ml, max 150 mg, note: "<20 kg: use 2 mg/kg. >20 kg: 1 mg/kg"`
- ✅ **Dose correct.** This is the standard pediatric split (infants/young children 2 mg/kg, older children/adolescents 1 mg/kg).
- **Source:** FDA Anectine/succinylcholine label; Lasa 2025 PALS; clinician.com 2024 pediatric RSI review.

**9. Rocuronium (line 432)**
- Current: `0.6–1.2 mg/kg IV/IO, 10 mg/ml, max 100 mg, "RSI: 1–1.2 mg/kg. Standard: 0.6 mg/kg"`
- ✅ **Dose correct.** 1.0–1.2 mg/kg for RSI (PEM Playbook, wikEM, 2024 pediatric RSI review); 0.6 mg/kg for maintenance/repeat paralysis. Max 100 mg reasonable.
- **Source:** wikEM RSI; PEM Playbook; AAP.

**10. Vecuronium (line 433)**
- Current: `0.1–0.15 mg/kg IV/IO, 1 mg/ml, max 10 mg, "RSI: 0.15 mg/kg. Standard: 0.1 mg/kg"`
- ✅ **Dose correct** (0.1 mg/kg standard, 0.15 mg/kg priming/RSI, sometimes up to 0.2–0.3 mg/kg for RSI). Slower onset than roc — correct caveat.
- **Source:** AAP Pediatric Care Online Vecuronium; wikEM.

---

### RSI — Post-Intubation Sedation

**11. Fentanyl — Analgesia (line 436)**
- Current: `0.5–2 mcg/kg IV, 50 mcg/ml, "Bolus, then 1–5 mcg/kg/hr infusion"`
- ✅ **Dose and infusion range correct** (most pediatric pathways use fentanyl 1–5 mcg/kg/hr, max 5 mcg/kg/hr per some; bolus 0.5–2 mcg/kg).
- **Source:** CHOC CVICU protocol; CHR PICU; UNC PED Post-RSI Sedation pathway.

**12. Morphine — Analgesia (line 437)**
- Current: `0.05–0.1 mg/kg IV, 2 mg/ml, max 4 mg, "q2-4h bolus"`
- ✅ **Dose correct.** 0.05–0.1 mg/kg IV q2–4h, max 4 mg/dose is the standard pediatric post-intubation intermittent dose. Continuous infusion 0.01–0.06 mg/kg/hr also reasonable.
- **Source:** Lexicomp; AAP.

**13. Midazolam — Sedation (line 438)**
- Current: `0.05–0.15 mg/kg IV, 5 mg/ml, max 2 mg, "Bolus, then 0.05–0.4 mg/kg/hr infusion"`
- ⚠️ **Max of 2 mg/dose is low.** The 2010 PALS/IWK guidelines and most pediatric ICU protocols use **max 0.4 mg/kg total dose OR 10 mg total dose**. 2 mg is too restrictive for older children. A 30 kg child would be capped at 2 mg, far below the standard bolus/infusion ceiling.
- **Source:** IWK Midazolam pediatric guidelines 2019; Stanford status epilepticus pathway; FDA CIV midazolam label (initial infusion 1–2 mcg/kg/min = 0.06–0.12 mg/kg/hr).
- **Suggested fix:** change max from 2 mg → 10 mg (consistent with the Status Epilepticus midazolam max on line 473). Recommended patch: `mx:10, mu:'mg'` (matching the 10 mg ceiling used everywhere else).

**14. Lorazepam — Sedation (line 439)**
- Current: `0.05–0.1 mg/kg IV, 2 mg/ml, max 2 mg, "q4-6h bolus"`
- ⚠️ **Max of 2 mg may be restrictive for adolescents.** Most PICU protocols allow 0.05–0.1 mg/kg IV q4–6h with a max of **4 mg/dose** (same ceiling as status). For a 50 kg adolescent, 0.1 mg/kg = 5 mg — capped at 2 mg would be underdose.
- **Source:** CHR PICU; Lexicomp; Stanford pediatric status epilepticus pathway.
- **Suggested fix:** change max from 2 mg → 4 mg to align with the Status Epilepticus entry (line 472) and adult/older child range. Patch: `mx:4, mu:'mg'`.

**15. Propofol — Sedation infusion (line 440)**
- Current: `0.5–4 mg/kg/hr IV, 10 mg/ml, "Start low, titrate. Avoid bolus in peds. Watch for PRIS"`
- ✅ **Range correct.** Standard pediatric ICU propofol sedation is 0.5–4 mg/kg/hr (5–66 mcg/kg/min), with a hard ceiling of 4 mg/kg/hr (~67 mcg/kg/min) to mitigate PRIS. Avoid bolus in peds is the standard.
- **Source:** UNC PICU Propofol Continuous Infusion Guideline 2017; Cureus 2024 safety review.

**16. Dexmedetomidine — Sedation infusion (line 441)**
- Current: `0.2–1 mcg/kg/hr IV, 4 mcg/ml, "May load 0.5–2 mcg/kg over 10 min"`
- ✅ **Range correct.** Loading 0.5–1 mcg/kg over 10 min, infusion 0.2–1.5 mcg/kg/hr is standard. Bradycardia risk noted correctly. Max 1.5 mcg/kg/hr is the typical PICU ceiling.
- **Source:** PEM Morsels dexmedetomidine for PED sedation; FDA Precedex label; Tobias 2007.

**17. Ketamine — Sedation/analgesia (line 442)**
- Current: `0.5–2 mg/kg/hr IV, 100 mg/ml, "Infusion. Bronchodilator. Emergence phenomena"`
- ⚠️ **Range is on the low end.** The standard ketamine sedation infusion is **0.5–3 mg/kg/hr** (some references 1–3 mg/kg/hr; 0.5 mg/kg/hr is acceptable as a starting rate). 2 mg/kg/hr as the upper limit is conservative but not wrong.
- **Source:** Lexicomp; AAP.
- **Verdict:** ✅ acceptable but conservative; could consider extending `hi` to 3. — **Minor/optional.**

---

### Resuscitation

**18. Epinephrine — Cardiac arrest (line 445)**
- Current: `0.01 mg/kg IV/IO, 1:10,000 (0.1 mg/ml), max 1 mg, "Repeat q3-5 min. No maximum in arrest"`
- ⚠️ **Contradictory: max 1 mg is set AND "No maximum in arrest" in the note.** The PALS 2025 algorithm lists max 1 mg/dose (which is reasonable to cap the calculator), but the note text says "no maximum in arrest" which contradicts the displayed max. Note "No maximum in arrest" actually refers to total cumulative dose (not a per-dose ceiling) and is misleading as written.
- **Source:** AHA PALS Cardiac Arrest Algorithm 250123: "0.01 mg/kg (0.1 mg/mL concentration). Max dose 1 mg."
- **Suggested fix:** Remove "No maximum in arrest" from the note. Replace with: *"Repeat q3-5 min. Per-dose max 1 mg; no cumulative-dose cap."* Or just delete the sentence.

**19. Epinephrine — Cardiac arrest (ET) (line 446)**
- Current: `0.05–0.1 mg/kg ET, 1:1,000 (1 mg/ml), max 10 mg, "Dilute in 3-5 ml NS. IV/IO strongly preferred over ET"`
- ⚠️ **Dose is correct** (0.1 mg/kg ET is the PALS dose = 0.1 mL/kg of 1:1,000) but the **lo range 0.05 mg/kg is outdated.** PALS 2025/2020 lists ET dose at 0.1 mg/kg (10× the IV dose) and AHA Part 8 (2025) explicitly states "IV or IO administration of epinephrine is preferred over endotracheal administration when possible."
- **Source:** AHA PALS Cardiac Arrest Algorithm; Lasa et al. 2025 Part 8 PALS (publications.aap.org pediatrics 157/1 e2025074351).
- **Suggested fix:** change `lo:.05` → `lo:.1` (i.e., 0.1 mg/kg, single value). Note already correctly states IV/IO preferred, but consider adding: *"ET route is a last resort if no IV/IO access — PALS 2025 de-emphasizes ET."*

**20. Amiodarone — VF/pVT (line 447)**
- Current: `5 mg/kg IV/IO, 50 mg/ml, max 300 mg, "Max 300 mg 1st dose, 150 mg 2nd. For shock-refractory"`
- ✅ **Correct.** Amiodarone 5 mg/kg bolus (max 300 mg first dose, 150 mg subsequent) per PALS 2025.
- **Source:** AHA PALS Cardiac Arrest Algorithm 250123: "5 mg/kg bolus (max 300 mg). May repeat up to 3 doses (max 150 mg subsequent doses)."

**21. Lidocaine — VF/pVT (line 448)**
- Current: `1 mg/kg IV/IO, 20 mg/ml (2%), max 100 mg, "Alternative to amiodarone for VF/pVT"`
- ✅ **Correct.** Lidocaine 1 mg/kg loading dose; max 3 mg/kg cumulative per arrest per most references. 100 mg is a reasonable per-dose ceiling.
- **Source:** AHA PALS Cardiac Arrest Algorithm 250123; FDA lidocaine label; Medscape.

**22. Adenosine (1st) — SVT (line 449)**
- Current: `0.1 mg/kg IV, 3 mg/ml, max 6 mg, "RAPID push (1-2 sec) followed by immediate flush. Proximal IV preferred"`
- ✅ **Correct.** AHA PALS Tachycardia Algorithm 250117: "0.1 mg/kg (max 6 mg) rapid push followed by IV flush."
- **Source:** cpr.heart.org PALS Tachyarrhythmia 250117; CHOP/PEMMorsels; ACLS drugs adenosine.

**23. Adenosine (2nd) — SVT (line 450)**
- Current: `0.2 mg/kg IV, 3 mg/ml, max 12 mg, "Double the 1st dose. RAPID push + flush"`
- ✅ **Correct.** "Consider repeat dose 0.2 mg/kg rapid push followed by IV flush; maximum dose 12 mg."
- **Source:** Same as 22.

**24. Atropine — Symptomatic brady (line 451)**
- Current: `0.02 mg/kg IV/IO, 0.1 mg/ml, min 0.1 mg, max 0.5 mg, "Min 0.1 mg. Max 0.5 mg (<40 kg), 1 mg (>40 kg)"`
- ⚠️ **Contradictory: the entry has mx=.5, but the note says "1 mg (>40 kg)"** — the entry's max is 0.5 mg but the note allows 1 mg for kids >40 kg. PALS Bradycardia Algorithm 2025: "Maximum single dose 0.5 mg" (no weight break).
- **Source:** AHA PALS Bradycardia Algorithm 250121.
- **Suggested fix:** Either remove the "(<40 kg)/1 mg (>40 kg)" from the note (PALS just says max 0.5 mg single dose) OR add a separate entry for the "max 1 mg" convention. Easiest: change note to: *"Min 0.1 mg. Max single dose 0.5 mg. Higher doses may be used in organophosphate poisoning."* (the >40 kg/1 mg convention is from 2010 PALS and has been removed in 2020+).

**25. Atropine — Brady (ET) (line 452)**
- Current: `0.03–0.04 mg/kg ET, 0.4 mg/ml, "If no IV/IO access"`
- ⚠️ **Dose range is wrong.** PALS lists atropine ET at **0.04–0.06 mg/kg** (Kleinman 2010 PALS Part 14; PedSanesthesia endotracheal drug table).
- **Source:** Part 14: Pediatric Advanced Life Support 2010, Circulation; pedsanesthesia.org endotracheal medication administration.
- **Suggested fix:** change `lo:.03, hi:.04` → `lo:.04, hi:.06`. (Also consider concentration 0.4 mg/ml is correct for atropine injectable 0.4 mg/mL, so conc is OK.)

**26. Naloxone — Opioid reversal (line 453)**
- Current: `0.01–0.1 mg/kg IV/IO/IM/IN, 0.4 mg/ml, max 2 mg, "Titrate to respiratory drive. Lower end for chronic opioid"`
- ⚠️ **Concentration should typically be 0.4 mg/mL OR 1 mg/mL.** 0.4 mg/mL is fine (Narcan 0.4 mg/mL). The dose range 0.01–0.1 mg/kg is broad — most current pediatric guidelines use **0.1 mg/kg IV/IM/IN for full reversal** (max 2 mg) and **0.01–0.05 mg/kg for chronic-opioid partial reversal**. The lo of 0.01 mg/kg with hi of 0.1 mg/kg in a single entry is a hybrid that may be confusing. Not dangerous but suboptimal.
- **Source:** wikEM naloxone; pedmed.org; Sandelich 2024 PMC10920943.
- **Suggested fix:** consider splitting or clarifying: change note to: *"0.1 mg/kg for full reversal. 0.01–0.05 mg/kg for chronic-opioid partial reversal to avoid withdrawal."*

**27. Calcium Chloride — HyperK⁺/CCB OD (line 454)**
- Current: `20 mg/kg IV/IO, 100 mg/ml (10%), max 1000 mg, "Give slowly. Central line preferred"`
- ✅ **Correct.** 20 mg/kg (0.2 mL/kg of 10% solution) slow IV push, max 1 g/dose, central line preferred.
- **Source:** AHA PALS; AAP Pediatric Care Online Calcium Chloride; pemportal hyperkalemia management.

**28. Magnesium Sulfate — Torsades/asthma (line 455)**
- Current: `25–50 mg/kg IV/IO, 500 mg/ml (50%), max 2000 mg, "25 mg/kg for asthma, 50 mg/kg for torsades"`
- ✅ **Correct.** 25–50 mg/kg (max 2 g) IV over 20 min, both for asthma and torsades de pointes; 50 mg/kg is typical for torsades per PECARN and most pediatric pathways.
- **Source:** IWK pediatric drug dosing; AAP Pediatric Care Online; PECARN 2024; medscape MgSO4 dosing.

**29. Sodium Bicarbonate — Prolonged arrest (line 456)**
- Current: `1 mEq/kg IV/IO, 1 mEq/ml (8.4%), max 50 mEq, "<3 mo: use 4.2% solution. For hyperK⁺, TCA OD, prolonged arrest"`
- ✅ **Dose correct** (1 mEq/kg standard) and **4.2% solution in <3 months** is correct. Max 50 mEq is the standard pediatric cap.
- **Source:** StatPearls Sodium Bicarbonate; PALS; FDA sodium bicarbonate label (medsafe NZ datasheet).
- ⚠️ Note: 2010+ PALS no longer routinely recommends bicarb in arrest except for hyperK, TCA OD, or prolonged arrest — current note is appropriately narrow.

**30. Dextrose (D10W) — Hypoglycemia (line 457)**
- Current: `5–10 ml/kg IV/IO, D10W (100 mg/ml), "0.5–1 g/kg. For documented hypoglycemia. PALS: 5–10 mL/kg of D10W"`
- ⚠️ **The "5–10 mL/kg" range is for D10, but the standard 5/2/1 rule (PEM Cincinnati, wikEM) gives:**
  - **Neonates/infants <2 mo:** D10W 2.5–5 mL/kg (not 5–10)
  - **2 mo–8 yr:** D25W 2 mL/kg
  - **>8 yr/adolescent:** D50W 1 mL/kg
  - The 5–10 mL/kg D10 range is the AAP "neonatal" range; for older infants (>2 mo), most pediatric EM practice uses 2 mL/kg of D25W or 5 mL/kg of D10W — both delivering 0.5 g/kg dextrose.
- **Source:** PALS PECC; wikEM Dextrose-based products; 5/2/1 rule (PEMCincinnati 2021).
- **Suggested fix:** change note to: *"0.5–1 g/kg. Neonates/infants <2 mo: D10W 5–10 mL/kg. Older infants/children: D25W 2 mL/kg or D10W 5 mL/kg (≈0.5 g/kg). >8 yr: D50W 1 mL/kg."*

**31. Dextrose (D25W) — Hypoglycemia (>2yr) (line 458)**
- Current: `2–4 ml/kg IV/IO, D25W (250 mg/ml), "0.5–1 g/kg. When volume matters. >2 yr or >10 kg"`
- ✅ **Dose correct.** D25W 2 mL/kg = 0.5 g/kg (standard 5/2/1 rule). Some references allow 4 mL/kg = 1 g/kg for severe hypoglycemia. The threshold of ">2 yr or >10 kg" is the **5/2/1 rule's cutoff for D25** (per PALS PECC and wikEM). 
- **Source:** 5/2/1 rule; PALS PECC; MaMimonidesEM 2025; wikEM Dextrose products.
- ✅ **Verdict: correct**, but see #30 above for the PALS threshold callout.

---

### Anaphylaxis

**32. Epinephrine — 1st line IM (line 461)**
- Current: `0.01 mg/kg IM, 1:1,000 (1 mg/ml), max 0.5 mg, "Max 0.3 mg (<30 kg), 0.5 mg (≥30 kg). Anterolateral thigh. Repeat q5-15 min"`
- ⚠️ **Conflict between `mx:.5` and the note's "0.3 mg (<30 kg), 0.5 mg (≥30 kg)".** The entry shows `mx:.5` but the note splits it. AAP/WAO 2017 (and AAP 2024) recommend:
  - <7.5 kg: 0.01 mg/kg
  - 7.5–15 kg: 0.1 mg
  - 15–30 kg: 0.15 mg
  - >30 kg: 0.3 mg (most US auto-injectors), up to 0.5 mg per WAO recommendation
- The 0.3 mg/0.5 mg split is the more accepted convention (Hopkins 2023, Children's Colorado, Seattle Children's, AAP 2017 epinephrine policy). The entry's `mx:.5` is the WAO/children's hospital convention.
- **Source:** WAO 2020 update; AAP 2017 policy (publications.aap.org pediatrics 139/3 e20164006); Hopkins Anaphylaxis Pathway 2023.
- **Suggested fix:** change `mx:.5` → `mx:.3` (per AAP/Auto-injector convention is the most common US ED practice) OR add a clarifying note that 0.5 mg is the WAO upper cap for >50 kg adolescents.

**33. Epinephrine — Severe/impending arrest (line 462)**
- Current: `0.01 mg/kg IV/IO, 1:10,000 (0.1 mg/ml), max 1 mg, "For shock or impending arrest ONLY. Slow IV push"`
- ✅ **Correct.** IV epinephrine 0.01 mg/kg of 1:10,000 (max 1 mg) for anaphylactic shock/impending arrest, slow IV push.
- **Source:** AAP; PALS; FDA epinephrine label.

**34. Diphenhydramine — H1 blocker (line 463)**
- Current: `1–2 mg/kg IV/IO/IM/PO, 50 mg/ml, max 50 mg, "Max 50 mg"`
- ✅ **Correct.** 1–2 mg/kg IV/IM/PO, max 50 mg/dose, max 5 mg/kg/day. PDR; StatPearls.
- **Source:** StatPearls Diphenhydramine 2025; AAFP 2003; PDR Benadryl Children's.

**35. Methylprednisolone — Steroid (line 464)**
- Current: `1–2 mg/kg IV/IO, 62.5 mg/ml, max 125 mg, "Biphasic reaction prevention. Max 125 mg"`
- ✅ **Correct.** 1–2 mg/kg IV, max 125 mg. The note correctly frames steroid as **biphasic reaction prevention** (no role in acute rescue; takes 4–6 h to work).
- **Source:** UNMH Pediatric Anaphylaxis Pathway; Cheng 2011 PMC3043023; wikEM methylprednisolone.

**36. Dexamethasone — Steroid (alt) (line 465)**
- Current: `0.6 mg/kg PO/IV/IO, 4 mg/ml, max 16 mg, "Max 16 mg. Alternative to methylprednisolone"`
- ⚠️ **Anaphylaxis max is 10–18 mg per most sources (wikEM); 16 mg is acceptable.** For croup the max is typically 10–12 mg. The 16 mg figure (used in this entry) is the upper end of the dexamethasone croup/anaphylaxis range. ✅ **Acceptable** for anaphylaxis; only mild concern.
- **Source:** wikEM dexamethasone; Children's MN croup pathway; CPS acute croup position statement 2017.
- **Verdict:** ✅ correct (could also be 10 mg per some sources, 16 mg is the higher acceptable cap; not critical).

**37. Famotidine — H2 blocker (line 466)**
- Current: `0.5 mg/kg IV/IO, 10 mg/ml, max 20 mg, "Max 20 mg"`
- ✅ **Correct.** 0.5 mg/kg IV (max 20 mg) for anaphylaxis adjunct. Per FDA 2025 label, the IV pediatric dose is 0.25 mg/kg q12h titrated to max 0.5 mg/kg q12h (max 20 mg/dose). For single-dose anaphylaxis adjunct 0.5 mg/kg IV (max 20 mg) is widely used.
- **Source:** UNMH Pediatric Anaphylaxis Pathway; FDA famotidine injection 2025 label (219935s000lbl); AAP Pediatric Care Online Anaphylaxis 2022.

**38. Ranitidine — H2 blocker (alt) (line 467)**
- Current: `1 mg/kg IV/IO, 25 mg/ml, max 50 mg, "Alternative to famotidine. Max 50 mg"`
- ❌ **CRITICAL — Ranitidine was withdrawn from the US market in 2020 due to NDMA contamination.** All ranitidine products (Zantac and generics) were requested to be removed by the FDA on April 1, 2020. **The drug is not available for prescription or OTC use in the US.** Including it on a bedside code sheet as an "alternative to famotidine" is dangerously misleading — a resident at the bedside would have no way to obtain it.
- **Source:** FDA News Release April 1, 2020: "FDA Requests Removal of All Ranitidine Products (Zantac) from the Market" (fda.gov/news-events/press-announcements/fda-requests-removal-all-ranitidine-products-zantac-market); AHA 4/1/2020; Wagner 2021 PMC8301580.
- **Suggested fix:** DELETE the ranitidine entry entirely, or replace with another H2 (e.g., cimetidine) if a second H2 is desired — but **famotidine alone is sufficient** for anaphylaxis adjunct. If keeping a placeholder for non-US users, add a note: *"⚠️ Ranitidine withdrawn from US market 2020 (NDMA). Use famotidine."*

**39. Albuterol — Bronchospasm (line 468)**
- Current: `2.5–5 mg Neb, 0.5% (5 mg/ml), "Fixed dose (not weight-based). Continuous for severe"`
- ✅ **Correct.** Albuterol nebulized 2.5 mg (for <20 kg) to 5 mg (>20 kg) is the standard intermittent dose; continuous 0.5 mg/kg/hr (max 20 mg/hr) for severe.
- **Source:** AAP Pediatric Care Online albuterol; OHSU DCH Asthma Pathway 2021; UpToDate pediatric albuterol.
- *(Note: This is in the Anaphylaxis section, but it duplicates the Asthma section's Albuterol entry — minor redundancy, out of scope to fix here.)*

**40. IV Fluid Bolus — Hypotension (line 469)**
- Current: `20 ml/kg IV/IO, NS or LR, "Repeat as needed. Up to 60 ml/kg in first hour for severe shock"`
- ✅ **Correct.** 20 mL/kg bolus × 3 (60 mL/kg) in first hour for severe pediatric shock, NS or LR.
- **Source:** PALS; Surviving Sepsis Campaign Pediatric 2020; AAP.

---

### Status Epilepticus

**41. Lorazepam — 1st line (line 472)**
- Current: `0.05–0.1 mg/kg IV/IO, 2 mg/ml, max 4 mg, "Max 4 mg. Repeat once if needed. Onset 2-5 min"`
- ✅ **Correct.** IV/IO lorazepam 0.05–0.1 mg/kg (most use 0.1 mg/kg), max 4 mg/dose. Note: many protocols now use 0.1 mg/kg as the single dose (no range). 0.05 mg/kg is the lower end if using a half-dose strategy.
- **Source:** Stanford Pediatric Status Epilepticus Pathway; AES 2017; CHOP; Pediatric Critical Care 2022.

**42. Midazolam — No IV access (line 473)**
- Current: `0.1–0.2 mg/kg IM/IN, 5 mg/ml, max 10 mg, "IN via MAD device. Also buccal route"`
- ⚠️ **Buccal route is missing from the route list.** The entry says r:'IM/IN' but does not include **buccal**, which is a first-line non-IV route for status epilepticus (CPS, Children's MN, Starship). Dose for buccal is **0.5 mg/kg** (not 0.1–0.2), per Starship, CPS, and Children's MN status algorithms.
- **Source:** Starship NZ PICU 2022; CPS 2021 Status Epilepticus algorithm; Children's MN Status Epilepticus pathway; EIIC PEAK Status Epilepticus 2025.
- **Suggested fix:** split into two entries (IM/IN: 0.2 mg/kg max 10 mg; Buccal: 0.5 mg/kg max 10 mg) or expand route list and add note about buccal dose.

**43. Diazepam — No IV access (line 474)**
- Current: `0.2–0.5 mg/kg PR/IV, 5 mg/ml, max 20 mg, "PR max 20 mg, IV max 10 mg. Rectal gel if available"`
- ✅ **Correct.** Diastat (rectal diazepam gel) 0.2–0.5 mg/kg per FDA label; max 20 mg PR / 10 mg IV. Note that the IV max of 10 mg is per Stanford pathway for status epilepticus.
- **Source:** FDA Diastat label (accessdata.fda.gov); Stanford pathway; MSF; CHW NSW PR diazepam protocol.

**44. Fosphenytoin — Load (line 475)**
- Current: `15–20 mg PE/kg IV/IO, 50 mg PE/ml, max 1500 mg PE, "Load over 10 min. PE = phenytoin equivalents. Can give IM if needed"`
- ✅ **Correct.** 15–20 mg PE/kg IV load (max 1500 mg PE/dose) over 10 min, can give IM.
- **Source:** FDA fosphenytoin label (labeling.pfizer.com ShowLabeling.aspx?id=749); Stanford; Lurie Children's; CHOP.

**45. Levetiracetam — Load (line 476)**
- Current: `20–60 mg/kg IV/IO, 100 mg/ml, max 4500 mg, "60 mg/kg for status; 20-40 mg/kg for other seizures. Give over 5-15 min"`
- ✅ **Correct.** Levetiracetam 60 mg/kg IV (max 4500 mg/dose) for status epilepticus, 20–40 mg/kg for other seizure indications. CHOP/Stanford/CHW all use 60 mg/kg max 4500 mg.
- **Source:** CHOP Status Epilepticus Pathway; Stanford; litFL Levetiracetam 2025; Key Advance Pediatric Status Epilepticus 2024.

**46. Phenobarbital — Load (line 477)**
- Current: `15–20 mg/kg IV/IO, 65 or 130 mg/ml, max 1000 mg, "SLOW push. Respiratory depression risk — have airway ready"`
- ✅ **Correct.** Phenobarbital 15–20 mg/kg IV (max 1000 mg/dose); maximum total dose 30 mg/kg. SLOW push with respiratory monitoring.
- **Source:** CHEO Phenobarbital 2019; Children's MN; Stanford; FDA Sezaby 2024 label (15–20 mg/kg).

---

### Procedural Sedation

**47. Ketamine — Dissociative (line 480)**
- Current: `1–2 mg/kg IV/IO, 100 mg/ml, "Lower for analgesia, higher for dissociation. Give over 60 sec. Maintain airway"`
- ⚠️ **Route is incomplete.** Procedural sedation ketamine can also be given **IM 4–5 mg/kg** (no IV needed) — a critical route for kids without IV access. The "IV/IO" only is a meaningful omission.
- **Source:** Green et al. 2011 Ann Emerg Med; AAP Clinical Practice Guideline; wikEM ketamine; Perth Children's Hospital.
- **Suggested fix:** change `r:'IV/IO'` → `r:'IV/IM'` (or split into two entries: IV 1–2 mg/kg + IM 4–5 mg/kg). If keeping one entry, add IM sub-dose in note.

**48. Midazolam — Anxiolysis (line 481)**
- Current: `0.05–0.15 mg/kg IV/IO/IM/IN/PO, 5 mg/ml, max 2 mg, "Max 2 mg. IN via MAD. PO liquid available"`
- ⚠️ **Max of 2 mg is too low for older children/adolescents.** The standard pediatric midazolam max is **10 mg** for procedural sedation and seizure (consistent with the Status Epilepticus entry on line 473). 2 mg is appropriate only for small children. For a 40 kg child, 0.15 mg/kg = 6 mg, capped at 2 mg is significant underdosing.
- **Source:** PEMMorsels midazolam; AAP; Lexicomp; FDA CIV midazolam label.
- **Suggested fix:** change `mx:2, mu:'mg'` → `mx:10, mu:'mg'`. (Note also: PO max is often 20 mg per single dose per Lexicomp, but 10 mg is the safer bedside cap.)

**49. Fentanyl — Analgesia (line 482)**
- Current: `0.5–2 mcg/kg IV/IO/IN, 50 mcg/ml, max 100 mcg, "IN via MAD for quick pain control. Watch chest wall rigidity"`
- ✅ **Correct.** Fentanyl 0.5–2 mcg/kg IV/IN/IM, max 100 mcg, with chest-wall rigidity warning.
- **Source:** FDA fentanyl citrate label; StatPearls 2023; UCSF Pain Management.

**50. Morphine — Analgesia (line 483)**
- Current: `0.05–0.1 mg/kg IV/IO/IM, 2 mg/ml, max 4 mg, "Titrate to pain. Onset 5-10 min IV"`
- ✅ **Correct.** Morphine 0.05–0.1 mg/kg IV/IM, max 4 mg/dose. Onset 5–10 min IV.
- **Source:** AAP; Lexicomp; Pediatric Sedation Mehta 2023.

---

### Push-Dose Pressors

**51. Epinephrine — Push-dose (line 486)**
- Current: `0.5–1 mcg/kg IV, (diluted) 10 mcg/ml, max 10 mcg, "Prep: 1 ml of 1:10,000 + 9 ml NS = 10 mcg/ml. Push 1 ml at a time q2-5min"`
- ⚠️ **Dose range and prep math are correct, but the dose `lo:.5` is not standard.** PEM Playbook / Weingart / REBEL EM / NorCal EMS all cite pediatric push-dose epi at **0.1 mL/kg (1 mcg/kg) per dose, max 10 mcg (1 mL), repeat q1–5 min.** The 0.5–1 mcg/kg range is essentially a 1 mcg/kg single dose, which is fine — but `lo:.5` allows half-strength dose which most bedside EM protocols do not list separately.
- **Prep math verification:**
  - 1 mL of 1:10,000 = 0.1 mg = **100 mcg** epinephrine
  - + 9 mL NS = 10 mL total
  - → 100 mcg / 10 mL = **10 mcg/mL** ✅ **math correct**
- **Source:** PEM Playbook push-dose epi; REBEL EM pediatric push-dose epi; Weingart 2015 PMC5052865; NorCal EMS 2025.
- **Verdict:** ✅ prep math correct, dose acceptable; `lo:.5` is slightly nonstandard but not wrong.

**52. Phenylephrine — Push-dose (line 487)**
- Current: `5–20 mcg/kg IV, (diluted) 100 mcg/mL, "Prep: 10 mg in 100 ml NS = 100 mcg/ml. Titrate to effect. q2-5min"`
- ⚠️ **Prep math:**
  - 10 mg phenylephrine (1 mL of 10 mg/mL vial) into 100 mL NS = 100 mL total
  - → 10 mg / 100 mL = 0.1 mg/mL = **100 mcg/mL** ✅ **math correct**
- ⚠️ **Dose range 5–20 mcg/kg is high for bedside push-dose.** Standard adult push-dose phenylephrine is 50–200 mcg (0.5–2 mL of 100 mcg/mL) per dose, NOT mcg/kg. The mcg/kg dosing in pediatrics is rarely standardized. Most pediatric protocols use a fixed **1–2 mcg/kg per dose** (range 0.5–2 mcg/kg) titrated, not 5–20 mcg/kg which would be massive in a 20 kg child (100–400 mcg = 1–4 mL).
- **Source:** wikEM phenylephrine; LITFL; Weingart 2015 PMC5052865; CHEO 2017.
- **Suggested fix:** change `lo:5, hi:20, u:'mcg/kg'` → `lo:1, hi:2, u:'mcg/kg'` (standard pediatric push-dose range is 0.5–2 mcg/kg/dose). Or change to fixed mcg per dose: `5–20 mcg per push (0.05–0.2 mL)`.
- **Verdict:** ⚠️ dose range is **5–20× too high** — this is potentially dangerous (massive alpha-agonism in a small child). PATCH THIS.

---

## SUMMARY

### 1. CRITICAL ERRORS (could harm a patient)
| # | Drug | Problem | Fix |
|---|------|---------|-----|
| 1 | **Ranitidine** (line 467, Anaphylaxis) | Drug was **withdrawn from US market in April 2020 by FDA** due to NDMA contamination. A resident at the bedside cannot obtain it. Listing it as an "alternative to famotidine" is dangerously misleading. | **DELETE the entry entirely**, or replace with explicit warning: *"⚠️ Withdrawn from US market 2020. Use famotidine."* |
| 2 | **Phenylephrine push-dose** (line 487) | Dose range `5–20 mcg/kg` is **5–20× higher than the standard pediatric push-dose range of 0.5–2 mcg/kg/dose**. A 20 kg child getting 20 mcg/kg would receive 400 mcg = 4 mL of the 100 mcg/mL solution — a massive alpha-agonist bolus that can cause hypertensive emergency, reflex bradycardia, and worsened end-organ perfusion. | Change `lo:5, hi:20, u:'mcg/kg'` → `lo:1, hi:2, u:'mcg/kg'`. Add note: *"Per dose, max 100 mcg (1 mL); repeat q1–5 min."* |
| 3 | **Atropine ET dose** (line 452) | Listed as 0.03–0.04 mg/kg. Correct PALS dose is **0.04–0.06 mg/kg ET**. The lo end of 0.03 is **25% underdose** for a brady-arrest child with no IV access. | Change `lo:.03, hi:.04` → `lo:.04, hi:.06`. |

### 2. MODERATE ERRORS (suboptimal/wrong but not immediately life-threatening)
| # | Drug | Problem | Fix |
|---|------|---------|-----|
| 4 | Atropine Bradycardia (line 451) | Note says "1 mg (>40 kg)" but the entry's max is 0.5 mg; PALS 2025 no longer has the >40 kg/1 mg break. | Change note to: *"Min 0.1 mg. Max single dose 0.5 mg. Higher doses for organophosphate poisoning."* |
| 5 | Atropine pretreatment (line 420) | Note says "no minimum dose" but PALS 2025 still lists 0.1 mg minimum for bradycardia. | Change note to: *"Per 2025 AHA PALS: 0.02 mg/kg IV/IO. Min 0.1 mg, max single dose 0.5 mg. May repeat once."* |
| 6 | Epinephrine arrest IV/IO (line 445) | Note "No maximum in arrest" contradicts the displayed max of 1 mg. | Remove or rephrase: *"Repeat q3–5 min. Per-dose max 1 mg."* |
| 7 | Epinephrine arrest ET (line 446) | Lo end 0.05 mg/kg is outdated; PALS 2020+ lists 0.1 mg/kg ET. | Change `lo:.05` → `lo:.1` (single value). |
| 8 | Midazolam post-intubation (line 438) | Max 2 mg is too low for older children; should be 10 mg. | Change `mx:2` → `mx:10`. |
| 9 | Lorazepam post-intubation (line 439) | Max 2 mg is too low for older children; should be 4 mg (matches Status Epilepticus entry). | Change `mx:2` → `mx:4`. |
| 10 | Midazolam status no-IV (line 473) | Buccal route missing from route list; buccal dose is 0.5 mg/kg, not 0.1–0.2. | Either add separate entry for buccal (0.5 mg/kg, max 10 mg) or expand note. |
| 11 | Midazolam procedural (line 481) | Max 2 mg too low for older children; standard is 10 mg. | Change `mx:2` → `mx:10`. |
| 12 | Ketamine procedural (line 480) | IM route missing — IM 4–5 mg/kg is the most common pediatric procedural route when no IV. | Add IM route: change `r:'IV/IO'` → `r:'IV/IM'` and add IM dose 4–5 mg/kg in note. |
| 13 | Dextrose D10W (line 457) | Note doesn't clarify the age-based threshold for D10 vs D25 vs D50 (5/2/1 rule). The 5–10 mL/kg range only applies to neonates/infants. | Update note to include 5/2/1 rule by age (neonate D10 5–10; <8 yr D25 2 mL/kg; >8 yr D50 1 mL/kg). |
| 14 | Epinephrine IM (line 461, Anaphylaxis) | Conflict between `mx:.5` and note's "0.3 mg (<30 kg), 0.5 mg (≥30 kg)". The 0.3/0.5 split is the AAP auto-injector convention; the 0.5 cap is WAO. AAP 2017 epinephrine policy uses 0.15 mg for 15–30 kg and 0.3 mg for >30 kg auto-injector. For syringe-based, 0.01 mg/kg up to 0.3 mg (<30 kg) or 0.5 mg (≥30 kg) is fine. | Either match `mx:.5` with the 0.3/<30 kg detail in note, or change `mx:.5` → `mx:.3` for AAP consistency. |

### 3. UNCERTAIN/UNVERIFIED (couldn't find a definitive primary source — flag for Greg)
- **Etomidate "avoid in sepsis" note** (line 425): the 2025 Mendez et al. retrospective (PMC11945125) did not find increased adrenal insufficiency in peds ED single-dose etomidate. The 2024 ACR/EMRA reviews still favor ketamine in sepsis but the "avoid" language is stronger than the data. Could soften to: *"Adrenal suppression (4–8 h) — prefer ketamine in sepsis."* — Directionally correct, but the absolute "avoid" may be overstating the evidence.
- **Albuterol anaphylaxis bronchospasm** (line 468): the entry is duplicated in the Asthma section (out of scope). Confirm whether duplication is intentional.
- **Dextrose D10W 5–10 mL/kg range**: standard for neonates (UCSF, wikEM); for older infants the dose is usually 5 mL/kg of D10W to deliver 0.5 g/kg, but I did not find a single primary source confirming "5–10 mL/kg of D10W" as the universal PALS range.
- **Naloxone lo end 0.01 mg/kg** (line 453): mostly used for neonatal reversal; the adult/older child chronic-opioid strategy uses 0.01–0.05 mg/kg. The hybrid range 0.01–0.1 mg/kg is widely used but I could not find a single primary source endorsing the wide range as a single bedside entry.
- **Dexmedetomidine load 0.5–2 mcg/kg** (line 441): common range per FDA Precedex label and PEMMorsels, but the upper 2 mcg/kg is rarely used in ED settings — most use 0.5–1 mcg/kg load. Could be flagged as high.
- **Epinephrine IM 0.3 vs 0.5 mg cap** (line 461): pediatric auto-injectors are FDA-approved at 0.15 mg (15–30 kg) and 0.3 mg (>30 kg) per AAP 2017. WAO recommends 0.5 mg max regardless of weight. The bedside sheet should pick one convention explicitly.

### 4. ROUTE AMBIGUITY (technically correct but the EM convention is different, or list is incomplete)
- **Midazolam status** (line 473): buccal is missing; this is one of the most common first-line non-IV routes per Starship NZ, CPS, Children's MN, EIIC. Strongly recommend adding.
- **Ketamine procedural** (line 480): IM route is missing. IM 4–5 mg/kg is the standard ED procedural sedation route when no IV.
- **Diazepam status** (line 474): the route list `r:'PR/IV'` is correct but doesn't include IM (diazepam IM is poorly absorbed — not used in practice, so omitting IM is correct, just noting).
- **Lidocaine RSI pretreatment** (line 421): the route list says IV/IO only, which is correct (no IM or IN for laryngoscopy ICP blunting).
- **Fosphenytoin** (line 475): route list is correct (IV/IO) and the note correctly mentions IM as a secondary option.

---

## POSITIVE FINDINGS (correct as written)
The following entries are accurate against PALS 2025, Harriet Lane 22e, Lexicomp, and FDA labels — no change needed:
- Lidocaine RSI pretreatment (line 421)
- Fentanyl RSI pretreatment (line 422)
- Etomidate dose (line 425) — note about sepsis is a stylistic minor
- Ketamine induction (line 426)
- Propofol induction (line 427)
- Midazolam induction (line 428)
- Succinylcholine split dose (line 431)
- Rocuronium RSI dose (line 432)
- Vecuronium RSI dose (line 433)
- Fentanyl post-intubation (line 436)
- Morphine post-intubation (line 437)
- Propofol infusion (line 440)
- Dexmedetomidine infusion (line 441)
- Ketamine infusion (line 442)
- Epinephrine IV arrest (line 445) — fix note only
- Amiodarone (line 447)
- Lidocaine VF (line 448)
- Adenosine 1st + 2nd (lines 449–450)
- Calcium chloride (line 454)
- Magnesium sulfate (line 455)
- Sodium bicarbonate (line 456)
- Epinephrine IV for anaphylaxis shock (line 462)
- Diphenhydramine (line 463)
- Methylprednisolone (line 464)
- Dexamethasone (line 465)
- Famotidine (line 466)
- Albuterol bronchospasm (line 468)
- IV fluid bolus (line 469)
- Lorazepam status (line 472)
- Diazepam status (line 474)
- Fosphenytoin (line 475)
- Levetiracetam (line 476)
- Phenobarbital (line 477)
- Fentanyl procedural (line 482)
- Morphine procedural (line 483)
- Push-dose epi prep math (line 486) — math verified

---

## RECOMMENDED PATCH ORDER (priority)
1. **DELETE ranitidine** (line 467) — CRITICAL
2. **FIX phenylephrine push-dose range** (line 487): 5–20 → 1–2 mcg/kg — CRITICAL
3. **FIX atropine ET range** (line 452): 0.03–0.04 → 0.04–0.06 mg/kg — CRITICAL
4. **FIX epinephrine ET lo end** (line 446): 0.05 → 0.1 mg/kg — MODERATE
5. **FIX midazolam post-intubation max** (line 438): 2 mg → 10 mg — MODERATE
6. **FIX lorazepam post-intubation max** (line 439): 2 mg → 4 mg — MODERATE
7. **FIX midazolam procedural max** (line 481): 2 mg → 10 mg — MODERATE
8. **ADD midazolam buccal route/dose** (line 473) — MODERATE (route completeness)
9. **ADD ketamine IM route** (line 480) — MODERATE (route completeness)
10. **FIX atropine bradycardia note** (line 451): drop "1 mg (>40 kg)" — MODERATE
11. **FIX atropine pretreatment note** (line 420): add 0.1 mg minimum back — MODERATE
12. **FIX epinephrine arrest note** (line 445): remove "No maximum in arrest" — MODERATE
13. **UPDATE dextrose note** (line 457) with 5/2/1 rule — MODERATE
14. **CLARIFY epinephrine IM max** (line 461) — moderate/uncertain
15. **SOFTEN etomidate sepsis note** (line 425) — UNCERTAIN (directionally correct)

---

## CITATIONS (primary sources used)
- AHA PALS 2025 — Lasa et al. "Part 8: Pediatric Advanced Life Support: 2025 American Heart Association Guidelines for CPR and ECC" (publications.aap.org pediatrics 157/1 e2025074351; ahajournals.org/doi/10.1161/CIR.0000000000001368)
- AHA PALS Cardiac Arrest Algorithm 2025 (cpr.heart.org/-/media/CPR-Files/.../Algorithm-PALS-CA-250123.pdf)
- AHA PALS Bradycardia Algorithm 2025 (cpr.heart.org/-/media/CPR-Files/.../Algorithm-PALS-Bradycardia-250121.pdf)
- AHA PALS Tachycardia Algorithm 2025 (cpr.heart.org/-/media/CPR-Files/.../Algorithm-PALS-Tachyarrhythmia-250117.pdf)
- Harriet Lane Handbook 22e (general reference; not paginated in this audit)
- AAP Pediatric Care Online drug monographs (publications.aap.org/pediatriccare): Etomidate, FentaNYL, Famotidine, Albuterol, Diphenhydramine, Vecuronium, Calcium Chloride, Magnesium Sulfate
- FDA Diastat label 2016 (accessdata.fda.gov/drugsatfda_docs/label/2016/020648s014lbl.pdf)
- FDA Fosphenytoin label (labeling.pfizer.com/ShowLabeling.aspx?id=749)
- FDA Famotidine Injection 2025 label (accessdata.fda.gov/drugsatfda_docs/label/2025/219935s000lbl.pdf)
- FDA Amidate (etomidate) label (labeling.pfizer.com/ShowLabeling.aspx?id=4444)
- FDA Succinylcholine label 2022 (accessdata.fda.gov/drugsatfda_docs/label/2022/215143Orig1s001Lbl.pdf)
- FDA Midazolam CIV Injection label (labeling.pfizer.com/ShowLabeling.aspx?id=4529)
- FDA Ranitidine market withdrawal notice 2020 (fda.gov/news-events/press-announcements/fda-requests-removal-all-ranitidine-products-zantac-market)
- AAP 2017 Epinephrine for First-aid Management of Anaphylaxis (publications.aap.org/pediatrics/article/139/3/e20164006)
- Weingart 2015 — "Push-dose pressors for immediate blood pressure control" (PMC5052865)
- PEM Playbook — Push-Dose Epi (pemplaybook.org/podcast/push-dose-epi/)
- REBEL EM — "Getting the Epi Dose Right During Pediatric Resuscitation" (rebelem.com 2018)
- Green et al. 2011 — "Clinical Practice Guideline for Emergency Department Ketamine Dissociative Sedation" (Ann Emerg Med)
- Lasa et al. 2025 — AHA PALS 2025 update (publications.aap.org/pediatrics/article/157/1/e2025074351)
- CHOP Status Epilepticus Clinical Pathway
- Stanford Pediatric Status Epilepticus Pathway
- Children's MN Status Epilepticus
- UNC Pediatric ED RSI Checklist 2025
- UNC PICU Propofol Continuous Infusion Guideline 2017
- 5/2/1 rule (PEM Cincinnati 2021)
- Kresta et al. 2024 — "Magnesium Sulfate in Pediatric Emergency Medicine" (PMC12497407)
- Mendez et al. 2025 — "Single-dose etomidate for RSI in children" (PMC11945125)

---

**End of audit report.**
