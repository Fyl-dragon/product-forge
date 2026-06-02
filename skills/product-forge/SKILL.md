---
name: product-forge
description: ProductForge PM Operating System for professional product managers. Use when Codex should guide product-management through project-management workflows: requirement analysis, research, product spec kernels, PRDs, product prototype demos, release planning, project coordination, reviews, acceptance, and retrospectives through pf-* skills with a persistent .product workspace and Codex-installable skill pack.
---

# ProductForge

Use ProductForge as the entrypoint for a professional product AI operating framework. It mirrors the useful parts of GSD and BMAD, but stops at the product/project management boundary: intake, research, feature definition, spec kernel, PRD, product prototype demo, release plan, project coordination, review, acceptance, and retrospective.

Default language: Chinese for product outputs. Keep JSON keys, directory names, and stable identifiers in English.

## Core Model

Product work is managed as persistent context under `.product/`:

```text
.product/
  PRODUCT.md
  REQUIREMENTS.md
  DISCOVERY.md
  PRIORITIZATION.md
  METRICS.md
  ROADMAP.md
  STATE.md
  config.yaml
  features/<feature-slug>/
    00-intake.md
    01-research.md
    discovery.md
    opportunity-solution-tree.md
    02-define.md
    SPEC.md
    PRFAQ.md
    docs/prd.md
    metrics.md
    prototype/
      index.html
      styles.css
      app.js
      data/sample-data.json
      data/copy.zh-CN.json
      spec/product-spec.json
    acceptance.md
    review.md
    decision-log.md
    versions/
  projects/<project-slug>/
    project-plan.md
    raid-log.md
    stakeholder-update.md
    decision-log.md
    launch-readiness.md
    acceptance-tracker.md
  references/
```

## Workflow Routing

Use these command skills when the user mentions them:

- `$pf-help`: recommend the next ProductForge command.
- `$pf-init`: initialize `.product/` for a product or repo.
- `$pf-intake`: turn rough ideas, notes, or meetings into structured intake.
- `$pf-discovery`: run continuous discovery, opportunity mapping, and assumption testing.
- `$pf-research`: competitor, market, user, and opportunity analysis.
- `$pf-roadmap`: prioritize opportunities and maintain product strategy and roadmap.
- `$pf-metrics`: define North Star, input, guardrail, launch, and UX metrics.
- `$pf-narrative`: create customer-backward PRFAQ or launch narrative.
- `$pf-define`: define feature scope, entities, workflow, states, permissions, and rules.
- `$pf-spec`: create or update the product spec kernel.
- `$pf-prd`: create or update `.product/features/<feature-slug>/docs/prd.md`.
- `$pf-prototype`: create a lightweight multi-file prototype demo.
- `$pf-plan`: create milestones, dependency map, delivery plan, and launch checklist.
- `$pf-project`: manage milestones, RAID log, stakeholder updates, launch readiness, and acceptance progress.
- `$pf-review`: review PRD/prototype/demo for PM quality and product risk.
- `$pf-accept`: create acceptance criteria, UAT cases, rollout gates, and evidence standards.
- `$pf-retro`: capture decisions, lessons, follow-ups, and product memory.

If the user asks broadly, choose the smallest workflow that completes the request. If the request involves LLM aggregation platforms, model routing, cloud vendors, model pricing, suppliers, channels, CRM/RPM, settlement, or resource pools, also read `pm-llm-platform`.

## Stage Gates

- `$pf-prd` expects `SPEC.md` unless the user explicitly asks for fast path.
- `$pf-prototype` expects `SPEC.md` or PRD context and only produces product demonstration assets.
- `$pf-project` coordinates product/project management readiness and does not create engineering execution tasks.
- `$pf-roadmap` ranks product opportunities and does not create engineering execution tasks.
- `$pf-discovery` must record evidence quality before recommending a direction.
- `$pf-metrics` must connect success signals to customer value and business outcomes.
- `$pf-narrative` must expose customer-facing value, FAQ gaps, and stakeholder risks before PRD or executive review.
- `$pf-review` returns findings first, ordered P0-P3.
- `$pf-accept` must tie scenarios back to capability IDs, business rules, permissions, state transitions, prototype demo coverage, rollout gates, and evidence.

## Boundary

ProductForge covers product management and product-side project management. It must not generate architecture plans, engineering tickets, implementation stories, production code, test code, code review output, or developer execution plans. If the user needs that, stop at a product handoff summary.

## Artifact Rules

- PRDs are Markdown unless the user asks otherwise.
- Prototype demos are PM-owned demonstration assets by default, not production software.
- Single-file HTML is allowed only for disposable demos and must be labeled disposable.
- Keep visible UI copy in `copy.zh-CN.json` where practical.
- Keep mock business data in `sample-data.json`.
- Keep pages, entities, statuses, actions, and permissions in `product-spec.json`.
- Every important page region, table, filter, form, modal, tab, and action button must have stable `data-pm-id`.
- Do not invent production APIs or engineering implementation details for prototypes. Mock behavior must stay local and explicit.
- Capability IDs in `SPEC.md` are stable (`CAP-1`, `CAP-2`, ...). PRD, prototype spec, review, and acceptance artifacts should reference them.

## Product Quality Bar

Every substantial output should make these explicit:

- problem and target user
- goal, non-goal, and success metric
- core scenario and workflow
- entities, fields, statuses, permissions, and actions
- business rules and constraints
- empty, loading, error, disabled, and success states
- acceptance criteria and open questions
- project milestones, risks, dependencies, stakeholder updates, and launch readiness when the work is in project-management mode
- product strategy, prioritization rationale, roadmap options, and tradeoffs when the work is in roadmap mode
- discovery evidence, assumptions, experiments, and decision rules when the work is in discovery mode
- North Star, input, guardrail, UX, launch, and post-launch metrics when the work is in metrics mode
- customer-backward narrative, PRFAQ, and internal FAQ when the work is in narrative mode

## References

- Read `references/methodology.md` for the full PM framework.
- Read `references/prototype-demo.md` before generating or modifying prototype demos.
- Read `references/review-checklist.md` before reviewing PRDs or prototypes.
- Read `references/project-workspace.md` before initializing or validating `.product/`.
- Read `references/method-library.md` when verifying whether ProductForge covers mature PM methods.
- Read `references/domain-packages.md` when a workflow needs vertical domain knowledge such as `pm-llm-platform`.
- Read `references/usage-guide.md` when the user asks how to use ProductForge or wants a GSD/BMAD-like manual.
