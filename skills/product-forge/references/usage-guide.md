# ProductForge Usage Guide

完整中文使用手册见项目内 `docs/ProductForge使用手册.md`。

Codex 中使用 ProductForge 命令时，使用 `$` 前缀：

```text
$pm-help [当前状态或问题]
$pm-init [产品背景或版本目标]
$pm-intake [原始需求]
$pm-discovery [客户发现、机会树或假设验证]
$pm-research [调研问题]
$pm-roadmap [产品策略、优先级或路线图问题]
$pm-metrics [北极星、输入、护栏或上线指标]
$pm-narrative [PRFAQ、客户 FAQ 或干系人叙事]
$pm-define [功能需求]
$pm-spec [功能名或需求说明]
$pm-prd [功能名或需求说明]
$pm-prototype [功能名或原型要求]
$pm-plan [版本目标或功能名]
$pm-project [项目管理状态或版本推进问题]
$pm-review [SPEC、PRD、原型或功能名]
$pm-accept [功能名]
$pm-retro [功能名或复盘内容]
```

ProductForge 的工作台目录是 `.product/`，核心 feature pack 包含：

```text
.product/features/<feature-slug>/
  按阶段懒生成：
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
  按阶段懒生成：
    project-plan.md
    raid-log.md
    stakeholder-update.md
    decision-log.md
    launch-readiness.md
    acceptance-tracker.md
```

所有 `pm-*` 命令默认先做一次边界确认：先问 1 个问题，给 3 个选项，用户回复 `A / B / C` 后，再只生成当前阶段最小必要文件。
