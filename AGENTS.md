# PediRef maintainer instructions

## Source of truth

- `data/data_neonatal.json`
- `data/data_pedi.json`
- `data/data_adult.json`

`index.html` embeds these JSON objects for offline operation. Do not create or restore a separate hand-coded medication array or flattened `flat_drugs_*.json` export.

## Safe change rules

1. Preserve the JSON values exactly unless the project owner explicitly approves a clinical-data change.
2. Keep non-dosage entries: notes, tables, algorithms, steps, empty categories, and empty subcategories are intentional.
3. Do not add clinical values from memory. Use a verified source and document the decision before changing source data.
4. Run the data-bundle check and JavaScript syntax check before committing.
5. Test the three group screens and search in a browser before deployment.

## Checks

```bash
python3 scripts/verify_data_bundle.py
node -e "const fs=require('fs');const h=fs.readFileSync('index.html','utf8');const m=h.match(/<script>([\\s\\S]*?)<\\/script>/);if(!m)throw Error('script missing');fs.writeFileSync('/tmp/pediref-check.js',m[1]);"
node --check /tmp/pediref-check.js
```

## Runtime

```bash
python3 -m http.server 4173
```

Open `http://127.0.0.1:4173/`. Do not use `file://` when testing PWA behavior.
