---
name: pm-prototype
description: Create or update ProductForge product prototype demos as PM-owned demonstration assets with mock data, copy JSON, product spec JSON, stable data-pm-id markers, local interactions, and capability traceability. This does not enter production development.
---

# PM Prototype

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

Default mode is lazy generation. Only create the prototype files required by the selected boundary.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before prototype work, ask exactly one boundary question with exactly three options:
   - 问题：这次 prototype 主要用于什么验证？
   - A. 概念演示，只验证页面和主价值表达。
   - B. 工作流演示，验证关键流程和主要状态。
   - C. 验收演示，补齐规则、异常、权限和证据映射。
   - 请回复 A / B / C。
3. After the user chooses, inspect existing prototype files first.
4. Read `SPEC.md` and PRD before UI. If both are missing, recommend `$pm-spec` or `$pm-prd`.
5. Create only the prototype files required by the selected boundary:
   - `product-spec.json` for pages, entities, statuses, fields, actions, permissions, and capability ID mapping
   - `sample-data.json` with realistic business records
   - `copy.zh-CN.json` for visible copy
   - `index.html`, `styles.css`, and `app.js`
6. Verify clickable workflow, responsive layout, and state coverage.

## Rules

- Every meaningful UI element needs stable `data-pm-id`.
- Do not call real APIs.
- Keep demo useful for product review and stakeholder alignment. Do not turn it into a development plan or production implementation.
