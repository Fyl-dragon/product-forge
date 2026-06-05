# ProductForge

ProductForge 是面向专业产品经理的 AI 产品工作框架，可以理解为产品经理版 GSD/BMAD：它覆盖产品管理到产品侧项目管理，把需求分析拆成可持续维护的 `.product` 工作台、`SPEC.md` 产品契约、PRD、产品原型演示、项目管理、评审、验收和复盘。

框架已吸收成熟产品方法：持续发现/机会树、RICE/路线图优先级、North Star/护栏指标、Working Backwards PRFAQ、RAID 项目管理。

ProductForge 明确不进入开发阶段：不生成架构方案、工程任务、实现故事、生产代码、测试代码或代码评审。

## 交互原则

ProductForge 默认不是“收到命令就直接出文档”，而是先做一次边界确认：

- 每个 `pm-*` 命令先问 1 个问题。
- 每个问题只给 3 个互斥选项。
- 用户回复 `A / B / C` 后，再根据选项生成当前阶段最小必要产物。
- 默认按阶段懒生成，不整包预创建 feature pack / project pack。

## 命令体系

Codex 中使用 `$` 前缀：

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

## 技能包结构

```text
skills/
  product-forge/
  pm-help/
  pm-init/
  pm-intake/
  pm-discovery/
  pm-research/
  pm-roadmap/
  pm-metrics/
  pm-narrative/
  pm-define/
  pm-spec/
  pm-prd/
  pm-prototype/
  pm-plan/
  pm-project/
  pm-review/
  pm-accept/
  pm-retro/
docs/
  ProductForge使用手册.md
bin/
  product-forge.js
```

## Product Workspace

ProductForge 的持久化工作台是 `.product/`：

```text
.product/
  PRODUCT.md
  STATE.md
  config.yaml
  按阶段懒生成的根文档：
    REQUIREMENTS.md
    DISCOVERY.md
    PRIORITIZATION.md
    METRICS.md
    ROADMAP.md
  features/<feature-slug>/
    按阶段懒生成：
      00-intake.md
      01-research.md
      discovery.md
      opportunity-solution-tree.md
      02-define.md
      SPEC.md
      PRFAQ.md
      docs/prd.md
      metrics.md
      prototype/
        index.html
        styles.css
        app.js
        data/sample-data.json
        data/copy.zh-CN.json
        spec/product-spec.json
      acceptance.md
      review.md
      decision-log.md
      versions/
  projects/<project-slug>/
    按阶段懒生成：
      project-plan.md
      raid-log.md
      stakeholder-update.md
      decision-log.md
      launch-readiness.md
      acceptance-tracker.md
  references/
```

`SPEC.md` 是核心机器契约：capability 使用稳定 ID，例如 `CAP-1`，后续 PRD、原型、项目管理、评审和验收都引用这些 ID。

## 质量门禁

ProductForge 不靠命令数量堆能力，核心门禁是产物字段必须足够可审查：

- `$pm-discovery`：机会树必须包含 outcome、opportunity、solution、assumption test、evidence quality、decision rule。
- `$pm-metrics`：指标体系必须包含 North Star、input metrics、guardrails、baseline、target、owner、review cadence。
- `$pm-narrative`：PRFAQ 必须包含 press release、customer FAQ、internal FAQ、risks、rejected alternatives、open questions。
- `$pm-project`：项目管理必须包含 RAID escalation rule、stakeholder update cadence、decision log、launch readiness gate、acceptance progress state。

## 安装到 Codex Skills

仓库根目录执行：

```bash
node bin/product-forge.js install --target codex --home ~/.codex
```

安装会复制 `product-forge` 与全部 `pm-*` 技能到 `~/.codex/skills`，并清理旧 `product-gsd` / `pgd-*` 技能目录，避免新旧命令同时暴露。

常用 CLI：

```bash
node bin/product-forge.js validate --source skills
node bin/product-forge.js list --source skills
node bin/product-forge.js status --target codex --home ~/.codex
node bin/product-forge.js uninstall --target codex --home ~/.codex
```

完整说明见 [docs/ProductForge使用手册.md](docs/ProductForge使用手册.md)。
