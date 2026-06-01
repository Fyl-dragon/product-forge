# Product Workspace

`.product/` is the product operating memory for a repo. It does not replace existing `docs/`; it maps and stabilizes product context.

## Required Files

- `PRODUCT.md`: product positioning, users, business model, modules.
- `REQUIREMENTS.md`: requirement backlog and intake history.
- `ROADMAP.md`: milestones and current direction.
- `STATE.md`: current status, locked decisions, open issues.

## Feature Pack

Each feature should live under `.product/features/<feature-slug>/`:

```text
docs/prd.md
prototype/index.html
prototype/styles.css
prototype/app.js
prototype/data/sample-data.json
prototype/data/copy.zh-CN.json
prototype/spec/product-spec.json
research.md
acceptance.md
versions/
```

## Existing Docs Mapping

When a repo already has product docs:

- Do not delete old files.
- Create a feature pack per functional area.
- Add `source-map.md` to record original files.
- Mark current PRD, prototype, architecture, and historical versions.
- If an old file mixes PRD and HTML, mark it as composite draft.

