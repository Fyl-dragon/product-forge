---
name: pm-init
description: Initialize or refresh a ProductForge .product workspace for a repo or product. Use when creating PRODUCT.md, STATE.md, config.yaml, optional root artifacts, references, and initial product context for professional PM workflows.
---

# PM Init

Initialize or refresh `.product/` without deleting existing docs.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before initializing, ask exactly one boundary question with exactly three options:
   - 问题：这次要把 `.product/` 初始化到什么深度？
   - A. 最小工作台：只建 `PRODUCT.md`、`STATE.md`、`config.yaml` 和目录。
   - B. 标准工作台：额外补齐 `REQUIREMENTS.md`、`ROADMAP.md` 等常用根文档。
   - C. 导入模式：在标准工作台基础上梳理现有文档映射。
   - 请回复 A / B / C。
3. After the user chooses, inspect existing `docs/`, README, product files, and visible project structure.
4. Create only the files required by the chosen option. Default is lean initialization, not full scaffolding.
5. If existing docs are present and the chosen option requires it, map them by feature and create `source-map.md` under `.product/features/<feature-slug>/`.
6. Preserve uncertainty as open questions. Do not invent product facts that are not in the repo or user request.

## Output

Summarize initialized files, mapped docs, assumptions, and next recommended `pm-*` command.
