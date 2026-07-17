# PediRef

Offline-first clinical reference PWA built from three JSON data sets.

## Project layout

```text
.
├── index.html                 # Complete app: UI, renderer, and bundled JSON
├── data/                      # Canonical source JSON files
│   ├── data_neonatal.json
│   ├── data_pedi.json
│   └── data_adult.json
├── sw.js                      # Service worker and cache version
├── manifest.json              # PWA manifest
├── icon-192.png
├── icon-512.png
├── scripts/                   # Maintainer checks and utilities
└── README.md
```

## Source of truth

The three files in `data/` are the canonical source data:

- `data/data_neonatal.json`
- `data/data_pedi.json`
- `data/data_adult.json`

`index.html` bundles these same JSON objects for offline use and renders the source shape directly. The runtime renderer is intentionally not backed by a separate hand-coded medication array or flattened export.

Current payload coverage:

| Group | Categories | Items | Dosage records |
|---|---:|---:|---:|
| Neonates | 9 | 37 | 8 |
| Peds | 24 | 430 | 379 |
| Adults | 24 | 418 | 367 |

The app retains empty categories/subcategories and non-dosage entries such as notes, tables, algorithms, and step lists. Each entry also has an expandable exact-JSON view for reviewability.

## Run locally

From the project root:

```bash
python3 -m http.server 4173
```

Open <http://127.0.0.1:4173/>.

Do not open `index.html` with `file://`; service-worker/PWA behavior requires HTTP or HTTPS.

## Maintainer checks

Extract and syntax-check the inline JavaScript:

```bash
node -e "const fs=require('fs');const h=fs.readFileSync('index.html','utf8');const m=h.match(/<script>([\\s\\S]*?)<\\/script>/);if(!m)throw Error('script missing');fs.writeFileSync('/tmp/pediref-check.js',m[1]);"
node --check /tmp/pediref-check.js
```

Before deployment, verify that the three bundled objects exactly match the canonical JSON files in `data/`, and test the Neonates, Peds, Adults, search, dose-entry, and exact-JSON disclosure paths in a browser.

## Deployment

GitHub Pages serves `main` at:

<https://josephghaly7.github.io/PediRef/>

After changing the app or service worker, bump the cache identifier in `sw.js`, run the checks above, commit, push, and verify the live URL rather than relying only on the GitHub push result.

## Historical material

Historical audits, comparisons, screenshots, and source-review notes were removed from the public project tree. They are not runtime inputs and can be kept separately outside the repository if needed for provenance.

## Clinical disclaimer

Reference display only. Verify doses and protocols against institutional standards before clinical use. The app does not replace clinical judgment.
