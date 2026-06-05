---
name: pm-prd
description: Write or update ProductForge PRDs for feature packs. Use for Markdown PRDs grounded in SPEC.md with goals, scenarios, requirements, business rules, data model, permissions, states, acceptance criteria, risks, and open questions.
---

# PM PRD

Default target: `.product/features/<feature-slug>/docs/prd.md`.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before PRD writing, ask exactly one boundary question with exactly three options:
   - 问题：这次 PRD 要写到什么用途？
   - A. 决策摘要版，只支撑范围评审。
   - B. 标准 PRD，支撑原型、评审和验收。
   - C. 深度 PRD，额外展开异常、状态和运营细节。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, `SPEC.md`, companion files, `00-intake.md`, discovery artifacts, `01-research.md`, `PRFAQ.md`, `metrics.md`, `02-define.md`, and source docs.
4. If the domain is LLM aggregation, read `pm-llm-platform`.
5. If `SPEC.md` is missing, stop and recommend `$pm-spec` unless the user explicitly asks for fast path.
6. Write only `.product/features/<feature-slug>/docs/prd.md` in Chinese with:
   - 背景与问题
   - 目标与非目标
   - 用户与场景
   - 功能范围
   - capability ID traceability
   - 业务规则
   - 数据对象与字段
   - 权限与角色
   - 状态流转
   - 页面/交互要求
   - 异常与边界
   - 验收标准
   - 指标与上线后观察
   - 风险与待确认
7. Preserve assumptions explicitly and append meaningful decisions to `decision-log.md`.

## Rule

PRD must be specific enough to support product review, prototype demo, project planning, and acceptance cases.

## Decision Binding Rules

- Do not only spread source nouns across many sections. For each boundary, add at least one line that keeps the actor, the governed object, and the decision or outcome in the same bullet, paragraph, or table row.
- Prefer short binding lines over decorative prose. If a source workflow is central, restate it once in compact form before expanding details elsewhere.

### A. 决策摘要版

- The first summary block should explicitly state that the PRD only serves `范围评审` and what is deliberately left out.
- If the source names a stakeholder who is part of the alignment audience, such as `培训主管`, `产品经理`, `采购运营负责人`, or similar, bind that stakeholder with `范围评审` and at least one `非目标` item in the same line or bullet.
- When a scope decision is still pending, keep the scoped noun and the defer phrase together, such as `暂不进入`, `不在本阶段`, or `本版不决定`.

### B. 标准 PRD

- Add at least one rule or scenario line that binds the primary role, the controlled object, and the review/acceptance consequence in the same line.
  - Example shape: `发布经理 + 阻塞项 + 门禁 + 证据 + 是否可放行`
  - Example shape: `销售 + 审批人 + 折扣申请 + 卡点`
- When the source includes a gated blocker like `影响放行`, keep that blocker and the allowed/blocked outcomes together in one rule line instead of separating them into different sections.
- If an open question contains a concrete business noun such as `临时授权审批`, repeat that noun once in `风险与待确认` or `非目标` together with its pending status, rather than only mentioning a generic "待确认事项".

### C. 深度 PRD

- For prioritized operational workflows, bind the core object, action, and prioritization cue together in one line.
  - Example shape: `高风险客户 + 建议动作 + 优先级`
- For exception-heavy domains, add a compact exception row or bullet that keeps multiple source exception terms together before expanding handling details.
  - Example shape: `证据不足 / 客户价值缺失 / 任务超时`
- When the source mentions fallback, degradation, rollback, or manual takeover, keep the trigger and the fallback path together in the same line.

### Cross-cutting

- If a section uses a table, use it to preserve binding, not to split the chain further. A good row keeps role/object/status/evidence or role/object/decision together.
- When a metric or acceptance statement is directly tied to a business role or scenario, prefer writing them in one line rather than putting the role in one section and the metric meaning in another.
