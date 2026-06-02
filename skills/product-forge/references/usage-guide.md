# ProductForge Usage Guide

完整中文使用手册见项目内 `docs/ProductForge使用手册.md`。

Codex 中使用 ProductForge 命令时，使用 `$` 前缀：

```text
$pf-help [当前状态或问题]
$pf-init [产品背景或版本目标]
$pf-intake [原始需求]
$pf-discovery [客户发现、机会树或假设验证]
$pf-research [调研问题]
$pf-roadmap [产品策略、优先级或路线图问题]
$pf-metrics [北极星、输入、护栏或上线指标]
$pf-narrative [PRFAQ、客户 FAQ 或干系人叙事]
$pf-define [功能需求]
$pf-spec [功能名或需求说明]
$pf-prd [功能名或需求说明]
$pf-prototype [功能名或原型要求]
$pf-plan [版本目标或功能名]
$pf-project [项目管理状态或版本推进问题]
$pf-review [SPEC、PRD、原型或功能名]
$pf-accept [功能名]
$pf-retro [功能名或复盘内容]
```

ProductForge 的工作台目录是 `.product/`，核心 feature pack 包含：

```text
.product/features/<feature-slug>/
  00-intake.md
  discovery.md
  opportunity-solution-tree.md
  01-research.md
  02-define.md
  SPEC.md
  PRFAQ.md
  docs/prd.md
  metrics.md
  prototype/
  acceptance.md
  review.md
  decision-log.md
  versions/
.product/projects/<project-slug>/
  project-plan.md
  raid-log.md
  stakeholder-update.md
  decision-log.md
  launch-readiness.md
  acceptance-tracker.md
```
