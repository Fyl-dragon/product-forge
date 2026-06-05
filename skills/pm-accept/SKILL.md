---
name: pm-accept
description: Generate ProductForge acceptance criteria, UAT scenarios, product demo verification steps, rollout gates, and evidence requirements for feature packs.
---

# PM Accept

Define how product work is proven complete.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before acceptance design, ask exactly one boundary question with exactly three options:
   - 问题：这次 acceptance 先证明哪类完成度？
   - A. 业务规则和 capability 覆盖。
   - B. 角色权限、状态流转和异常场景。
   - C. 原型 Demo、上线门禁和证据闭环。
   - 请回复 A / B / C。
3. After the user chooses, read `SPEC.md`, PRD, metrics, prototype demo, product spec, review findings, and release plan.
4. Create only `.product/features/<feature-slug>/acceptance.md`.
5. Include:
   - 功能验收标准
   - capability ID 覆盖
   - 角色/权限验收
   - 状态流转验收
   - 异常场景
   - 业务规则与数据一致性
   - 数据展示验收
   - 原型 Demo 验收
   - 灰度与上线门槛
   - 指标基线、目标与观察周期
   - 验收证据
6. Every scenario should name the observable evidence needed to pass.

## Evidence Chain Rules

- Under `验收证据`, always add a mandatory auditable table named `证据链门禁表` with columns `来源/场景`, `Gate Status`, `负责人`, `验收证据`, and `关闭/放行条件`.
- Also add two more audit tables:
  - `角色/规则证据链表`
  - `指标门禁表`
- Treat these tables as required output structure, not optional examples.
- In these tables, create one row for every review finding, open question, locked decision, launch-plan milestone, metric gate, and selected-option core rule.
- Copy source terms verbatim into the row instead of paraphrasing them away. Preserve names such as `北区`, `样本量不足`, `临时授权审批`, `门禁证据回填延迟`, `供应商 B`, `T-7`, `T-1`, `高优租户`, `训练营`, and role names when they appear in source files.
- Each evidence-chain row must bind these elements in the same row: source scenario or risk term, `PASS` / `CONCERN` / `FAIL`, owner/负责人 or a concrete responsible role, and observable evidence.
- In the `负责人` column, prefer accountable owner titles over bare participant labels. When the source only gives executor-like roles such as `销售运营`, `审批人`, `销售主管`, `值班`, or `SRE`, expand at least one owner into a literal owner form such as `销售运营负责人`, `审批流程负责人`, `证据负责人`, `SRE 负责人`, `发布负责人`, or `owner`.
- For unresolved review findings or open questions, use `CONCERN` or `FAIL` until closure evidence exists. Include the exact finding phrase, responsible role, evidence needed to close, and launch/rollout impact in the same row.
- For approval-flow or evidence-chain risks under option `A`, especially rows containing terms like `临时授权审批` or `证据链`, the same row should explicitly include an accountable owner label such as `审批流程负责人` or `销售运营负责人`; do not leave the `负责人` cell as only `审批人` or `销售运营`.
- If `review-findings.md`, `.product/STATE.md`, or `launch-plan.md` contains any non-empty item, never emit a fake ``无`` row for that category. Only write ``无`` when the source category is truly empty after inspection.
- In `证据链门禁表`, add one row per:
  - review finding bullet
  - open question item
  - locked decision item
  - launch-plan milestone or rollout bullet
  - gating rollout statement from PRD/SPEC
- In `角色/规则证据链表`, add one row per selected-option core rule. Keep the exact actor and exact rule in the same row.
  - For option `A`, include rows like `新销售 + 建议 + 证据来源/可追溯`, `销售主管 + 建议不可解释`, `超阈值折扣 + 升级审批`, or equivalent source-grounded rows when those terms exist.
  - For option `B`, include rows like `证据缺失 + 不得放行`, `已阻塞 + 恢复/关闭`, and any role-specific release rule from PRD/SPEC/review findings.
  - For option `B`, blocking release-gate rows such as `证据缺失 + 不得放行` must stay `FAIL` or `CONCERN` until the same row shows closure evidence and explicit release conditions; do not mark them `PASS` just because the rule exists in PRD/SPEC.
  - For option `C`, include rows like `T-7 + 门禁复核`, `T-1 + 回退演练 + 值班`, `供应商 B + 证据不完整`, or equivalent source-grounded rows when those terms exist.
- For `A` boundary rows about threshold hits, approval transitions, or suggestion traceability, keep source-like evidence nouns verbatim in the same row instead of replacing them with generic `日志` or `截图`. Prefer exact terms such as `规则命中日志`, `审批流转记录`, `证据来源`, `可追溯`, `抽检记录`, `原文定位`, and similar source-grounded evidence phrases when available.
- For role-specific rules, bind the role, rule, gate state, and evidence together in one row. Prefer listing multiple concrete roles in the same row when the source shows shared ownership, instead of arbitrarily picking one role.
- For rollout gates, bind the milestone/time point, gate state, owner, and evidence together in one row. Example shape: `T-1 + 回退演练 + PASS/CONCERN + 值班 + SRE 负责人 + 演练记录`.
- In `指标门禁表`, add one row per metric, and if multiple metrics share one rollout scope or observation window, add an extra combined summary row that names the shared scope, all relevant metric names, and the observation window together.
- For metrics gates, bind the rollout scope, metric names, observation window, status, owner, and evidence together in one row. Example shape: `训练营 + 复盘覆盖率 + 建议采纳率 + 观察周期 + CONCERN + 指标报表`.
- In every combined metric summary row, include the literal phrase `观察周期` inside the `来源/场景` cell instead of only expressing the window as prose elsewhere.
- When the source contains regional or phased scope words such as `训练营`, `Q3`, `东区`, `南区`, `华东区`, `全国推广`, or `高优租户`, repeat those scope words inside the relevant metric and rollout rows instead of relying on nearby prose.
- Do not scatter a risk term in one section and its owner/status/evidence in another; acceptance must be auditable row by row.
