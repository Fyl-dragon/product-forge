---
name: pgd-new-product
description: Initialize a Product GSD .product workspace for a repo or product. Use when creating PRODUCT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md, references, and initial product context for product manager AI workflows.
---

# PGD New Product

Initialize or refresh `.product/` without deleting existing docs.

## Workflow

1. Inspect existing `docs/`, README, product files, and visible project structure.
2. Create or update:
   - `.product/PRODUCT.md`
   - `.product/REQUIREMENTS.md`
   - `.product/ROADMAP.md`
   - `.product/STATE.md`
   - `.product/references/`
3. If existing docs are present, map them by feature and create `source-map.md` under `.product/features/<feature-slug>/`.
4. Preserve uncertainty as open questions. Do not invent product facts that are not in the repo or user request.

## Output

Summarize initialized files, mapped docs, assumptions, and next recommended PGD command.

