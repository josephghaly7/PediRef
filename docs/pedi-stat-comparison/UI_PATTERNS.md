# STAT EM (Pedi STAT) — UI/UX Patterns from Screenshots

**Source:** 33 STAT EM screenshots + 1 wikem.org Broselow reference, captured 2026-07-16
**Location:** `docs/pedi-stat-comparison/screenshots/`
**Detailed catalog:** `SCREENSHOT_CATALOG.json`

---

## Key UI Patterns Observed

### 1. **Multi-input patient entry (the killer feature)**

STAT EM has 6 ways to enter a patient, accessible from the home screen:

| Button | Input | Icon |
|---|---|---|
| Pediatric Weight | direct kg/lb, ≤43 kg | scale |
| Pediatric Age | years + months, or birthday | calendar |
| Pediatric Height | direct cm/in | ruler |
| Pediatric Length Tape | Broselow color-coded weight | colored squares |
| Adult | >43 kg | person |
| Neonatal Resuscitation | gest-age-based dosing | baby |

**Why it matters:** Greg's app currently only has kg input. A kid comes in with no scale — you can use age, length, or Broselow color. STAT EM handles all 4. We should add at least age and length.

### 2. **Broselow color = weight (verifies our colors match)**

From the screenshots and wikem.org, the standard Broselow colors:

| Color | Weight (kg) | Age (approx) |
|---|---|---|
| Preemie | 2-3 | newborn preterm |
| Gray | 3.5-5 | newborn term |
| Pink | 6-7 | 4 mo |
| Red | 8-9 | 6 mo |
| Purple | 10-11 | 1 yr |
| Yellow | 12-14 | 2 yr |
| White | 15-18 | 4 yr |
| Blue | 19-23 | 6 yr |
| Orange | 24-29 | 8 yr |
| Green | 30-36 | 10 yr |

### 3. **Persistent bottom bar = always-visible weight/age/height**

Every screen has a bottom bar showing the current patient: weight icon + value, age icon + value, height icon + value, Favorites button. This is the patient's "context" — never lost when navigating.

**Our app equivalent:** we have a kg input at the top. We should consider a persistent patient bar that survives scrolling, or at least stays sticky.

### 4. **Search bar always present on category lists**

Every categories list has a search bar with placeholder "categories, medications, equipment, etc." — lets you search across the entire app from anywhere. **Our app has a search button in the tools bar but it's not always visible.** Adding an inline search at the top of sections would be a small but useful change.

### 5. **Categories list uses colored squares as visual icons**

Each category has a colored square to its left (blue, orange, green, pink, yellow, etc.). These appear to be randomly assigned but provide visual differentiation. We have emojis (💉 😴 💪) — these work but colored squares are more scannable when scrolling fast.

### 6. **Age input uses wheel pickers, not text fields**

The "Enter Age" screen has two wheels (years, months) — like iOS date picker. Faster to spin than to type. We have a text input for kg; could do the same for age.

### 7. **Default weight prompt for neonatal section**

When entering the neonatal section, a modal pops up: "A default weight of 3500 grams have been set for this section's calculations. For most accurate calculations, it is recommended this is modified by using the bottom bar weight icon once a weight is known."

**Insight:** they don't make you enter a weight — they assume 3.5 kg (term newborn) and let you adjust. Smart default for the most common case. We could do this for our "Resuscitation" section.

### 8. **IBW (Ideal Body Weight) calc for adult patients**

Adult flow: enter height + sex → app calculates IBW → uses IBW for med dosing (not actual weight). This is the standard adult EM practice. Our app is peds-only but it's worth noting that STAT EM uses IBW because actual weight would overdose the obese patient.

### 9. **No clinical content in these screenshots**

Important caveat: these 34 screenshots are **all navigation/setup screens**. None of them show actual drug doses, equipment tables, or clinical content. To see the drug values, we'd need to:
- Tap into a category (e.g., "Cardiac Resuscitation")
- Tap into a drug
- That shows the dose + volume at the entered weight

The JSON dumps from earlier (`data_pedi.json`, `data_neonatal.json`, `data_adult.json`) have the actual content. Screenshots only show the navigation layer.

### 10. **Favorites button always present in bottom bar**

The "Favorites" button (star icon) is always in the bottom bar. Users can pin drugs they reach for often. **We don't have this — would be a high-value addition.** Even just a small "★ Starred" section at the top with 5-10 commonly-pinned drugs would help.

---

## UI Patterns We DON'T Have That STAT EM Has

| Pattern | Effort | Value |
|---|---|---|
| Multi-input patient entry (age/length/Broselow) | Medium | High — real-world utility |
| Persistent bottom patient bar | Low | Medium |
| Search bar always visible | Low | High |
| Default weight prompt per section | Low | Medium |
| Favorites/pinning | Medium | High — saves time |
| IBW calc for adult meds | N/A (we're peds) | N/A |

## UI Patterns We HAVE That STAT EM Doesn't

| Pattern | Why it's better for Greg |
|---|---|
| Single PWA, no app store | Free, offline, instant updates |
| Sources modal (transparent citations) | Every dose cited — see why |
| Sourced from UMass 2026 (real institutional document) | Not just a clinical opinion |
| Lightweight (no native app install) | No permission prompts, no storage cost |

---

## Screenshots NOT Captured (would need another pass)

To complete the comparison, we'd also want:
- Tap into "Cardiac Resuscitation" → see a drug → see the dose + volume calculation
- Tap into "Equipment" → see the ETT/NG/foley tables
- Tap into "CODE SHEET" → see what the printable code sheet looks like
- The drug-detail screen UI (how they show multiple concentrations, dose ranges, max)
- Any "premium" / paywall screens

If Greg wants to do a second pass to capture the actual drug screens, we can compare UI patterns for how each app displays a dose at a given weight — that's the most important comparison for an emergency reference app.
