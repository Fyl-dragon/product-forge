---
name: pf-define
description: Define a ProductForge feature before product spec or PRD writing. Use to specify feature goal, users, scenarios, entities, fields, statuses, permissions, workflows, business rules, edge cases, and acceptance direction.
---

# PF Define

Use when requirements are too rough for spec, PRD, or prototype work.

## Workflow

1. Read product context and related feature docs.
2. Define the feature pack path `.product/features/<feature-slug>/`.
3. Produce or update `.product/features/<feature-slug>/02-define.md`:
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
4. Recommend `$pf-spec` once the feature boundary is stable.
