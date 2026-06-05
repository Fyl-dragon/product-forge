---
name: pm-metrics
description: Create or update ProductForge product metrics. Use for North Star metric design, input metric trees, HEART-style UX metrics, success criteria, guardrail metrics, launch monitoring, and post-launch review plans.
---

# PM Metrics

Use this when product decisions need measurable success criteria or when launch/project management needs monitoring.

## Default Output

```text
.product/METRICS.md
.product/features/<feature-slug>/metrics.md
```

Default mode is lazy generation. Create only the metric artifact(s) needed by the chosen option.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before metric design, ask exactly one boundary question with exactly three options:
   - 问题：这次指标先服务哪类决策？
   - A. 先定义成功指标，判断值不值得做。
   - B. 先定义上线门禁，判断能不能发。
   - C. 先建完整指标体系，支持后续持续复盘。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, relevant `SPEC.md`, PRD, acceptance, and project artifacts. Read `.product/ROADMAP.md` and `.product/PRIORITIZATION.md` if present.
4. Define the metric model:
   - North Star metric
   - input metrics
   - guardrail metrics
   - UX or journey metrics
   - launch and adoption metrics
5. Tie metrics to customer value, business goal, capability IDs, and post-launch decisions.
6. Define baseline, target, measurement source, review cadence, and owner.
7. Recommend `$pm-roadmap`, `$pm-accept`, `$pm-project`, or `$pm-retro` based on the metric gap.

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

## Stage Control and Minimal Deliverable Rules

- **If the user has not selected A / B / C yet:** reply with **only** the prescribed boundary question and wait. Do **not** generate metrics, summarize a plan, or write any files.
- **If the user already selected A / B / C in the conversation:** do **not** ask the boundary question again. Continue directly with the current-stage minimal deliverable.
- **Lazy generation by option:**
  - **A. 成功指标** → usually update only `.product/features/<feature-slug>/metrics.md`.
  - **B. 上线门禁** → usually update only `.product/features/<feature-slug>/metrics.md`.
  - **C. 完整指标体系** → update `.product/METRICS.md` and the current feature metrics file when both are needed for the system-level + feature-level view.
- Never create extra planning, tracking, or state files unless the current stage explicitly requires them.
- Before writing, ground the metric design in the local product context: product/state/spec/PRD/acceptance/project artifacts, plus roadmap/prioritization if present.
- In every written metrics artifact, make the model explicitly decision-oriented and include, where applicable to the chosen option: customer value link, business value link, linked capability IDs, baseline, target or threshold, source, owner, review cadence, and decision rule / launch gate.
- For **option C**, `.product/METRICS.md` must begin with a short **feature-specific context block** rather than a generic product-only metrics frame. Reuse the user's feature nouns and scope terms directly in that top-level artifact, including:
  - the current feature or problem name,
  - the current rollout scope / pilot / region / segment when present,
  - why a **完整指标体系** or continuous review system is needed now.
- For **option C**, the top-level `.product/METRICS.md` should explicitly restate the feature context in the artifact body so that system-level metrics remain visibly grounded in the current feature, not only in the feature-local metrics file.
- In the final reply, briefly confirm the exact artifact path(s) written, note that only the current-stage minimal deliverable was produced, and recommend exactly one next `pm-*` command.

<!-- SLOW_UPDATE_START -->
Protect the stage boundary strictly. If the user has not chosen A / B / C yet, reply with only the exact prescribed boundary question and nothing else. Do not add greetings, explanations, plans, file mentions, or metric content.

If the user already chose A / B / C anywhere in the conversation, never ask the boundary question again. Proceed directly to the deliverable for that option.

Keep output minimal by option:
- For A, usually write only `.product/features/<feature-slug>/metrics.md`.
- For B, usually write only `.product/features/<feature-slug>/metrics.md`.
- For C, write `.product/METRICS.md` and the current feature metrics file only when both are needed.
Do not create extra docs, plans, trackers, or state artifacts unless the current stage explicitly requires them.

Before writing metrics, ground them in the local product artifacts required by the skill. Use the product context to make the metrics decision-oriented rather than generic.

In every metrics artifact you write, include the elements needed for the chosen option: customer value link, business value link, linked capability IDs when available, baseline or explicit unknown, target or launch threshold, source, owner, review cadence, and a decision rule or launch gate.

For option C specifically:
- Make `.product/METRICS.md` start with a short feature-specific context block or section that repeats the user's current feature nouns and scope terms.
- If the user request or local product files mention pilot scope, region, segment, or rollout context, repeat that explicitly in `.product/METRICS.md`.
- Make the top-level metrics doc say why a full metrics system / 持续复盘 / 完整指标体系 is needed now, so the system-level artifact is visibly tied to this feature.

In your final reply after writing files, be brief and concrete: state the exact artifact path(s) written, explicitly say that only the current-stage minimal deliverable was produced, and recommend exactly one next `pm-*` command.

Do not drift into instrumentation design, analytics implementation tasks, or data engineering work.
<!-- SLOW_UPDATE_END -->
