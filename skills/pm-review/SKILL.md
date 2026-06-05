---
name: pm-review
description: Review ProductForge specs, PRDs, prototype demos, product specs, release plans, and project-management artifacts for product quality. Findings-first review covering product logic, missing states, unclear scope, field gaps, commercial risks, operational risks, stakeholder risks, and acceptance gaps.
---

# PM Review

Use review mindset. Findings first.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before reviewing, ask exactly one boundary question with exactly three options:
   - 问题：这次 review 先看哪类产品风险？
   - A. 范围和产品逻辑。
   - B. 规则、状态、权限和异常完整性。
   - C. 上线、验收和干系人风险。
   - 请回复 A / B / C。
3. After the user chooses, read target PRD/prototype/spec and `.product/` context.
4. Read `product-forge/references/review-checklist.md`.
5. Review for:
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
6. Return findings ordered by severity: P0, P1, P2, P3.
7. Save or propose only `.product/features/<feature-slug>/review.md` when the user wants the review persisted.
   - Keep the review findings-first; do not lead with praise or summary.
   - In the persisted `review.md`, mention the exact feature name from the request or feature context at least once near the beginning.
   - Reuse the exact business anchor nouns that define the risk surface for the chosen boundary. Examples:
     - A: feature name, target user, scope, non-goals, success signal
     - B: feature name, rules, statuses, permissions, exceptions
     - C: feature name, launch, acceptance, rollback, owner, dependency, stakeholder, operational risk, 值班
   - Do not let the review drift into generic findings that omit the feature's own name or core business nouns.
   - Prefer compact markdown tables or short bullets, but make each critical finding self-contained. Do not rely on a section intro, table header, or a previous sentence to carry the business anchor nouns for a finding.
   - When a finding is about a concrete gate or risk, repeat the anchor labels inside the finding line itself, such as `owner / 负责人：...`, `dependency / 依赖：...`, `stakeholder / 干系人：...`, `rollback / 回滚：...`, `success signal / 成功信号：...`, `data source / 数据来源：...`.
   - When a row-binding rule names a specific noun family, keep those exact nouns on the line. Do not silently swap `规则` into `数据来源`, and do not swap `回滚` into `owner`.
   - Before finishing, do a same-line binding check: if two or more nouns belong to one finding, keep them in the same markdown row or the same bullet, not split across a paragraph intro and a later table row.
   - Option A row-binding rules:
     - Include at least one A-finding that keeps `feature name + target user + scope + non-goals` on the same line.
     - Include at least one A-finding that keeps the exact user/workflow nouns from the docs on the same line as `success signal / 成功信号`; do not abstract them away. Examples: `新销售 + 复盘 + 建议 + 成功信号`, `区域经理 + 推荐价 + 差价解释 + 成功信号`.
     - If the same A-finding also depends on source quality, append `data source / 输入来源` to that same line instead of moving it to another row.
   - Option B row-binding rules:
     - Include at least one B-finding that keeps `feature name + statuses + permissions + exceptions` on the same line.
     - Include at least one B-finding that keeps `entities + fields + rules / business rule + audit / 审计 / 留痕` on the same line when the gap is rule completeness.
     - Include at least one B-finding that keeps `entities + fields + data source / source of truth / 数据来源 + audit / 审计 / 留痕` on the same line when the gap is source-of-truth completeness.
   - Option C row-binding rules:
     - Include at least one C-finding that keeps `feature name + launch + acceptance + rollback + owner` on the same line.
     - Include at least one C-finding that keeps `dependency + stakeholder + operational risk / 值班 + rollback` on the same line.
     - If launch risk depends on a named stage or gate from the docs, keep that stage anchor on the same line too, such as `T-1`, `GA`, `beta`, `白名单`, `回退演练`.

Do not lead with praise or summary. If no findings, state that clearly and list residual risks.
