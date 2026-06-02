# Product Prototype Demo Standard

The default prototype is a product-management demonstration asset, not a production app and not a development-stage artifact.

## Shape

```text
prototype/
  index.html
  styles.css
  app.js
  data/
    sample-data.json
    copy.zh-CN.json
  spec/
    product-spec.json
```

## Responsibilities

- `index.html`: shell, root container, script/style loading.
- `styles.css`: design tokens, layout, components, responsive rules, state styles.
- `app.js`: local routing, rendering, filtering, modal behavior, state transitions, mock interactions.
- `data/sample-data.json`: realistic business records.
- `data/copy.zh-CN.json`: visible UI copy and PM-editable wording.
- `spec/product-spec.json`: capabilities, pages, components, entities, fields, statuses, actions, permissions.

## Required Demo Behavior

- At least one primary workflow must be clickable.
- Include visible feedback for success, disabled, loading, empty, and error states.
- Include filters/search when the product surface is operational or B-end.
- Use realistic sample data with IDs, names, statuses, owners, times, amounts, and risk labels.
- Use stable `data-pm-id` on meaningful UI elements.
- Map important UI regions and actions to `SPEC.md` capability IDs when possible.
- Do not call real APIs.
- Do not hard-code business data in `app.js` if it belongs in JSON.
- Do not turn the demo into production code, architecture, engineering tasks, or test code.

## Modification Protocol

When changing an existing demo:

1. Inspect current files first.
2. Keep existing `data-pm-id` stable unless the surface is renamed.
3. Update `copy.zh-CN.json` for text changes.
4. Update `sample-data.json` for business data changes.
5. Update `product-spec.json` for fields, statuses, actions, or page changes.
6. Touch `app.js` only for behavior or rendering changes.
7. Touch `styles.css` only for visual system or layout changes.

Preferred user references:

```text
修改 data-pm-id="price.table.discount" 的显示规则。
在 page id "source-routing" 增加一个 "客户探测风险" tab。
给 entity "tenantRoutePolicy" 增加字段 "source_stickiness"。
```
