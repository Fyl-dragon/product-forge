# PM Review Checklist

Use this checklist for `$pm-review`.

## Problem And Scope

- Is the target user explicit?
- Is the problem separated from the proposed solution?
- Are goals measurable?
- Are non-goals documented?
- Are assumptions visible?
- Does every important capability have a concrete success signal?

## Product Logic

- Are entities and fields complete enough for product and project-management discussion?
- Are statuses and transitions defined?
- Are permissions and role differences clear?
- Are empty, loading, error, disabled, and success states covered?
- Are audit, logs, or traceability needed?
- Do PRD, prototype, and acceptance artifacts reference the same capability IDs?

## Commercial And Operational Risk

- Does the PRD mention pricing, margin, quota, settlement, or SLA when relevant?
- Does the workflow create operational burden?
- Are edge cases and fallback rules defined?
- Are customer-visible commitments consistent with internal routing or supply behavior?

## Prototype Demo

- Does the prototype demonstrate the real workflow?
- Are mock records realistic?
- Is copy externalized?
- Are important nodes marked with `data-pm-id`?
- Can a stakeholder understand the feature without an oral explanation?

## Output Format

Return findings first, ordered by severity:

- P0: blocks product correctness or causes serious business risk
- P1: likely causes product/project ambiguity or user-visible failure
- P2: important quality gap
- P3: polish or documentation improvement
