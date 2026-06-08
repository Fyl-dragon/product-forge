---
name: pm-define
description: Define a ProductForge feature before product spec or PRD writing. Use to specify feature goal, users, scenarios, entities, fields, statuses, permissions, workflows, business rules, edge cases, and acceptance direction.
---

# PM Define

Use when requirements are too rough for spec, PRD, or prototype work.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before define work, ask exactly one boundary question with exactly three options:
   - 问题：这次 define 先锁哪类结构边界？
   - A. 功能范围和非目标。
   - B. 实体、字段和业务规则。
   - C. 状态、权限和异常流转。
   - 请回复 A / B / C。
3. After the user chooses, read product context and related feature docs.
4. Define the feature pack path `.product/features/<feature-slug>/`.
5. Produce or update only `.product/features/<feature-slug>/02-define.md`:
   - feature goal
   - target users and jobs
   - user stories
   - entities and fields
   - statuses and transitions
   - roles and permissions
   - business rules
   - exceptions and edge states
   - dependencies
   - open questions
6. Recommend `$pm-spec` once the feature boundary is stable.

## Execution Rules

- If the conversation already selected A / B / C, do not restate a work plan. Read the local context and write `02-define.md` directly in the same turn.
- Keep writes limited to the single target artifact unless the task explicitly allows more.
- Prefer a compact, template-like `02-define.md` over a long narrative draft. The goal is structural completeness, not prose polish.
- In `entities and fields`, explicitly include field name, field type, whether required, data source / source of truth, and validation rule when the task asks for entity-field detail.
- When the boundary is **B**, bias the artifact toward `entities / fields / 字段类型 / 是否必填 / 数据来源 / 校验规则 / 业务规则`, and make those labels visibly present in the file.
- Your last action in the turn must be the user-facing reply after `02-define.md` is written. Do not stop after preparation, file existence checks, or context summaries.
