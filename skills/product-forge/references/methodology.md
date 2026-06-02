# ProductForge Methodology

ProductForge covers product management through product-side project management. It does not cover development execution.

## Operating Loop

1. Intake: clarify source, stakeholder, urgency, target user, and business goal.
2. Diagnose: separate problem, symptom, proposed solution, and measurable outcome.
3. Discovery: map customer opportunities, assumptions, experiments, and evidence quality.
4. Research: inspect competitors, alternatives, internal docs, user scenarios, and constraints.
5. Roadmap: prioritize opportunities, sequence scope, and record tradeoffs.
6. Metrics: define North Star, input, guardrail, UX, launch, and post-launch review metrics.
7. Narrative: write customer-backward PRFAQ or launch narrative to align stakeholders.
8. Define: lock scope, non-goals, entities, fields, states, permissions, and business rules.
9. Spec: create `SPEC.md` with stable capabilities, constraints, non-goals, success signals, and companions.
10. PRD: expand the spec into stakeholder-readable requirements.
11. Demonstrate: build a product prototype demo with realistic data and local interactions.
12. Plan: split release milestones, dependencies, risks, and launch checks.
13. Project: manage RAID, stakeholder updates, decision logs, launch readiness, and acceptance progress.
14. Review: audit product logic, business risk, edge states, project-management ambiguity, and acceptance gaps.
15. Accept: create UAT scenarios and evidence requirements.
16. Retro: record decisions, lessons, follow-ups, and context that future work must preserve.

## Requirement Analysis

Always distinguish:

- user problem vs stakeholder request
- confirmed facts vs inferred assumptions
- must-have vs tradeoff vs future idea
- user-facing behavior vs internal operation
- policy/rule vs UI display
- one-time feature vs reusable platform capability

Minimum requirement output:

- 背景
- 目标用户
- 核心场景
- 问题定义
- 成功指标
- 范围内
- 范围外
- 业务规则
- 数据对象
- 状态流转
- 权限
- 异常与边界
- 验收标准
- 待确认问题

## Product Spec Kernel

`SPEC.md` is the downstream contract. It should include:

- problem
- users/jobs
- capabilities with stable IDs and success signals
- constraints
- non-goals
- business rules
- states
- assumptions
- open questions
- companions

Move bulky matrices into companion files such as `entities.md`, `permissions.md`, `state-machine.md`, or `business-rules.md`.

## Competitor Research

Do not produce generic competitor summaries. Convert research into product decisions.

Useful comparison axes:

- target segment
- core workflow
- information architecture
- pricing and packaging
- permission model
- onboarding path
- operational console
- data visibility
- integration model
- differentiators and weaknesses

Output should include:

- 竞品/替代方案清单
- 对比矩阵
- 可借鉴点
- 不应照搬点
- 对当前产品的设计启发
- 对 PRD 或原型的直接影响

## Project Management

PM planning should connect product scope to delivery:

- milestone and phase goals
- dependency map
- decision log
- risk log
- acceptance owner
- rollout and rollback criteria
- launch checklist
- post-launch metric review

Avoid writing plans that only list tasks. Every item should point to a user/business outcome, a decision, evidence, a risk, or a stakeholder commitment.

Do not produce development-stage artifacts: architecture plans, engineering tickets, implementation stories, production code, test code, or code review output.

## Roadmap And Prioritization

Use prioritization to make tradeoffs explicit, not to justify a preselected answer.

Useful scoring lenses:

- RICE: reach, impact, confidence, effort
- impact-effort
- MoSCoW
- strategic fit against current product goals
- risk reduction

Roadmap output should include selected direction, rejected alternatives, sequencing rationale, success signals, and open decisions.

## LLM Platform Domain Integration

When the product is an LLM aggregation platform, read `pm-llm-platform` and include:

- demand side: tenant, customer, user, API consumer, operator
- supply side: vendor, cloud, source channel, model family, resource pool
- commercial side: price, discount, gross margin, settlement, rebate
- operational side: quota, health, logs, routing, fallback, audit
- risk side: customer detection, vendor instability, billing mismatch, compliance
