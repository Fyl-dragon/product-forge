---
name: pf-discovery
description: Run ProductForge continuous discovery for product managers. Use for customer interview synthesis, opportunity-solution trees, assumption mapping, experiment design, evidence collection, and discovery decisions before committing to roadmap, spec, or PRD.
---

# PF Discovery

Use this when the team needs stronger evidence before prioritizing, defining, or specifying a product direction.

## Default Output

```text
.product/DISCOVERY.md
.product/features/<feature-slug>/discovery.md
.product/features/<feature-slug>/opportunity-solution-tree.md
```

## Workflow

1. Read `.product/PRODUCT.md`, `.product/REQUIREMENTS.md`, `.product/PRIORITIZATION.md`, `.product/STATE.md`, relevant intake/research docs, and any existing discovery artifacts.
2. Identify the desired outcome, target customer segment, and current evidence quality.
3. Map:
   - customer opportunities
   - solution ideas
   - assumptions
   - evidence sources
   - experiment or interview plan
4. Separate facts, interview signals, assumptions, and decisions.
5. Save or propose discovery updates and recommend `$pf-roadmap`, `$pf-define`, or `$pf-spec`.

## Opportunity Tree Standard

A valid opportunity tree must make these fields explicit:

- Outcome: the measurable customer or business result, not a feature name.
- Opportunity: a customer problem, unmet need, workflow friction, or decision gap.
- Solution: a possible product direction tied to one opportunity.
- Assumption test: the fastest interview, evidence review, prototype check, or experiment that can reduce uncertainty.
- Evidence quality: classify evidence as observed behavior, interview signal, usage data, market/competitor signal, stakeholder claim, or assumption.
- Decision rule: state what evidence changes the decision, kills the direction, or moves it to `$pf-roadmap`, `$pf-define`, or `$pf-spec`.

## Quality Bar

- Do not jump from stakeholder request to solution.
- Every recommended direction must cite evidence or mark itself as an assumption.
- Discovery experiments must state success signal, evidence needed, owner, and decision rule.
- Do not create engineering tasks or implementation plans.
