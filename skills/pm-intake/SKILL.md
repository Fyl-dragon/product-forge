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
   - Preserve high-salience source terms when they express the product signal itself, not just the domain. Examples: 告警, 预警, 提醒, 复盘, 审批, 路由, 毛利, 上线门禁. If the user or context uses one of these signal words, make sure it appears explicitly in the intake artifact.
   - Keep evidence labels explicit inside the artifact. Use concrete markers such as `已确认` for grounded facts, `推断` or `假设` for inferred statements, and `待确认` for unresolved constraints. Do not collapse all three into smooth generic prose.
   - Keep key business anchors self-contained on the same markdown line or bullet. Do not rely on the heading, section title, or a previous sentence to carry the feature noun, user, and risk/signal noun.
   - Option A same-line binding:
     - Include at least one A-line that keeps `feature noun + primary user + core problem or risk noun` together. Examples: `折扣审批 + 销售经理 + 毛利`, `AI 跟进教练 + 新销售 + 复盘 / 话术`.
     - If the open questions couple threshold scope with approver escalation, keep them on the same `待确认` line. Example: `折扣阈值 + 区域差异化 + 财务共同审批`.
   - Option B same-line binding:
     - Include at least one B-line that keeps `feature noun or signal noun + affected user + operational signal noun` together. Examples: `异常报价 + 区域经理 + 微信群 + 预警`, `供应商报价 + 毛利 + 告警 / 预警 / 提醒 / 监控`.
     - Include at least one B-line that keeps `threshold or constraint noun + scope/entity noun` together. Examples: `异常阈值 + 品类 + 合同`, `阈值 + 跨区查看`.
     - If the open questions mention two concrete constraints at once, keep them on the same `待确认` line instead of scattering them. Examples: `异常识别阈值 + 跨区查看`, `折扣阈值 + 财务共同审批`.
   - Option C same-line binding:
     - Include at least one C-line that keeps `feature noun or signal noun + primary user + success or risk noun` together. Examples: `流失预警 + 客户成功 + 续费`, `模型路由 + 资源池 + SLA + 故障切换`.
     - If the open questions couple segmentation/threshold uncertainty with action uncertainty, keep them on the same risk or `待确认` line. Examples: `客户分层 + 动作建议 + 风险`, `预警阈值 + 动作建议 + 风险`.
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
