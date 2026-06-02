# ProductForge 使用手册

ProductForge 是面向专业产品经理的 AI 产品工作框架。它借鉴 GSD 的阶段化工作流和 BMAD 的 spec 契约思想，把产品管理到产品侧项目管理拆成可持续维护的上下文、产物和质量门禁。

本框架吸收了优秀产品方法：持续发现/机会树、RICE/路线图优先级、North Star/护栏指标、Working Backwards PRFAQ、RAID 项目管理。

ProductForge 明确不进入开发阶段：不生成架构方案、工程任务、实现故事、生产代码、测试代码或代码评审。需要工程交付时，ProductForge 只输出产品侧交接摘要。

Codex 中使用 `$` 前缀：

```text
Codex: $pf-intake ...
不是: /pf-intake ...
```

## 1. 工作台结构

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
  projects/<project-slug>/
    project-plan.md
    raid-log.md
    stakeholder-update.md
    decision-log.md
    launch-readiness.md
    acceptance-tracker.md
  references/
```

核心原则：`SPEC.md` 是机器契约，PRD、产品原型演示、项目管理、评审和验收都围绕稳定 capability ID 展开，例如 `CAP-1`。

### 1.1 质量门禁

ProductForge 的专业度来自可审查产物，而不是继续增加命令数量：

| 能力 | 合格字段 |
|---|---|
| `$pf-discovery` | outcome、opportunity、solution、assumption test、evidence quality、decision rule |
| `$pf-metrics` | North Star、input metrics、guardrails、baseline、target、owner、review cadence |
| `$pf-narrative` | press release、customer FAQ、internal FAQ、risks、rejected alternatives、open questions |
| `$pf-project` | RAID escalation rule、stakeholder update cadence、decision log、launch readiness gate、acceptance progress state |

## 2. 推荐主流程

### 2.1 初始化工作台

```text
$pf-init 当前项目是大模型聚合平台，需要管理模型、资源池、货源、客户折扣、渠道报价、计费和异步任务。
```

产物：`.product/PRODUCT.md`、`REQUIREMENTS.md`、`ROADMAP.md`、`STATE.md`、`config.yaml`。

### 2.2 需求录入

```text
$pf-intake 我们需要做一个模型价格中心，不同渠道商有不同折扣，客户报价也不同，还要看毛利。
```

目标：分离用户问题、业务目标、拟议方案、范围、风险和待确认问题。建议产物是 `00-intake.md`。

### 2.3 持续发现

```text
$pf-discovery 为模型价格中心建立机会树，梳理客户机会、方案假设和需要验证的实验。
```

目标：先验证用户机会和关键假设，再进入路线图或规格定义。产物包括 `.product/DISCOVERY.md`、`discovery.md`、`opportunity-solution-tree.md`。

### 2.4 调研

```text
$pf-research 调研 OpenRouter、LiteLLM、云厂商模型平台的模型价格和路由管理能力，输出对模型价格中心的设计启发。
```

目标：不是写竞品摘要，而是把竞品、替代方案、用户场景转成产品决策输入。需要最新事实时应联网核对并标注日期。

### 2.5 产品策略、优先级和路线图

```text
$pf-roadmap 基于模型价格中心、资源池路由和渠道报价三个方向，做一期优先级和路线图取舍。
```

目标：把需求池、调研结论、业务目标和约束转成可解释的优先级矩阵、路线图选项和取舍理由。产物是 `.product/PRIORITIZATION.md` 和 `.product/ROADMAP.md`。

### 2.6 指标设计

```text
$pf-metrics 为模型价格中心定义 North Star 贡献、输入指标、护栏指标、上线观察指标和复盘节奏。
```

目标：把成功标准从“做完功能”变成“有可观察的客户价值和业务结果”。产物是 `.product/METRICS.md` 和功能级 `metrics.md`。

### 2.7 客户反向叙事

```text
$pf-narrative 为模型价格中心写 PRFAQ，包含客户 FAQ、内部 FAQ、风险和未解问题。
```

目标：在写 PRD 前用客户语言验证产品价值和干系人共识。产物是 `PRFAQ.md` 和 `narrative.md`。

### 2.8 功能定义

```text
$pf-define 模型价格中心，需要支持模型基础成本、渠道成本、客户报价、折扣、毛利预警和价格生效时间。
```

目标：锁定功能目标、用户与 jobs、实体字段、状态、权限、业务规则、异常和依赖。建议产物是 `02-define.md`。

### 2.9 生成 Product Spec

```text
$pf-spec 为模型价格中心生成 SPEC.md，要求覆盖供应商成本、客户折扣、渠道报价、毛利率、价格审批和生效记录。
```

`SPEC.md` 默认包含：

- problem
- users/jobs
- capabilities with `intent` and `success`
- constraints
- non-goals
- business rules
- states
- success signals
- assumptions
- open questions
- companions

复杂字段表、权限矩阵、状态机可以放到 companion 文件，例如 `entities.md`、`permissions.md`、`state-machine.md`。

### 2.10 写 PRD

```text
$pf-prd 为模型价格中心写 PRD，要求基于 SPEC.md 展开，并保留 capability traceability。
```

默认产物：`.product/features/<feature-slug>/docs/prd.md`。如果没有 `SPEC.md`，`$pf-prd` 应先建议运行 `$pf-spec`，除非用户明确要求 fast path。

### 2.11 生成产品原型演示

```text
$pf-prototype 为资源池动态路由策略生成产品原型演示，展示客户折扣、货源等级、毛利保护、探测风险和路由结果预览。
```

原型默认是多文件结构：

```text
prototype/
  index.html
  styles.css
  app.js
  data/sample-data.json
  data/copy.zh-CN.json
  spec/product-spec.json
