---
name: pm-project
description: Manage ProductForge project-management artifacts for product managers after scope is defined. Use for milestones, RAID logs, stakeholder updates, decision tracking, launch readiness, acceptance progress, and cross-functional coordination without entering development execution.
---

# PM Project

Use this for product-side project management. It coordinates delivery readiness and stakeholder alignment, but it does not create engineering tasks, architecture, production code, test code, or code review instructions.

## Default Output

```text
.product/projects/<project-slug>/
  project-plan.md
  raid-log.md
  stakeholder-update.md
  decision-log.md
  launch-readiness.md
  acceptance-tracker.md
```

Default mode is lazy generation. Create only the project-management artifact(s) needed by the chosen option.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. First determine whether the conversation has already selected A / B / C.
   - If no option has been selected yet, ask exactly one boundary question with exactly three options, output exactly the following five lines verbatim with no blank lines, bullets, markdown formatting, or extra text before/after, then stop and wait:
     问题：这次 project 先补哪类管理门禁？
     A. RAID 和决策追踪。
     B. 干系人沟通和里程碑状态。
     C. 上线准备和验收推进。
     请回复 A / B / C。
   - If the user already selected an option anywhere in the conversation, do not re-ask. Continue directly.
3. Once an option is selected, read `.product/PRODUCT.md`, `.product/STATE.md`, related `SPEC.md`, PRD, acceptance criteria, review findings, and launch plan. Read `.product/ROADMAP.md` if present.
4. Define product/project milestones by outcome, not by development tasks, and keep all content grounded in the actual product context from the docs and user prompt.
5. Create or update only the current-stage minimal artifact pair required by the selected option:
   - A -> `raid-log.md` + `decision-log.md`
   - B -> `project-plan.md` + `stakeholder-update.md`
   - C -> `launch-readiness.md` + `acceptance-tracker.md`
   Do not create other project-management files in the same turn unless the user explicitly asks for them.
6. Keep all open items owner-based and evidence-based.
   Also keep them specific: carry forward the real rollout stage, target regions or audiences, named blockers, dependencies, owners, evidence, and dates/cadence from the source materials instead of using generic placeholders.
7. Prefer compact markdown tables for the main control content.
   Do not scatter one logical control across separate bullets or separate rows when the source materials clearly bind them together.
   When a rollout anchor, gate anchor, owner, evidence theme, cadence, or expansion boundary belong to one decision, keep them in the same markdown row or the same short list item.
8. Before finishing, do a row-binding check against the source nouns:
   - If the docs mention multiple rollout units together, keep them together in one row when they describe the same gate. Examples: `产品线 A` + `产品线 B`, `华东` + `华南` + `华北`, `东区` + `南区` + `西区`, `高优白名单` + `SLA`.
   - If the docs mention a gate date or cadence phrase, keep it on the same row as the gate it controls. Examples: `每周四`, `周度项目同步`, `T-7`, `T-1`, `上线前 7 天`.
   - If the docs mention a named blocker or open question, keep that blocker or open question on the same row as its owner and revisit condition instead of only mentioning it in summary prose.
   - Do not rely on table headers alone for control labels. When a row is about evidence, owner, or revisit logic, repeat the label inside the row text itself, such as `证据：...`, `负责人：...`, `回看条件：...`.
