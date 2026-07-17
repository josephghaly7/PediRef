# 🩺 PediRef — JSON Clinical Reference

A free, offline-first clinical reference app for healthcare professionals. The neonatal, pediatric, and adult data sets are bundled and rendered directly from the supplied JSON files. Works on any device — installable as a native app (PWA).

**Built by PGY-1s, for PGY-1s.** Because $8 is $8.

## Features
- 👶 **Neonates / Peds / Adults** group switcher
- 📦 **Full-fidelity JSON rendering** — categories, subcategories, notes, tables, algorithms, steps, all dosage records, concentrations, segments, and extra fields
- 🔎 **Search across every JSON field**
- ⚖️ **Optional weight calculation line** — shown separately from the exact source formula/value
- 🧾 **Exact JSON disclosure** on every entry for auditability
- 📴 **Works fully offline** — no cell service? No problem.
- 📱 **Install on home screen** — works like a native app on iOS & Android

## How to Install on Your Phone
1. Open the site in Safari (iPhone) or Chrome (Android)
2. Tap the Share button → "Add to Home Screen"
3. Done — it's now an app icon on your home screen

## Disclaimer
⚠️ For reference only. Verify all doses against your institutional protocols. Not a substitute for clinical judgment.

## Data Source
- The three user-supplied JSON files: `data_neonatal.json`, `data_pedi.json`, and `data_adult.json`.

The app does not silently drop non-drug entries. Empty categories and empty subcategories are retained as well.
