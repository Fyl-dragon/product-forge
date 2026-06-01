---
name: pgd-review
description: Review PRDs, prototype demos, product specs, and release plans for product quality. Findings-first review covering product logic, missing states, unclear scope, field gaps, commercial risks, operational risks, and acceptance gaps.
---

# PGD Review

Use review mindset. Findings first.

## Workflow

1. Read target PRD/prototype/spec and `.product/` context.
2. Read `product-gsd/references/review-checklist.md`.
3. Review for:
   - problem clarity
   - scope ambiguity
   - missing entities/fields/statuses
   - permission gaps
   - missing empty/loading/error/disabled/success states
   - commercial/operational risk
   - acceptance gaps
   - prototype demo gaps
4. Return findings ordered by severity: P0, P1, P2, P3.

Do not lead with praise or summary. If no findings, state that clearly and list residual risks.