```

要求：

- 关键区域、表格、表单、按钮、弹窗、筛选器必须有稳定 `data-pm-id`。
- `product-spec.json` 应记录 pages、entities、statuses、actions、permissions 和 capability 映射。
- 不接真实 API，不引入后端，不作为开发阶段入口。
- 至少有一个主流程可点击演示，并覆盖空、加载、异常、禁用、成功反馈。

### 2.12 版本计划

```text
$pf-plan 规划模型价格中心一期上线，要求先支持内部运营配置，再支持渠道报价。
```

目标：拆里程碑、依赖、风险、验收负责人、灰度策略、回滚条件、上线检查项和上线后观察指标。

### 2.13 项目管理推进

```text
$pf-project 为模型价格中心一期建立项目管理节奏，跟踪里程碑、RAID、干系人沟通、上线准备和验收推进。
```

目标：维护 `.product/projects/<project-slug>/` 下的项目计划、RAID 日志、干系人更新、决策记录、上线准备清单和验收推进表。所有事项以产品结果、负责人和证据为单位，不拆开发任务。

### 2.14 产品评审

```text
$pf-review 审查 .product/features/resource-pool-routing/SPEC.md 和产品原型演示，重点看客户折扣和货源分层逻辑是否完整。
```

输出必须 findings first，按 P0、P1、P2、P3 排序。

### 2.15 验收

```text
$pf-accept 为模型价格中心生成验收清单，要求覆盖报价生效、毛利预警、审批和历史价格回溯。
```

验收必须覆盖 capability ID、业务规则、角色权限、状态流转、异常场景、产品原型演示、上线门禁和证据要求。

### 2.16 复盘

```text
$pf-retro 复盘资源池动态路由策略，本次新增客户折扣、货源等级和探测风险后，还有哪些后续需求需要进入需求池？
```

目标：沉淀关键决策、偏离原计划、产品模式、项目管理节奏、未解决问题、后续需求和模板改进。

## 3. 命令速查

| 命令 | 用途 | 典型产物 |
|---|---|---|
| `$pf-help` | 推荐下一步 | 命令建议 |
| `$pf-init` | 初始化产品工作台 | `.product/PRODUCT.md`、`ROADMAP.md`、`STATE.md`、`config.yaml` |
| `$pf-intake` | 需求录入与澄清 | `00-intake.md`、需求池条目 |
| `$pf-discovery` | 持续发现和机会树 | `DISCOVERY.md`、`opportunity-solution-tree.md` |
| `$pf-research` | 竞品/市场/用户研究 | `01-research.md` |
| `$pf-roadmap` | 产品策略、优先级和路线图 | `PRIORITIZATION.md`、`ROADMAP.md` |
| `$pf-metrics` | 产品指标体系 | `METRICS.md`、`metrics.md` |
| `$pf-narrative` | 客户反向叙事 | `PRFAQ.md`、`narrative.md` |
| `$pf-define` | 定义功能范围 | `02-define.md` |
| `$pf-spec` | 生成产品 spec 内核 | `SPEC.md`、companion files |
| `$pf-prd` | 写 PRD | `docs/prd.md` |
| `$pf-prototype` | 生成产品原型演示 | 原型文件、mock data、product spec |
| `$pf-plan` | 做版本/交付计划 | 里程碑、依赖、风险、上线清单 |
| `$pf-project` | 产品侧项目管理 | RAID、干系人更新、上线准备、验收推进 |
| `$pf-review` | 产品评审 | P0/P1/P2/P3 问题清单 |
| `$pf-accept` | 验收设计 | UAT、验收标准、证据要求 |
| `$pf-retro` | 复盘沉淀 | 决策、经验、后续需求 |

## 4. 安装和校验

安装到 Codex Skills：

```bash
node bin/product-forge.js install --target codex --home ~/.codex
```

校验本地技能包：

```bash
node bin/product-forge.js validate --source skills
python3 skills/product-forge/scripts/validate_product_forge.py
```

查看命令：

```bash
node bin/product-forge.js list --source skills
```

## 5. 领域包

涉及大模型聚合平台、模型路由、资源池、渠道报价、客户折扣、供应商、结算和毛利时，优先结合 `pm-llm-platform` 领域知识使用 ProductForge。
