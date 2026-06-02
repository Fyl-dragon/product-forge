---
name: pf-metrics
description: Create or update ProductForge product metrics. Use for North Star metric design, input metric trees, HEART-style UX metrics, success criteria, guardrail metrics, launch monitoring, and post-launch review plans.
---

# PF Metrics

Use this when product decisions need measurable success criteria or when launch/project management needs monitoring.

## Default Output

```text
.product/METRICS.md
.product/features/<feature-slug>/metrics.md
```

## Workflow

1. Read `.product/PRODUCT.md`, `.product/PRIORITIZATION.md`, `.product/ROADMAP.md`, `.product/STATE.md`, relevant `SPEC.md`, PRD, acceptance, and project artifacts.
2. Define the metric model:
   - North Star metric
   - input metrics
   - guardrail metrics
   - UX or journey metrics
   - launch and adoption metrics
3. Tie metrics to customer value, business goal, capability IDs, and post-launch decisions.
4. Define baseline, target, measurement source, review cadence, and owner.
5. Recommend `$pf-roadmap`, `$pf-accept`, `$pf-project`, or `$pf-retro` based on the metric gap.

## Metric Quality Standard

Every metric model must include:

- North Star: the durable value metric that links user value and business value.
- Input metrics: controllable leading indicators that can move the North Star.
- Guardrails: risk indicators that prevent growth from masking quality, trust, cost, compliance, or operational damage.
- Baseline: current value or explicit "unknown" with the source needed to establish it.
- Target: launch, milestone, or post-launch target with time horizon.
- Owner: accountable person or function for review and action.
- Review cadence: when metrics are reviewed and what decision will be made from the review.

## Boundary

Metrics define product decisions and operating reviews. Do not specify instrumentation code, analytics implementation tasks, or data engineering work.
