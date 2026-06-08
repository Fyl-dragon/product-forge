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
2. Before any narrative work, ask exactly one boundary question using this exact Chinese structure and exactly three options:
   - 问题：这次 narrative 先对齐哪类对象？
   - A. 客户价值，先验证用户是否买单。
   - B. 内部共识，先验证业务和运营是否认同。
   - C. 上线质疑，先处理风险、反对意见和未决问题。
   - 请回复 A / B / C。
3. Immediately stop after asking the boundary question and wait for the user's choice. Do not draft narrative content, do not add extra explanation, and do not create or update any files before A / B / C is selected.
4. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, and `.product/config.yaml` in addition to any available discovery, research, roadmap, `SPEC.md`, and PRD.

### Execution Rules

- If the conversation already includes a valid A / B / C selection, **do not ask the boundary question again**.
- Ground the narrative in the actual product context from those files: feature goal, target user or buyer, problem context, constraints, dependencies, proof points, support or rollout impact, and unresolved decisions.
- Prefer concrete statements over generic PM language. If evidence is missing, state the gap explicitly in Risks or Open Questions instead of inventing details.
- Keep writes minimal. Do not create both `PRFAQ.md` and `narrative.md` unless the selected option requires both.
- In the final user reply, report only the file(s) changed and end with exactly one recommended next command chosen from: `$pm-discovery`, `$pm-metrics`, `$pm-roadmap`, `$pm-spec`.

5. Write or update only the minimal artifact(s) required by the selected option.
   - If user selected **A 客户价值**: write `.product/features/<feature-slug>/PRFAQ.md` only.
     Required sections in that file:
     - Press Release / 发布稿 / 新闻稿
     - Customer FAQ / 客户 FAQ
     - Internal FAQ / 内部 FAQ
     - Risks / 风险
     - Rejected Alternatives / 备选方案
     - Open Questions / 未决问题
     Additional wording requirements for option A:
     - Explicitly label the target customer with a phrase such as `目标客户` or `适用对象`; do not rely only on a generic heading like `适合谁用`.
     - Explicitly label customer value with `客户价值` or an equivalent phrase like `价值在哪里`.
     - Explicitly label workflow explanation with `如何使用`, `如何工作`, or `具体怎么工作`.
     - Explicitly label the current scope limit with `当前边界`, `限制`, or `边界`.
     - Explicitly label proof or evidence with `直接证据`, `现有证据`, `证据缺口`, or `试点场景`.
     - Explicitly mention support or migration impact with phrases like `支持团队`, `运营和支持团队`, `支持影响`, or `迁移`.
   - If user selected **B 内部共识**: write `.product/features/<feature-slug>/narrative.md` only.
     Required sections in that file:
     - Alignment Goal / 对齐目标
     - Business Value / 业务价值
     - Operational Readiness / 运营准备
     - Stakeholder Concerns / 干系人关注
     - Dependencies / 依赖
     - Decision Needed / 待决策
   - If user selected **C 上线质疑**: write both `.product/features/<feature-slug>/PRFAQ.md` and `.product/features/<feature-slug>/narrative.md`.
     - `PRFAQ.md` must contain:
       - Internal FAQ / 内部 FAQ
       - Risks / 风险
       - Rejected Alternatives / 备选方案
       - Open Questions / 未决问题
     - `narrative.md` must summarize launch objections, mitigations, owners, next evidence, and launch-readiness framing.
   - Do not create any other feature artifact unless the interaction protocol explicitly requires it.
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
