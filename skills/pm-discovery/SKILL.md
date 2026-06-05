---
name: pm-discovery
description: Run ProductForge continuous discovery for product managers. Use for customer interview synthesis, opportunity-solution trees, assumption mapping, experiment design, evidence collection, and discovery decisions before committing to roadmap, spec, or PRD.
---

# PM Discovery

Use this when the team needs stronger evidence before prioritizing, defining, or specifying a product direction.

## Default Output

```text
.product/DISCOVERY.md
.product/features/<feature-slug>/discovery.md
.product/features/<feature-slug>/opportunity-solution-tree.md
```

Default mode is lazy generation. Only create the discovery artifacts required by the selected boundary.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before discovery work, ask exactly one boundary question with exactly three options:
   - 问题：这轮 discovery 先降低哪类不确定性？
   - A. 客户机会是否真实存在。
   - B. 方案方向是否值得继续推进。
   - C. 证据质量是否足以进入 roadmap/spec。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, relevant intake/research docs, and any existing discovery artifacts. Read `.product/REQUIREMENTS.md` and `.product/PRIORITIZATION.md` if present.
4. Identify the desired outcome, target customer segment, and current evidence quality.
5. Map:
   - customer opportunities
   - solution ideas
   - assumptions
   - evidence sources
   - experiment or interview plan
6. Separate facts, interview signals, assumptions, and decisions.
7. Save or propose only the discovery artifacts required by the selected option, then recommend `$pm-roadmap`, `$pm-define`, or `$pm-spec`.

## Opportunity Tree Standard

A valid opportunity tree must make these fields explicit:

- Outcome: the measurable customer or business result, not a feature name.
- Opportunity: a customer problem, unmet need, workflow friction, or decision gap.
- Solution: a possible product direction tied to one opportunity.
- Assumption test: the fastest interview, evidence review, prototype check, or experiment that can reduce uncertainty.
- Evidence quality: classify evidence as observed behavior, interview signal, usage data, market/competitor signal, stakeholder claim, or assumption.
- Decision rule: state what evidence changes the decision, kills the direction, or moves it to `$pm-roadmap`, `$pm-define`, or `$pm-spec`.

## Quality Bar

- Do not jump from stakeholder request to solution.
- Every recommended direction must cite evidence or mark itself as an assumption.
- Discovery experiments must state success signal, evidence needed, owner, and decision rule.
- Do not create engineering tasks or implementation plans.
