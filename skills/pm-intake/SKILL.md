---
name: pm-intake
description: Convert rough product ideas, voice-like notes, meeting notes, stakeholder requests, or messy requirement fragments into structured ProductForge intake with problem definition, target users, scenarios, scope, risks, assumptions, and open questions.
---

# PM Intake

Use for early requirement analysis.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Boundary selection is mandatory before intake generation:
   - If the conversation has not selected A / B / C yet, ask exactly one boundary question with exactly these three options, then stop and wait.
   - Do not generate intake content, do not ask any additional follow-up questions, and do not write any files before the user selects a boundary.
   - 问题：这次 intake 先锁哪类边界？
   - A. 问题和目标用户，先确认为什么要做。
   - B. 范围和约束，先确认做什么/不做什么。
   - C. 目标和风险，先确认成功标准与主要不确定性。
   - 请回复 A / B / C。
3. If the user already chose A / B / C in the conversation, do not re-ask; continue directly. Then read `.product/PRODUCT.md`, `.product/STATE.md`, and relevant feature context when available. Read `.product/REQUIREMENTS.md` if it already exists.
4. Separate confirmed facts, inferred assumptions, proposed solution, and unresolved questions.
5. Produce or update only `.product/features/<feature-slug>/00-intake.md`:
   - 背景
   - 目标用户
   - 业务目标
   - 问题定义
   - 核心场景
   - 范围内
   - 范围外
   - 关键规则
   - 风险
   - 待确认问题
   - Reuse the user's key actors, domain terms, and problem signals instead of drifting into generic PM language.
   - If the request is about faster discovering anomalies, risks, churn, margin damage, or operational problems, make the artifact use explicit signal nouns such as `预警`、`告警`、`监控`、`提醒` instead of only abstract phrases like “更快发现”.
   - If the request is about approvals, routing, or review, preserve those operation nouns explicitly as well.
   - Emphasize the chosen boundary in the write-up: A = sharpen problem and target users; B = sharpen scope, exclusions, and constraints; C = sharpen goals, success criteria, major risks, and uncertainties.
   - Do not create or modify any other artifact at this stage unless step 6 explicitly applies.
6. Only append or propose a requirement entry for `.product/REQUIREMENTS.md` when the chosen boundary or user request explicitly asks for backlog sync.
7. Recommend the next command: usually `$pm-discovery`, `$pm-research`, `$pm-roadmap`, `$pm-define`, or `$pm-spec`.

## Reply Contract

- If you only asked the boundary question, the reply should contain only that question block.
- After writing the intake, briefly confirm completion and reference the single updated artifact path.
- Recommend exactly one next `pm-*` command; default to `$pm-discovery` unless the context clearly suggests another listed command.

## Quality Bar

Do not jump directly to UI. Lock problem, user, success criteria, and boundary first.
