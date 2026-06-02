---
name: pf-project
description: Manage ProductForge project-management artifacts for product managers after scope is defined. Use for milestones, RAID logs, stakeholder updates, decision tracking, launch readiness, acceptance progress, and cross-functional coordination without entering development execution.
---

# PF Project

Use this for product-side project management. It coordinates delivery readiness and stakeholder alignment, but it does not create engineering tasks, architecture, production code, test code, or code review instructions.

## Default Output

```text
.product/projects/<project-slug>/
  project-plan.md
  raid-log.md
  stakeholder-update.md
  decision-log.md
  launch-readiness.md
  acceptance-tracker.md
```

## Workflow

1. Read `.product/PRODUCT.md`, `.product/ROADMAP.md`, `.product/STATE.md`, related `SPEC.md`, PRD, acceptance criteria, review findings, and launch plan.
2. Define product/project milestones by outcome, not by development tasks.
3. Create or update:
   - milestone plan
   - RAID log: risks, assumptions, issues, dependencies
   - stakeholder communication summary
   - decision log
   - launch readiness checklist
   - acceptance progress tracker
4. Keep all open items owner-based and evidence-based.
5. Recommend `$pf-review`, `$pf-accept`, or `$pf-retro` when the project reaches the relevant gate.

## Project Management Standard

Every project pack must include:

- RAID escalation rule: severity, trigger, owner, decision needed, and update cadence for risks, assumptions, issues, and dependencies.
- Stakeholder update cadence: audience, cadence, status summary, decision requests, risks, and next milestone.
- Decision log: decision type, status, rationale, evidence, owner, and revisit condition.
- Launch readiness gate: PASS / CONCERN / FAIL status, required evidence, blocker, and launch decision.
- Acceptance progress state: Not Started, In Progress, Blocked, Evidence Ready, Accepted, or Waived, with evidence links and owner.

## Boundary

- Do not write implementation plans, tickets, stories, architecture, code, test code, or code review output.
- If the user asks for engineering execution, hand off with a product-ready artifact summary and stop ProductForge at the product/project management boundary.
