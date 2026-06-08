---
name: pm-plan
description: Create ProductForge product release plans, scope milestones, dependency maps, launch checklists, risk logs, rollout criteria, and post-launch metric review plans without entering development execution.
---

# PM Plan

Turn product scope into release and project-management planning.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. First detect whether the conversation already contains the user's boundary selection:
   - If A / B / C is already selected in the conversation, do not ask again; continue directly.
   - If no selection exists yet, ask exactly one boundary question with exactly three options, output exactly the following five lines verbatim with no blank lines, bullets, markdown formatting, or extra text before/after, then stop and wait:
     问题：这次 plan 先推进哪类计划边界？
     A. 里程碑和范围切分。
     B. 风险、依赖和决策门禁。
     C. 上线与灰度准备。
     请回复 A / B / C。
   - Before the user selects A / B / C, do not generate artifacts and do not modify any files.
3. After a boundary is selected, read `SPEC.md`, PRD, prototype, acceptance criteria, `.product/PRODUCT.md`, `.product/STATE.md`, and `.product/config.yaml`. Read `.product/ROADMAP.md` and `.product/PRIORITIZATION.md` if present.
4. Split milestones by user/business value and decision gates, not by engineering tasks.
5. Identify dependencies, decisions, risks, owners, and evidence.
6. Create only the current-stage minimal plan content needed by the selected option, and keep it grounded in the feature's stated release context, scope, stage, and success language from the prompt and workspace:
   - A: 版本目标 / 里程碑 / 范围切分 / 决策门禁 / 负责人（含验收负责人）
   - B: 版本目标 / 依赖 / 风险 / 决策门禁 / 缓解动作 / 负责人 / 证据
   - C: 灰度策略 / 回滚条件 / 上线检查项 / 验收负责人 / 上线后观察指标
   - Do not add sections outside the selected boundary unless required for coherence by the task's required headings.
7. Update only the artifact required for the current stage, usually `.product/ROADMAP.md`. Do not create extra planning files, and do not modify `.product/STATE.md` unless the task explicitly requires a state update.
8. In the final user-facing reply, briefly confirm which artifact was updated, note if other planning files were not changed, and recommend exactly one next command: `$pm-project`.

## Boundary

## Deliverable Discipline

- Prefer the smallest valid artifact update that satisfies the selected boundary.
- When benchmark or workspace rules name a required artifact path, restrict writes to that path only.
- Do not expand into implementation planning, multi-file planning packs, or unrelated roadmap sections.
- If the user only needs the boundary question, the correct behavior is to ask it and wait.

Do not create developer tickets, implementation stories, architecture tasks, production code tasks, or test-code tasks.
