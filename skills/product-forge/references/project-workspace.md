# ProductForge Workspace

`.product/` is the product operating memory for a repo. It does not replace existing `docs/`; it maps and stabilizes product context.

## Required Files

- `PRODUCT.md`: product positioning, users, business model, modules.
- `REQUIREMENTS.md`: requirement backlog and intake history.
- `DISCOVERY.md`: customer opportunities, assumptions, experiments, and evidence quality.
- `PRIORITIZATION.md`: opportunity scoring, product tradeoffs, and priority rationale.
- `METRICS.md`: North Star, input, guardrail, launch, and post-launch metrics.
- `ROADMAP.md`: milestones and current direction.
- `STATE.md`: current status, locked decisions, open issues.
- `config.yaml`: language, rigor, artifact paths, and workflow gate defaults.

## Feature Pack

Each feature should live under `.product/features/<feature-slug>/`:

```text
00-intake.md
discovery.md
opportunity-solution-tree.md
01-research.md
02-define.md
SPEC.md
PRFAQ.md
docs/prd.md
metrics.md
prototype/index.html
prototype/styles.css
prototype/app.js
prototype/data/sample-data.json
prototype/data/copy.zh-CN.json
prototype/spec/product-spec.json
acceptance.md
review.md
decision-log.md
versions/
```

`SPEC.md` is the machine contract. PRD, prototype, review, and acceptance artifacts should reference stable capability IDs such as `CAP-1`.

## Project Pack

Product-side project management artifacts live under `.product/projects/<project-slug>/`:

```text
project-plan.md
raid-log.md
stakeholder-update.md
decision-log.md
launch-readiness.md
acceptance-tracker.md
```

Project packs track outcomes, risks, assumptions, issues, dependencies, owners, stakeholder communication, readiness, and acceptance progress. They do not contain development tasks or implementation plans.

## Existing Docs Mapping

When a repo already has product docs:

- Do not delete old files.
- Create a feature pack per functional area.
- Add `source-map.md` to record original files.
- Mark current PRD, prototype, project plan, and historical versions.
- If an old file mixes PRD and HTML, mark it as composite draft.
