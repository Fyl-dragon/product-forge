---
name: pm-help
description: ProductForge command guide and next-step router. Use when the user asks how to use ProductForge, what pm-* command to run next, or wants status-aware guidance for the .product workspace.
---

# PM Help

Use this skill to orient the user and route to the next ProductForge step.

## Workflow

1. Read `../product-forge/references/interaction-protocol.md` and follow it strictly.
2. Before routing, ask exactly one boundary question with exactly three options. Use this default framing:
   - 问题：你现在最想解决哪类推进阻塞？
   - A. 只判断下一步命令，给最短路径。
   - B. 结合当前工作台状态，给标准推进顺序。
   - C. 先重整当前阶段和缺口，再给完整路径。
   - 请回复 A / B / C。
3. After the user chooses, inspect `.product/STATE.md`, `.product/ROADMAP.md` if present, and the relevant feature pack if present.
4. Identify the current stage: init, intake, discovery, research, roadmap, metrics, narrative, define, spec, PRD, prototype, plan, project, review, accept, retro.
5. Recommend one next `pm-*` command and explain why in one short Chinese paragraph.
6. If the workspace is missing, recommend `$pm-init`.

## Command Map

```text
$pm-init       初始化 .product 工作台
$pm-intake     录入和澄清原始需求
$pm-discovery  做客户发现、机会树、假设和实验设计
$pm-research   调研竞品、市场、用户和方案
$pm-roadmap    做产品策略、优先级和路线图
$pm-metrics    定义北极星、输入、护栏、体验和上线指标
$pm-narrative  生成客户反向叙事、PRFAQ 和内外部 FAQ
$pm-define     定义功能边界、实体、字段、状态、权限和规则
$pm-spec       生成 SPEC.md 产品规格内核
$pm-prd        基于 SPEC.md 写或更新 PRD
$pm-prototype  生成多文件 Prototype Demo
$pm-plan       规划版本、依赖、风险、灰度和上线检查
$pm-project    管理里程碑、RAID、干系人沟通、上线准备和验收推进
$pm-review     审查 spec/PRD/原型/计划的产品质量
$pm-accept     生成验收标准、UAT、上线门禁和证据要求
$pm-retro      复盘决策、经验、问题和后续需求
```

## Routing Defaults

- No `.product/`: `$pm-init`.
- Rough idea only: `$pm-intake`.
- Weak evidence or many assumptions: `$pm-discovery`.
- Market or competitor uncertainty: `$pm-research`.
- Need prioritization, sequencing, or product strategy: `$pm-roadmap`.
- Need success metric, launch metric, or post-launch review model: `$pm-metrics`.
- Need stakeholder alignment or customer-backward framing: `$pm-narrative`.
- Scope/field/status/permission ambiguity: `$pm-define`.
- Feature boundary stable but no machine contract: `$pm-spec`.
- Spec exists but no PRD: `$pm-prd`.
- PRD/spec exists and user needs demo: `$pm-prototype`.
- Ready to coordinate delivery: `$pm-plan`.
- Need project management cadence or stakeholder alignment: `$pm-project`.
- Need quality gate: `$pm-review`.
- Need proof of completion: `$pm-accept`.
- Completed or changed direction: `$pm-retro`.
