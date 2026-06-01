# Product GSD Methodology

## Operating Loop

1. Intake: clarify source, stakeholder, urgency, target user, and business goal.
2. Diagnose: separate problem, symptom, proposed solution, and measurable outcome.
3. Research: inspect competitors, alternatives, internal docs, user scenarios, and constraints.
4. Define: lock scope, non-goals, entities, fields, states, permissions, and business rules.
5. Specify: write PRD, acceptance criteria, and open questions.
6. Demonstrate: build a prototype demo with realistic data and local interactions.
7. Plan: split milestones, dependencies, risks, and launch checks.
8. Review: audit product logic, business risk, edge states, and delivery ambiguity.
9. Accept: create UAT scenarios and evidence requirements.
10. Retro: record decisions, lessons, follow-ups, and context that future work must preserve.

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

Avoid writing plans that only list tasks. Every task should point to a user/business outcome or a delivery risk.

## LLM Platform Domain Integration

When the product is an LLM aggregation platform, read `pm-llm-platform` and include:

- demand side: tenant, customer, user, API consumer, operator
- supply side: vendor, cloud, source channel, model family, resource pool
- commercial side: price, discount, gross margin, settlement, rebate
- operational side: quota, health, logs, routing, fallback, audit
- risk side: customer detection, vendor instability, billing mismatch, compliance

