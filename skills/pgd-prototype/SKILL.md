---
name: pgd-prototype
description: Create or update Product GSD prototype demos: lightweight multi-file HTML/CSS/JS demos with mock data, copy JSON, product spec JSON, stable data-pm-id markers, and local interactions. Use instead of single-file static HTML unless the user explicitly asks for disposable output.
---

# PGD Prototype

Use `product-gsd/references/prototype-demo.md` and align with `ai-prototype-spec`.

## Default Output

```text
.product/features/<feature-slug>/prototype/
  index.html
  styles.css
  app.js
  data/sample-data.json
  data/copy.zh-CN.json
  spec/product-spec.json
```

## Workflow

1. Inspect existing prototype files first.
2. Read PRD or create/update PRD summary before UI.
3. Create `product-spec.json` for pages, entities, statuses, fields, actions, and permissions.
4. Create `sample-data.json` with realistic business records.
5. Create `copy.zh-CN.json` for visible copy.
6. Generate `index.html`, `styles.css`, and `app.js`.
7. Verify clickable workflow, responsive layout, and state coverage.

## Rules

- Every meaningful UI element needs stable `data-pm-id`.
- Do not call real APIs.
- Keep demo stronger than static prototype but lighter than production development.

