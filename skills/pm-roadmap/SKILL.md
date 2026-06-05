---
name: pm-roadmap
description: Create or update ProductForge product strategy, prioritization, and roadmap artifacts. Use for product goals, opportunity ranking, RICE/impact-effort prioritization, roadmap options, scope sequencing, and tradeoff decisions before PRD or project-management planning.
---

# PM Roadmap

Use this for product strategy and prioritization. It turns intake, research, constraints, and business goals into a defensible roadmap without creating development tasks.

## Default Output

```text
.product/PRIORITIZATION.md
.product/ROADMAP.md
```

Default mode is lazy generation. Create only the roadmap artifact(s) needed by the chosen option.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before roadmap work, ask exactly one boundary question with exactly three options:
   - 问题：这次 roadmap 先解决哪类取舍？
   - A. 当前版本范围切分。
   - B. 阶段优先级和顺序。
   - C. 多个战略方向之间的路线选择。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, relevant `00-intake.md`, `01-research.md`, discovery artifacts, and stakeholder constraints. Read `.product/REQUIREMENTS.md`, `.product/DISCOVERY.md`, and `.product/METRICS.md` if present.
4. Clarify the strategy lens: business goal, target segment, time horizon, and success metric.
5. Rank opportunities with a product-friendly method such as RICE, impact-effort, MoSCoW, or strategic fit.
6. Produce only the artifacts needed by the selected option:
   - product goals and non-goals
   - opportunity backlog
   - prioritization matrix
   - roadmap options
   - selected roadmap with rationale
   - explicit tradeoffs and open decisions
7. Update or propose changes to `.product/PRIORITIZATION.md`, `.product/ROADMAP.md`, and `.product/STATE.md` only when they are needed by the chosen boundary.
8. Recommend `$pm-discovery`, `$pm-metrics`, `$pm-define`, `$pm-spec`, or `$pm-plan` based on maturity.

## Boundary

Roadmap items must be product outcomes or decision gates. Do not turn them into engineering tasks, implementation stories, or architecture work.
