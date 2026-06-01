---
name: product-gsd
description: Product manager AI workflow framework for product discovery, requirement intake, competitor research, PRD writing, prototype demos, release planning, product review, acceptance, and retrospectives. Use when Codex should operate like a professional PM system with a persistent .product workspace, GSD-style command workflows, structured product context, and multi-file HTML/CSS/JS prototype demos. For LLM aggregation platform work, combine with pm-llm-platform as the domain package.
---

# Product GSD

Use this skill as the entrypoint for a product-manager-focused AI development framework. It mirrors the useful parts of engineering GSD workflows, but optimizes for product work: discovery, requirements, research, PRD, prototype demo, project planning, review, acceptance, and retrospective.

Default language: Chinese for product outputs. Keep code, JSON keys, directory names, and stable identifiers in English.

## Core Model

Product work is managed as persistent context under `.product/`:

```text
.product/
  PRODUCT.md
  REQUIREMENTS.md
  ROADMAP.md
  STATE.md
  features/<feature-slug>/
    docs/prd.md
    prototype/
      index.html
      styles.css
      app.js
      data/sample-data.json
      data/copy.zh-CN.json
      spec/product-spec.json
    research.md
    acceptance.md
    versions/
  references/
```

## Workflow Routing

Use these command skills when the user mentions them:

- `$pgd-new-product`: initialize `.product/` for a product or repo.
- `$pgd-intake`: turn rough ideas, notes, or meetings into structured requirements.
- `$pgd-research`: competitor, market, user, and opportunity analysis.
- `$pgd-define-feature`: define feature scope, entities, workflow, states, permissions, and rules.
- `$pgd-write-prd`: create or update `.product/features/<feature-slug>/docs/prd.md`.
- `$pgd-prototype`: create a lightweight multi-file prototype demo.
- `$pgd-plan-release`: create milestones, dependency map, delivery plan, and launch checklist.
- `$pgd-review`: review PRD/prototype/demo for PM quality and product risk.
- `$pgd-acceptance`: create acceptance criteria, UAT cases, and rollout standards.
- `$pgd-retro`: capture decisions, lessons, follow-ups, and product memory.

If the user asks broadly, choose the smallest workflow that completes the request. If the request involves LLM aggregation platforms, model routing, cloud vendors, model pricing, suppliers, channels, CRM/RPM, settlement, or resource pools, also read `pm-llm-platform`.

## Artifact Rules

- PRDs are Markdown unless the user asks otherwise.
- Prototype demos are multi-file HTML/CSS/JS by default, not single-file HTML.
- Single-file HTML is allowed only for disposable demos and must be labeled disposable.
- Keep visible UI copy in `copy.zh-CN.json` where practical.
- Keep mock business data in `sample-data.json`.
- Keep pages, entities, statuses, actions, and permissions in `product-spec.json`.
- Every important page region, table, filter, form, modal, tab, and action button must have stable `data-pm-id`.
- Do not invent production APIs for prototypes. Mock behavior must stay local and explicit.

## Product Quality Bar

Every substantial output should make these explicit:

- problem and target user
- goal, non-goal, and success metric
- core scenario and workflow
- entities, fields, statuses, permissions, and actions
- business rules and constraints
- empty, loading, error, disabled, and success states
- acceptance criteria and open questions

## References

- Read `references/methodology.md` for the full PM framework.
- Read `references/prototype-demo.md` before generating or modifying prototype demos.
- Read `references/review-checklist.md` before reviewing PRDs or prototypes.
- Read `references/project-workspace.md` before initializing or validating `.product/`.
- Read `references/domain-packages.md` when a workflow needs vertical domain knowledge such as `pm-llm-platform`.
- Read `references/usage-guide.md` when the user asks how to use PGD or wants a GSD-like manual.
