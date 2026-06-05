# ProductForge Workspace

`.product/` is the product operating memory for a repo. It does not replace existing `docs/`; it maps and stabilizes product context.

ProductForge now defaults to lean, stage-only generation. Do not scaffold the whole workspace unless the user explicitly asks for it.

## Core Files

- `PRODUCT.md`: product positioning, users, business model, modules.
- `STATE.md`: current status, locked decisions, open issues.
- `config.yaml`: language, rigor, artifact paths, workflow gate defaults, interaction policy, and artifact policy.

## Optional Root Files

Create these only when the workflow reaches the corresponding stage:

- `REQUIREMENTS.md`: requirement backlog and intake history.
- `DISCOVERY.md`: customer opportunities, assumptions, experiments, and evidence quality.
- `PRIORITIZATION.md`: opportunity scoring, product tradeoffs, and priority rationale.
- `METRICS.md`: North Star, input, guardrail, launch, and post-launch metrics.
- `ROADMAP.md`: milestones and current direction.

## Feature Pack

Each feature should live under `.product/features/<feature-slug>/`:

```text
stage files created lazily:
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

Product-side project management artifacts live under `.product/projects/<project-slug>/` and should also be created lazily:

```text
project-plan.md
raid-log.md
stakeholder-update.md
decision-log.md
launch-readiness.md
acceptance-tracker.md
```

Project packs track outcomes, risks, assumptions, issues, dependencies, owners, stakeholder communication, readiness, and acceptance progress. They do not contain development tasks or implementation plans.

## Interaction Rule

Before any stage artifact is written, ProductForge should ask one boundary question with three options and wait for the user's choice. The selected option determines which file is created and how deep the artifact goes.

## Existing Docs Mapping

When a repo already has product docs:

- Do not delete old files.
- Create a feature pack per functional area.
- Add `source-map.md` to record original files.
- Mark current PRD, prototype, project plan, and historical versions.
- If an old file mixes PRD and HTML, mark it as composite draft.