9. Option-specific binding rules:
   - A / RAID + 决策追踪:
     Put the current scope boundary and the expansion boundary into at least one decision row, not only in a standalone scope note.
     If the source docs mention a governance noun such as `区域经理周会`, `异常阈值`, `临时授权审批`, `统一证据包`, or `审批人名录`, keep that noun on the same row as `status`, `owner`, and an inline `回看条件：...` phrase.
     If one row captures an exception policy, restate the affected base policy noun in that same row instead of assuming it from a previous row. Examples: `区域审批口径` + `临时授权审批` + `回看条件：...`; `异常阈值` + `区域经理周会` + `回看条件：...`.
     If the source docs mention metrics such as `闭环率`, `响应时长`, `超时率`, or `误路由`, keep the metric pair on the same RAID row as the rollout scope or trial stage they govern.
     If the source docs also mention a time gate such as `上线前 7 天` together with `审批人名录`, keep that time gate and the metric pair on one RAID control row instead of splitting schedule and metrics across separate rows.
     Treat the following as hard same-row packing rules, not soft guidance:
     - If the source docs mention `上线前 7 天` + `审批人名录` + `误路由` + `超时率`, at least one single RAID row must contain all four anchors together, along with the governed rollout scope or trial stage.
     - If the source docs mention `Q3` or `三区` together with `审批链超时`, `统一证据包`, and `审批人名录`, at least one single decision row must contain all of those anchors together, plus `负责人：...` and `回看条件：...`.
     - If the source docs mention `区域审批口径` and `临时授权审批`, at least one single decision row must contain both nouns together with an inline `回看条件：...`; do not place the base policy and the exception policy in separate rows.
   - B / 干系人沟通 + 里程碑状态:
     In `project-plan.md`, include at least one milestone or control row that keeps the rollout stage, the rollout units, and the cadence phrase together when they belong to the same milestone. Examples: `beta` + `产品线 A` + `产品线 B` + `每周四`; `华东` + `华南` + `华北` + `企业微信` + `通知链路`.
     In `stakeholder-update.md`, keep `门禁证据` / `证据模板` / `依赖团队反馈` / concrete owner on the same row when they describe one current gate.
     When the source docs mention a stakeholder trio such as `采购运营`, `品类经理`, `供应商经理`, keep them together on one row with the communication or sign-off mechanism they are aligning.
     Treat the following as hard same-row packing rules, not soft guidance:
     - If the source docs mention a rollout stage together with rollout units and a cadence phrase, at least one single `project-plan.md` row must contain all of those anchors together. Examples: `beta` + `产品线 A` + `产品线 B` + `每周四`; `华东` + `华南` + `华北` + `周度项目同步`.
     - If the source docs mention `企业微信` or another named communication mechanism together with rollout units, at least one single `project-plan.md` row must contain the rollout units, that communication mechanism, and the current owner together.
     - If the source docs mention a sign-off noun such as `品类经理`, `签收口径`, or `联签`, keep that sign-off noun on the same single `project-plan.md` row as the rollout units and the named communication mechanism it depends on. Example: `华东` + `华南` + `华北` + `企业微信` + `通知链路` + `品类经理` + `签收口径`.
     - If the source docs mention rollout units together with both a named communication mechanism and a cadence phrase, at least one single `project-plan.md` milestone row must contain the rollout units, the communication mechanism, and that cadence phrase together instead of splitting cadence into a later control section.
     - If the source docs mention `门禁证据`, `证据模板`, or `依赖团队反馈`, at least one single `stakeholder-update.md` row must contain those anchors together with the concrete owner inside the row text; do not rely on the owner column alone.
     - If the source docs mention rollout units such as `产品线 A` + `产品线 B` together with `门禁证据`, `证据模板`, `依赖团队反馈`, or `交付负责人`, at least one single `stakeholder-update.md` row must contain that rollout-unit pair and those gate anchors together.
     - If the source docs mention a stakeholder trio such as `采购运营` + `品类经理` + `供应商经理`, at least one single row must contain all three roles together with the aligned communication or sign-off mechanism.
     - When the source docs mention `华东` + `华南` + `华北` together with `企业微信` / `通知链路` and `品类经理` / `签收口径`, prefer one canonical first milestone row that contains all of these anchors together in this same row: rollout units, cadence phrase, communication mechanism, sign-off noun, and owner.
   - C / 上线准备 + 验收推进:
     In `launch-readiness.md`, keep scope, SLA, and gate dates on the same gate row when they belong together. If one gate is jointly controlled by `T-7` and `T-1`, put both anchors on that same row. Examples: `高优白名单` + `SLA` + `T-7` + `T-1`.
     If the source docs mention `CAP-3`, `回退入口`, `人工回退`, `回退演练`, `客服值班`, or a named supplier such as `供应商 B`, keep the relevant terms on the same gate or acceptance row instead of splitting them across separate sections. Prefer one combined blocker row when they all describe the same operational gate.
     If the source docs tie whitelist scope, `优先资源池`, and `SLA` together, add at least one combined acceptance row that keeps those three anchors together with the row owner.
     If the source docs tie supplier-specific evidence to rollback safety, keep the supplier noun on the same `CAP-3` row as `回退入口`, `回退演练`, and the relevant值班 / on-call control instead of creating a separate supplier-only row.
     If `CAP-3` and `客服值班` share the same T-1 launch gate, merge them into one combined launch or acceptance row instead of separate `CAP-3` and `客服值班` rows.
     In `acceptance-tracker.md`, each critical capability row should bind capability ID, owner, evidence state, and blocker in the same row; do not leave the blocker or evidence dependency only in a later note. Also repeat inline labels inside the row when useful, such as `负责人：...` and `证据：...`, so the capability row is self-contained without relying on the header.
     Treat the following as hard same-row packing rules, not soft guidance:
     - If the source docs mention `高优白名单` or `白名单`, `优先资源池`, and `SLA`, at least one single acceptance row must contain all three anchors together with the row owner and current evidence state.
     - If the source docs mention `CAP-3`, `回退入口`, `人工回退`, `回退演练`, and `T-1` or `客服值班`, at least one single launch or acceptance row must contain all of those anchors together; do not split rollback safety across separate rows.
     - If the source docs mention `跨云切换` in the same rollback context, keep `跨云切换` on that same single `CAP-3` / `T-1` rollback row together with `回退入口`, `人工回退`, `回退演练`, and `客服值班`.
     - If the source docs mention a supplier noun such as `供应商 B` in the same rollback context, that supplier noun must appear on the same single `CAP-3` or rollback-safety row together with `回退入口` / `回退演练` / `客服值班` or `T-1`.
     - When the source docs mention `高优白名单` / `优先资源池` / `SLA` and also mention `CAP-3` / `跨云切换` / `回退入口` / `人工回退` / `回退演练` / `客服值班` / `T-1`, prefer two canonical combined rows rather than many partial rows:
       1. one combined whitelist row containing `高优白名单` + `优先资源池` + `SLA` + `T-7` and `T-1` when both dates exist;
       2. one combined rollback row containing `CAP-3` + `跨云切换` + `回退入口` + `人工回退` + `回退演练` + `客服值班` + `T-1`.
