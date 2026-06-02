---
name: pf-roadmap
description: Create or update ProductForge product strategy, prioritization, and roadmap artifacts. Use for product goals, opportunity ranking, RICE/impact-effort prioritization, roadmap options, scope sequencing, and tradeoff decisions before PRD or project-management planning.
---

# PF Roadmap

Use this for product strategy and prioritization. It turns intake, research, constraints, and business goals into a defensible roadmap without creating development tasks.

## Default Output

```text
.product/PRIORITIZATION.md
.product/ROADMAP.md
```

## Workflow

1. Read `.product/PRODUCT.md`, `.product/REQUIREMENTS.md`, `.product/DISCOVERY.md`, `.product/METRICS.md`, `.product/STATE.md`, relevant `00-intake.md`, `01-research.md`, discovery artifacts, and stakeholder constraints.
2. Clarify the strategy lens: business goal, target segment, time horizon, and success metric.
3. Rank opportunities with a product-friendly method such as RICE, impact-effort, MoSCoW, or strategic fit.
4. Produce:
   - product goals and non-goals
   - opportunity backlog
   - prioritization matrix
   - roadmap options
   - selected roadmap with rationale
   - explicit tradeoffs and open decisions
5. Update or propose changes to `.product/PRIORITIZATION.md`, `.product/ROADMAP.md`, and `.product/STATE.md`.
6. Recommend `$pf-discovery`, `$pf-metrics`, `$pf-define`, `$pf-spec`, or `$pf-plan` based on maturity.

## Boundary

Roadmap items must be product outcomes or decision gates. Do not turn them into engineering tasks, implementation stories, or architecture work.
