---
name: pf-help
description: ProductForge command guide and next-step router. Use when the user asks how to use ProductForge, what pf-* command to run next, or wants status-aware guidance for the .product workspace.
---

# PF Help

Use this skill to orient the user and route to the next ProductForge step.

## Workflow

1. Inspect `.product/STATE.md`, `.product/ROADMAP.md`, and the relevant feature pack if present.
2. Identify the current stage: init, intake, discovery, research, roadmap, metrics, narrative, define, spec, PRD, prototype, plan, project, review, accept, retro.
3. Recommend one next `pf-*` command and explain why in one short Chinese paragraph.
4. If the workspace is missing, recommend `$pf-init`.

## Command Map

```text
$pf-init       初始化 .product 工作台
$pf-intake     录入和澄清原始需求
$pf-discovery  做客户发现、机会树、假设和实验设计
$pf-research   调研竞品、市场、用户和方案
$pf-roadmap    做产品策略、优先级和路线图
$pf-metrics    定义北极星、输入、护栏、体验和上线指标
$pf-narrative  生成客户反向叙事、PRFAQ 和内外部 FAQ
$pf-define     定义功能边界、实体、字段、状态、权限和规则
$pf-spec       生成 SPEC.md 产品规格内核
$pf-prd        基于 SPEC.md 写或更新 PRD
$pf-prototype  生成多文件 Prototype Demo
$pf-plan       规划版本、依赖、风险、灰度和上线检查
$pf-project    管理里程碑、RAID、干系人沟通、上线准备和验收推进
$pf-review     审查 spec/PRD/原型/计划的产品质量
$pf-accept     生成验收标准、UAT、上线门禁和证据要求
$pf-retro      复盘决策、经验、问题和后续需求
```

## Routing Defaults

- No `.product/`: `$pf-init`.
- Rough idea only: `$pf-intake`.
- Weak evidence or many assumptions: `$pf-discovery`.
- Market or competitor uncertainty: `$pf-research`.
- Need prioritization, sequencing, or product strategy: `$pf-roadmap`.
- Need success metric, launch metric, or post-launch review model: `$pf-metrics`.
- Need stakeholder alignment or customer-backward framing: `$pf-narrative`.
- Scope/field/status/permission ambiguity: `$pf-define`.
- Feature boundary stable but no machine contract: `$pf-spec`.
- Spec exists but no PRD: `$pf-prd`.
- PRD/spec exists and user needs demo: `$pf-prototype`.
- Ready to coordinate delivery: `$pf-plan`.
- Need project management cadence or stakeholder alignment: `$pf-project`.
- Need quality gate: `$pf-review`.
- Need proof of completion: `$pf-accept`.
- Completed or changed direction: `$pf-retro`.
