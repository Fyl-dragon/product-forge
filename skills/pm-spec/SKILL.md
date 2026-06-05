---
name: pm-spec
description: Create or update the ProductForge product spec kernel. Use to distill intake, discovery, research, feature definition, PRDs, PRFAQ, meeting notes, or rough requirements into SPEC.md with stable capability IDs, constraints, non-goals, success signals, business rules, states, open questions, and companion files for downstream PRD, prototype, project-management, review, and acceptance work.
---

# PM Spec

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

Default mode is lazy generation. Create `SPEC.md` first and only add companion files when the selected boundary makes them necessary.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before spec writing, ask exactly one boundary question with exactly three options:
   - 问题：这次 spec 需要锁到什么粒度？
   - A. 精简 capability 契约，只锁核心问题、能力和非目标。
   - B. 标准产品契约，补齐规则、状态和成功信号。
   - C. 审查级契约，额外拆 companion 文件处理复杂规则和矩阵。
   - 请回复 A / B / C。
3. After the user chooses, read `.product/PRODUCT.md`, `.product/STATE.md`, `00-intake.md`, discovery artifacts, `01-research.md`, `PRFAQ.md`, `02-define.md`, source docs, and any existing `SPEC.md`.
4. Preserve existing capability IDs. New capabilities get the next unused `CAP-N`; never renumber or reuse retired IDs.
5. Write `SPEC.md` with:
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
6. Move bulky but load-bearing details into companion files only when the selected option requires them instead of bloating `SPEC.md`.
7. Append create/update decisions and validation notes to `decision-log.md` only after the spec boundary is agreed.
8. Recommend the next command: usually `$pm-metrics`, `$pm-narrative`, `$pm-prd`, `$pm-prototype`, `$pm-review`, or `$pm-accept`.

## Spec Law

- Capabilities describe WHAT and WHY, not implementation details.
- Every capability must have a concrete success signal.
- Constraints must change a product or project-management decision.
- Non-goals are required.
- Every load-bearing source claim must land in `SPEC.md` or a companion.
- Keep prose lean. If a section becomes a table or matrix, move it to a companion.

## Contract Binding Rules

- Do not only scatter source keywords across different sections. Bind the source actor, source object, gating term, and decision signal together in the same bullet line or paragraph whenever they are part of the same core scenario.
- When the source contains a single primary workflow, create at least one line in `problem`, `capabilities`, `business rules`, or `success signals` that keeps the full chain together instead of splitting it across multiple bullets.
- For option `A`, include at least one line that binds the primary decision-maker, the key blocking object or gate, and the decision criterion together. Good pattern: `发布经理 + 阻塞项 + 门禁 + 证据 + 是否可放行`.
- For option `A`, if the source contains a scoped-but-unlocked noun such as `外部依赖门禁`, restate that noun once in the boundary or `non-goals` area together with a literal defer phrase such as `不在本阶段`, `暂不锁定`, or `非目标`, even if it also remains in `open questions`.
- For option `B`, include at least one line that binds the main actor pair or rule pair together with the affected object and the observable outcome.
  - Example pattern: `销售 + 折扣申请 + 审批人 + 卡点`.
  - Example pattern: `高价值客户 + 证据 + 优先级`.
- For option `B`, when a source open question contains a concrete noun phrase such as `临时授权审批`, keep the noun and its qualifying uncertainty in the same line, then expand the same line with the practical sub-questions when known, such as `授权范围` / `时效` / `审计要求`.
- For option `C`, use companion files to keep dense rules auditable. In `business-rules.md`, make at least one rule line bind the operational trigger, cause, rollback or fallback behavior, and auditability in the same line when the source discusses exception handling.
  - Example pattern: `异常切换 + 触发原因 + 回退状态 + 审计`.
- If the source includes phased boundaries such as `不在本阶段`, `非目标`, or `当前阶段只输出 SPEC`, keep that boundary phrase in the same line as the scoped noun when you lock or defer it.
- In `decision-log.md`, make the selected boundary explicit with a literal `A` / `B` / `C`, record the key scope decision, and add one validation note that points back to the artifact structure you actually produced.
