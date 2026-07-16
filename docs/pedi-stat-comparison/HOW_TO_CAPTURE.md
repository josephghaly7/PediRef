# How to Capture Pedi STAT for Comparison

Goal: screenshot every screen of Pedi STAT so we can compare its content, calculator output, and UI to our app.

## Setup
1. Install Pedi STAT (free or paid) on your emulator/laptop
2. Launch it
3. Use a known patient weight for every screenshot. Pick **10 kg** (1 year old) for all calculations. This gives us a fixed point to compare.

## Screens to capture (in order)

### 1. Home / Patient Input
- [ ] Main input screen (the "enter weight/age/length" page)
- [ ] After entering 10 kg, what does the result screen look like?
- [ ] Method picker (age vs weight vs length)

### 2. Drug Categories: capture each
- [ ] Cardiac Arrest / Resuscitation
- [ ] Airway / Intubation
- [ ] RSI
- [ ] Anaphylaxis / Allergic Reactions
- [ ] Seizures
- [ ] Procedural Sedation
- [ ] Pain Management
- [ ] Hypoglycemia
- [ ] Toxicology
- [ ] Any "other" category we don't have

### 3. Specific Drug Screens (10 kg patient)
For each of these, tap into the drug and screenshot the full display:
- [ ] Atropine
- [ ] Epinephrine (push-dose if they have it, arrest dose, infusion)
- [ ] Amiodarone
- [ ] Adenosine
- [ ] Fentanyl
- [ ] Morphine
- [ ] Midazolam
- [ ] Ketamine
- [ ] Rocuronium
- [ ] Succinylcholine
- [ ] Sodium Bicarbonate
- [ ] Calcium
- [ ] Dextrose (D10, D25, D50)
- [ ] Diphenhydramine
- [ ] Methylprednisolone
- [ ] Any antibiotic/antiviral they have

### 4. Equipment Sizing
- [ ] ETT size + depth (uncuffed + cuffed)
- [ ] Laryngoscope blade
- [ ] Suction catheter
- [ ] NG tube
- [ ] Foley
- [ ] Chest tube
- [ ] Central line
- [ ] IV catheter
- [ ] BP cuff
- [ ] Broselow-equivalent length-based data

### 5. Tools / Calculators
- [ ] Pediatric Assessment Triangle / Score
- [ ] GCS
- [ ] Croup score (Westley)
- [ ] Burn %TBSA
- [ ] Parkland formula
- [ ] Pediatric Code Sheet (the exportable/printable one)
- [ ] Vitals by age
- [ ] Tox / antidote lookup

### 6. Settings / About
- [ ] Version number
- [ ] Source citations (if they show any)
- [ ] Update date
- [ ] Any "powered by Lexicomp" / "sourced from" footer

## How to share with me
- Save screenshots to `~/pedi-stat/docs/pedi-stat-comparison/screenshots/`
- Use clear filenames: `01_home_input.png`, `02_atropine_10kg.png`, etc.
- Or just drag/attach in Discord; I can read them and catalog.

## What I will do with them
- Build a feature matrix: they have X, we have Y, we need to add Z
- Compare dose-by-dose: where we disagree, I will research which is right
- Note UI patterns: how they lay out the dose line, how they show max/conc, etc.
- Flag any features you want to clone vs leave behind
