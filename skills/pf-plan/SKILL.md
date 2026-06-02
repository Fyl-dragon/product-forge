---
name: pf-plan
description: Create ProductForge product release plans, scope milestones, dependency maps, launch checklists, risk logs, rollout criteria, and post-launch metric review plans without entering development execution.
---

# PF Plan

Turn product scope into release and project-management planning.

## Workflow

1. Read `SPEC.md`, PRD, prototype, acceptance criteria, `.product/PRIORITIZATION.md`, `.product/ROADMAP.md`, and `.product/STATE.md`.
2. Split milestones by user/business value and decision gates, not by engineering tasks.
3. Identify dependencies, decisions, risks, owners, and evidence.
4. Create launch plan:
   - 里程碑
   - 范围
   - 依赖
   - 风险
   - 验收负责人
   - 灰度策略
   - 回滚条件
   - 上线检查项
   - 上线后观察指标
5. Update or propose `.product/ROADMAP.md` and `.product/STATE.md` changes.
6. Recommend `$pf-project` when ongoing milestone tracking, stakeholder updates, or RAID management is needed.

## Boundary

Do not create developer tickets, implementation stories, architecture tasks, production code tasks, or test-code tasks.
