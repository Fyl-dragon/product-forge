---
name: pm-narrative
description: Create ProductForge customer-backward product narratives such as PRFAQ, launch narrative, customer FAQ, and internal alignment memo. Use before PRD, roadmap decisions, executive review, or stakeholder alignment.
---

# PM Narrative

Use this for Working Backwards-style product clarity. It forces the product idea to be explained from the customer and stakeholder perspective before deeper specification.

## Default Output

```text
.product/features/<feature-slug>/PRFAQ.md
.product/features/<feature-slug>/narrative.md
```

Default mode is lazy generation. Create only the narrative artifact(s) needed by the chosen option.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before narrative work, ask exactly one boundary question with exactly three options:
   - 问题：这次 narrative 先对齐哪类对象？
   - A. 客户价值，先验证用户是否买单。
   - B. 内部共识，先验证业务和运营是否认同。
   - C. 上线质疑，先处理风险、反对意见和未决问题。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, discovery, research, roadmap, `SPEC.md`, and PRD if available.
4. Write or update only the narrative artifact(s) needed by the selected option:
   - customer problem
   - launch-day press release
   - customer FAQ
   - internal FAQ
   - risks and constraints
   - rejected alternatives
   - open questions
5. Use plain customer language. Avoid internal jargon unless it belongs in internal FAQ.
6. If major gaps remain, route to `$pm-discovery`, `$pm-metrics`, or `$pm-roadmap` before PRD.

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
