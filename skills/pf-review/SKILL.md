---
name: pf-review
description: Review ProductForge specs, PRDs, prototype demos, product specs, release plans, and project-management artifacts for product quality. Findings-first review covering product logic, missing states, unclear scope, field gaps, commercial risks, operational risks, stakeholder risks, and acceptance gaps.
---

# PF Review

Use review mindset. Findings first.

## Workflow

1. Read target PRD/prototype/spec and `.product/` context.
2. Read `product-forge/references/review-checklist.md`.
3. Review for:
   - problem clarity
   - weak or missing capability success signals
   - scope ambiguity
   - missing entities/fields/statuses
   - permission gaps
   - missing empty/loading/error/disabled/success states
   - commercial/operational risk
   - acceptance gaps
   - prototype demo gaps
   - project-management gaps: unclear owner, dependency, risk, stakeholder update, or launch readiness
4. Return findings ordered by severity: P0, P1, P2, P3.
5. Save or propose `.product/features/<feature-slug>/review.md` when reviewing a feature pack.

Do not lead with praise or summary. If no findings, state that clearly and list residual risks.
