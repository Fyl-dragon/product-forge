---
name: pf-prd
description: Write or update ProductForge PRDs for feature packs. Use for Markdown PRDs grounded in SPEC.md with goals, scenarios, requirements, business rules, data model, permissions, states, acceptance criteria, risks, and open questions.
---

# PF PRD

Default target: `.product/features/<feature-slug>/docs/prd.md`.

## Workflow

1. Read `.product/PRODUCT.md`, `.product/STATE.md`, `SPEC.md`, companion files, `00-intake.md`, discovery artifacts, `01-research.md`, `PRFAQ.md`, `metrics.md`, `02-define.md`, and source docs.
2. If the domain is LLM aggregation, read `pm-llm-platform`.
3. If `SPEC.md` is missing, stop and recommend `$pf-spec` unless the user explicitly asks for fast path.
4. Write PRD in Chinese with:
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
5. Preserve assumptions explicitly and append meaningful decisions to `decision-log.md`.

## Rule

PRD must be specific enough to support product review, prototype demo, project planning, and acceptance cases.
