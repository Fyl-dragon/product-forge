# ProductForge

ProductForge 是面向专业产品经理的 AI 产品工作框架，可以理解为产品经理版 GSD/BMAD：它覆盖产品管理到产品侧项目管理，把需求分析拆成可持续维护的 `.product` 工作台、`SPEC.md` 产品契约、PRD、产品原型演示、项目管理、评审、验收和复盘。

框架已吸收成熟产品方法：持续发现/机会树、RICE/路线图优先级、North Star/护栏指标、Working Backwards PRFAQ、RAID 项目管理。

ProductForge 明确不进入开发阶段：不生成架构方案、工程任务、实现故事、生产代码、测试代码或代码评审。

## 命令体系

Codex 中使用 `$` 前缀：

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

## 技能包结构

```text
skills/
  product-forge/
  pf-help/
  pf-init/
  pf-intake/
  pf-discovery/
  pf-research/
  pf-roadmap/
  pf-metrics/
  pf-narrative/
  pf-define/
  pf-spec/
  pf-prd/
  pf-prototype/
  pf-plan/
  pf-project/
  pf-review/
  pf-accept/
  pf-retro/
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
  REQUIREMENTS.md
  DISCOVERY.md
  PRIORITIZATION.md
  METRICS.md
  ROADMAP.md
  STATE.md
  config.yaml
  features/<feature-slug>/
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

- `$pf-discovery`：机会树必须包含 outcome、opportunity、solution、assumption test、evidence quality、decision rule。
- `$pf-metrics`：指标体系必须包含 North Star、input metrics、guardrails、baseline、target、owner、review cadence。
- `$pf-narrative`：PRFAQ 必须包含 press release、customer FAQ、internal FAQ、risks、rejected alternatives、open questions。
- `$pf-project`：项目管理必须包含 RAID escalation rule、stakeholder update cadence、decision log、launch readiness gate、acceptance progress state。

## 安装到 Codex Skills

仓库根目录执行：

```bash
node bin/product-forge.js install --target codex --home ~/.codex
```

安装会复制 `product-forge` 与全部 `pf-*` 技能到 `~/.codex/skills`，并清理旧 `product-gsd` / `pgd-*` 技能目录，避免新旧命令同时暴露。

常用 CLI：

```bash
node bin/product-forge.js validate --source skills
node bin/product-forge.js list --source skills
node bin/product-forge.js status --target codex --home ~/.codex
node bin/product-forge.js uninstall --target codex --home ~/.codex
```

完整说明见 [docs/ProductForge使用手册.md](docs/ProductForge使用手册.md)。
