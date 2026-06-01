---
name: pgd-write-prd
description: Write or update product requirement documents for Product GSD feature packs. Use for Markdown PRDs with goals, scenarios, requirements, business rules, data model, permissions, states, acceptance criteria, risks, and open questions.
---

# PGD Write PRD

Default target: `.product/features/<feature-slug>/docs/prd.md`.

## Workflow

1. Read `.product/PRODUCT.md`, `.product/STATE.md`, relevant `context.md`, `research.md`, and source docs.
2. If the domain is LLM aggregation, read `pm-llm-platform`.
3. Write PRD in Chinese with:
   - 背景与问题
   - 目标与非目标
   - 用户与场景
   - 功能范围
   - 业务规则
   - 数据对象与字段
   - 权限与角色
   - 状态流转
   - 页面/交互要求
   - 异常与边界
   - 验收标准
   - 风险与待确认
4. Preserve assumptions explicitly.

## Rule

PRD must be specific enough to generate a prototype demo and acceptance cases.

