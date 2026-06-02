---
name: pf-prototype
description: Create or update ProductForge product prototype demos as PM-owned demonstration assets with mock data, copy JSON, product spec JSON, stable data-pm-id markers, local interactions, and capability traceability. This does not enter production development.
---

# PF Prototype

Use `product-forge/references/prototype-demo.md`. Treat the prototype as a product management artifact for stakeholder review, not as production software.

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
2. Read `SPEC.md` and PRD before UI. If both are missing, recommend `$pf-spec` or `$pf-prd`.
3. Create `product-spec.json` for pages, entities, statuses, fields, actions, permissions, and capability ID mapping.
4. Create `sample-data.json` with realistic business records.
5. Create `copy.zh-CN.json` for visible copy.
6. Generate `index.html`, `styles.css`, and `app.js`.
7. Verify clickable workflow, responsive layout, and state coverage.

## Rules

- Every meaningful UI element needs stable `data-pm-id`.
- Do not call real APIs.
- Keep demo useful for product review and stakeholder alignment. Do not turn it into a development plan or production implementation.