10. In the user-facing reply, briefly confirm only the exact artifact pair written or updated for this turn, and recommend exactly one of `$pm-review`, `$pm-accept`, or `$pm-retro` that best matches the current gate.
   - Mention the exact project or feature name at least once near the start of the reply.
   - Reuse exact rollout nouns from the source materials instead of paraphrasing them away. Examples: `beta`, `GA`, `产品线 A`, `产品线 B`, `书面状态更新`, `周度项目同步`, `华东 12 家重点门店`, `区域经理`, `扩区`, `全国推广`, `高优白名单`, `SLA`, `CAP-3`, `优先资源池`.
   - For option A, explicitly mention the current scope boundary and the expansion boundary when the source docs mention them, such as `扩区` or `全国推广`.
   - For option B, explicitly mention the rollout stage and cadence phrase when the source docs mention them, such as `beta` and `书面状态更新` or `周度项目同步`.
   - For option C, explicitly mention launch stage anchors and control nouns when the source docs mention them, such as `GA`, `白名单`, `SLA`, `CAP-3`, or `优先资源池`.
   - Do not use vague summaries like `内容已对齐现有产品上下文`.
   - Always emit a final user-facing reply after writing files, and include exactly one next command token.
   - Your last action in the turn must be the user-facing reply. Do not do extra shell reads, diff inspection, or silent stopping after the files are written.

## Project Management Standard

Every project pack must include:

- RAID escalation rule: severity, trigger, owner, decision needed, and update cadence for risks, assumptions, issues, and dependencies.
- Stakeholder update cadence: audience, cadence, status summary, decision requests, risks, and next milestone.
- Decision log: decision type, status, rationale, evidence, owner, and revisit condition.
- Launch readiness gate: PASS / CONCERN / FAIL status, required evidence, blocker, and launch decision.
- Acceptance progress state: Not Started, In Progress, Blocked, Evidence Ready, Accepted, or Waived, with evidence links and owner.

## Boundary

- Do not write implementation plans, tickets, stories, architecture, code, test code, or code review output.
- If the user asks for engineering execution, hand off with a product-ready artifact summary and stop ProductForge at the product/project management boundary.
