---
name: pf-narrative
description: Create ProductForge customer-backward product narratives such as PRFAQ, launch narrative, customer FAQ, and internal alignment memo. Use before PRD, roadmap decisions, executive review, or stakeholder alignment.
---

# PF Narrative

Use this for Working Backwards-style product clarity. It forces the product idea to be explained from the customer and stakeholder perspective before deeper specification.

## Default Output

```text
.product/features/<feature-slug>/PRFAQ.md
.product/features/<feature-slug>/narrative.md
```

## Workflow

1. Read `.product/PRODUCT.md`, discovery, research, roadmap, `SPEC.md`, and PRD if available.
2. Write or update:
   - customer problem
   - launch-day press release
   - customer FAQ
   - internal FAQ
   - risks and constraints
   - rejected alternatives
   - open questions
3. Use plain customer language. Avoid internal jargon unless it belongs in internal FAQ.
4. If major gaps remain, route to `$pf-discovery`, `$pf-metrics`, or `$pf-roadmap` before PRD.

## PRFAQ Quality Standard

A complete PRFAQ must contain:

- Press release: launch-day customer value, target customer, problem solved, and proof point.
- Customer FAQ: customer-facing questions about who it is for, how it works, limits, pricing/availability when relevant, and migration or support impact.
- Internal FAQ: business model, operations, support, policy, risk, dependency, metric, and rollout questions.
- Risks: product, commercial, operational, trust, compliance, and adoption risks.
- Rejected alternatives: credible options that were considered and why they were not selected.
- Open questions: unresolved decisions with owner, next evidence, and decision deadline.

## Boundary

The narrative clarifies customer value and alignment. Do not turn it into implementation design, architecture, or delivery tickets.
