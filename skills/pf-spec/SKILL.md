---
name: pf-spec
description: Create or update the ProductForge product spec kernel. Use to distill intake, discovery, research, feature definition, PRDs, PRFAQ, meeting notes, or rough requirements into SPEC.md with stable capability IDs, constraints, non-goals, success signals, business rules, states, open questions, and companion files for downstream PRD, prototype, project-management, review, and acceptance work.
---

# PF Spec

Use this as the ProductForge machine contract step. It turns product intent into a lean `SPEC.md` that downstream PM artifacts can consume without re-deriving the product logic.

## Default Output

```text
.product/features/<feature-slug>/
  SPEC.md
  decision-log.md
  companions as needed:
    entities.md
    permissions.md
    state-machine.md
    business-rules.md
```

## Workflow

1. Read `.product/PRODUCT.md`, `.product/STATE.md`, `00-intake.md`, discovery artifacts, `01-research.md`, `PRFAQ.md`, `02-define.md`, source docs, and any existing `SPEC.md`.
2. Preserve existing capability IDs. New capabilities get the next unused `CAP-N`; never renumber or reuse retired IDs.
3. Write `SPEC.md` with:
   - problem
   - users/jobs
   - capabilities with `intent` and `success`
   - constraints
   - non-goals
   - business rules
   - states
   - success signals
   - evidence quality
   - assumptions
   - open questions
   - companions
4. Move bulky but load-bearing details into companion files instead of bloating `SPEC.md`.
5. Append create/update decisions and validation notes to `decision-log.md`.
6. Recommend the next command: usually `$pf-metrics`, `$pf-narrative`, `$pf-prd`, `$pf-prototype`, `$pf-review`, or `$pf-accept`.

## Spec Law

- Capabilities describe WHAT and WHY, not implementation details.
- Every capability must have a concrete success signal.
- Constraints must change a product or project-management decision.
- Non-goals are required.
- Every load-bearing source claim must land in `SPEC.md` or a companion.
- Keep prose lean. If a section becomes a table or matrix, move it to a companion.
