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
7. Creation order matters:
   - First create or refresh `spec/product-spec.json`, `data/sample-data.json`, and `data/copy.zh-CN.json`.
   - Then create or refresh `index.html`, `styles.css`, and `app.js`.
   - Only after all six files exist should you do verification or reply to the user.

## Rules

- Every meaningful UI element needs stable `data-pm-id`.
- Do not call real APIs.
- Keep demo useful for product review and stakeholder alignment. Do not turn it into a development plan or production implementation.
- For every boundary, still ship the full six-file prototype pack unless the task explicitly narrows the deliverables.
- If no prototype exists yet, create the full directory structure and all six files in the same turn. Do not stop after only creating the shell or only one or two files.
- `index.html` must reference `styles.css` and `app.js` with stable `data-pm-id` anchors in the rendered shell.
- `styles.css` must include responsive rules with `@media`, and visible layout primitives such as `display`, `grid` or `flex`, plus `background`, `border`, and `padding`.
- `app.js` must render explicit prototype states for `loading`, `empty`, `error`, and `success` or `toast`, even in concept mode. Keep these states lightweight, but make the strings or identifiers visible in the file.
- `copy.zh-CN.json` should always include visible copy for title/description, value expression, search or placeholder text, error/loading/empty states, and success feedback or actions.
- `sample-data.json` should use business-shaped collections such as `records`, `dealers`, `opportunities`, or `items`, and each representative item should carry `id` plus owner/context fields such as `owner`, `region`, `status`, `stage`, `group`, `segment`, `growthLabel`, or `riskLabel` when relevant.
- `product-spec.json` must always include `capabilities`, `pages`, and `entities`, plus at least one structural surface list such as `components` or `regions`, and keep `CAP-` identifiers explicit.
- Boundary-specific minimums:
  - A / 概念演示: keep the prototype focused, but still include search/placeholder copy, concept-state feedback, and a simple `components` or `regions` structure in `product-spec.json`.
  - B / 工作流演示: include the main clickable path, primary state transitions, and the workflow controls that drive the key review path.
  - C / 验收演示: include permissions, exceptions, evidence mapping, and the states that block or unlock acceptance.
- Prefer concise, template-like files over ambitious custom implementations. The prototype only needs enough structure to be reviewable and complete; it does not need dense logic or polish that risks incomplete file creation.
- Your last action in the turn must be the user-facing reply after confirming all six files are present. Do not stop after directory creation, partial patching, or shell scaffolding.
