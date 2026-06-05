# ProductForge Interaction Protocol

ProductForge defaults to a conversation-first workflow. Every `pm-*` command must confirm boundary before generating formal artifacts.

## Boundary Confirmation Gate

Before writing any formal document, ask exactly one high-leverage boundary question and provide exactly three mutually exclusive options.

Required response shape:

```text
问题：<当前阶段最关键的边界问题>
A. <边界选项 A：偏窄、偏聚焦，说明会产出什么>
B. <边界选项 B：标准推荐，说明会产出什么>
C. <边界选项 C：偏广、偏完整，说明会产出什么>
请回复 A / B / C。
```

Rules:

- The question must determine the next artifact boundary, not ask for general brainstorming.
- The three options must change scope, depth, target decision, or artifact fan-out in a meaningful way.
- Do not generate formal artifacts before the user chooses an option.
- If the user's request already clearly picks one option, briefly restate the interpreted choice and continue.
- Only ask one boundary question per turn unless the user explicitly asks for deeper drilling.

## Lean Artifact Policy

ProductForge uses stage-only generation by default.

- Only create or update the current-stage minimal artifact(s).
- Do not create downstream artifacts in advance.
- Do not scaffold the entire feature pack or project pack unless the user explicitly asks for full scaffolding.
- Prefer updating `.product/STATE.md` with current phase, chosen boundary, next step, locked decisions, and open questions.

Examples:

- `$pm-intake`: default only `00-intake.md`
- `$pm-spec`: default only `SPEC.md`, companion files only when required
- `$pm-project`: default only the selected project-management artifact
- `$pm-prototype`: default only when the user explicitly chooses prototype depth that requires files

## Fast Path

Fast path is exceptional. Only skip the boundary gate when the user explicitly asks to skip confirmation, reuse an already selected option, or update an existing artifact with a narrowly scoped change.
