# PGD 使用手册

PGD 是面向产品经理的 AI 工作流框架，可以理解为“产品经理版 GSD”。GSD 更偏工程交付，PGD 更偏产品工作：需求澄清、竞品分析、PRD、Prototype Demo、项目计划、评审、验收、复盘。

如果你在 Codex 里使用，命令前缀使用 `$`，不要使用 `/`。

```text
Codex: $pgd-new-product ...
不是: /pgd-new-product ...
```

## 1. PGD 的整体架构

PGD 的核心结构是：

```text
product workspace
  milestone
    feature / phase
      deliverables
        PRD
        Prototype Demo
        research
        acceptance
        retro
```

在当前项目中，PGD 的持久化工作台是 `.product/`：

```text
.product/
  PRODUCT.md          产品定位、用户、商业模式、核心模块
  REQUIREMENTS.md     需求池
  ROADMAP.md          版本/里程碑路线图
  STATE.md            当前状态、已锁定决策、开放问题
  features/           单功能工作区
  references/         竞品、访谈、行业资料、领域资料
```

PGD 和 GSD 的概念对应关系：

| GSD 概念 | PGD 概念 | 说明 |
|---|---|---|
| milestone | milestone / 版本需求 | 管理一组产品目标和功能，不直接产出开发动作 |
| phase | feature / phase | 一个可被讨论、定义、写 PRD、做原型、验收的产品阶段 |
| wave | AI 自动执行批次 | 不需要人工管理，PGD 内部自动完成资料读取、草稿生成、校验 |

## 2. 什么时候用 PGD

适合使用 PGD 的场景：

- 你有一段口述需求，需要整理成正式产品需求。
- 你要做竞品分析，并希望分析结果能直接影响 PRD。
- 你要写 PRD，不只是写文案，而是把业务规则、字段、状态、权限、验收标准都补齐。
- 你要做可演示原型，要求比静态 HTML 更强，但不需要真实开发项目。
- 你要管理一个版本的多个功能，跟踪哪些已经讨论、哪些已经写 PRD、哪些已经验收。
- 你要复盘产品决策，把经验沉淀下来，后续 AI 能继续沿用。

## 3. 推荐主流程

### 3.1 初始化产品工作台

```text
$pgd-new-product [产品背景或版本目标]
```

作用：

- 初始化 `.product/`
- 创建或更新 `PRODUCT.md`
- 创建或更新 `REQUIREMENTS.md`
- 创建或更新 `ROADMAP.md`
- 创建或更新 `STATE.md`
- 盘点现有 `docs/` 文档并映射到 `.product/features/`

示例：

```text
$pgd-new-product 当前项目是大模型聚合平台，需要管理模型、资源池、货源、客户折扣、渠道报价、计费和异步任务。
```

### 3.2 需求录入和澄清

```text
$pgd-intake [你的原始需求]
```

作用：

- 把零散需求整理成结构化需求。
- 区分“用户问题”和“你提出的解决方案”。
- 明确目标用户、业务目标、核心场景、范围、非目标、风险、待确认问题。
- 必要时写入 `.product/REQUIREMENTS.md`。

示例：

```text
$pgd-intake 我们需要做一个模型价格中心，不同渠道商有不同折扣，客户报价也不同，还要看毛利。
```

### 3.3 竞品和方案调研

```text
$pgd-research [调研问题]
```

作用：

- 做竞品分析、市场分析、用户场景分析。
- 输出对比矩阵。
- 把调研结论转成产品设计启发，而不是泛泛总结。

示例：

```text
$pgd-research 调研 OpenRouter、LiteLLM、云厂商模型平台的模型价格和路由管理能力，输出对模型价格中心的设计启发。
```

如果你要求“最新价格”“最新模型列表”“最新竞品能力”，需要允许联网核对官方资料，并在结果中标注日期。

### 3.4 定义功能

```text
$pgd-define-feature [功能需求]
```

作用：

- 在正式写 PRD 之前，把功能边界定义清楚。
- 明确用户故事、实体、字段、状态、权限、业务规则、异常场景。
- 创建或更新 `.product/features/<feature-slug>/context.md`。

示例：

```text
$pgd-define-feature 模型价格中心，需要支持模型基础成本、渠道成本、客户报价、折扣、毛利预警和价格生效时间。
```

### 3.5 写 PRD

```text
$pgd-write-prd [功能名或需求说明]
```

默认输出：

```text
.product/features/<feature-slug>/docs/prd.md
```

PRD 默认包含：

- 背景与问题
- 目标与非目标
- 用户与场景
- 功能范围
- 业务规则
- 数据对象与字段
- 权限与角色
- 状态流转
- 页面与交互要求
- 异常与边界
- 验收标准
- 风险与待确认

示例：

```text
$pgd-write-prd 为模型价格中心写 PRD，要求覆盖供应商成本、客户折扣、渠道报价、毛利率、价格审批和生效记录。
```

### 3.6 生成 Prototype Demo

```text
$pgd-prototype [功能名或原型要求]
```

PGD 的原型不是单个静态 HTML，而是轻量 Prototype Demo：

```text
.product/features/<feature-slug>/prototype/
  index.html
  styles.css
  app.js
  data/
    sample-data.json
    copy.zh-CN.json
  spec/
    product-spec.json
```

各文件职责：

| 文件 | 职责 |
|---|---|
| `index.html` | 页面壳、CSS/JS 加载、根容器 |
| `styles.css` | 视觉系统、布局、响应式、状态样式 |
| `app.js` | 页面渲染、路由、筛选、弹窗、状态切换、mock 交互 |
| `sample-data.json` | 真实感 mock 数据 |
| `copy.zh-CN.json` | 可编辑 UI 文案 |
| `product-spec.json` | 页面、组件、实体、字段、状态、动作、权限 |

原型要求：

- 关键区域、表格、表单、按钮、弹窗、筛选器必须有稳定 `data-pm-id`。
- 至少有一个主流程可点击演示。
- 要覆盖空状态、加载、异常、禁用、成功反馈。
- 不接真实 API，不引入后端。
- 比静态原型更强，但比开发项目更轻。

示例：

```text
$pgd-prototype 为资源池动态路由策略生成 Prototype Demo，展示客户折扣、货源等级、毛利保护、探测风险和路由结果预览。
```

### 3.7 做版本/项目计划

```text
$pgd-plan-release [版本目标或功能名]
```

作用：

- 拆里程碑。
- 明确依赖、风险、验收负责人、灰度策略、回滚条件。
- 生成上线检查项和上线后观察指标。

示例：

```text
$pgd-plan-release 规划模型价格中心一期上线，要求先支持内部运营配置，再支持渠道报价。
```

### 3.8 产品评审

```text
$pgd-review [PRD、原型或功能名]
```

作用：

- 用产品评审视角检查问题。
- 重点找逻辑缺口、字段缺失、状态缺失、权限问题、商业风险、验收不清。
- 默认按严重级别输出：P0、P1、P2、P3。

示例：

```text
$pgd-review 审查 .product/features/resource-pool-routing/docs/prd.md 和 prototype，重点看客户折扣和货源分层逻辑是否完整。
```

### 3.9 验收

```text
$pgd-acceptance [功能名]
```

作用：

- 生成验收标准。
- 生成 UAT 场景。
- 明确验收证据。
- 覆盖角色权限、状态流转、异常场景、数据展示和 Prototype Demo 验收。

示例：

```text
$pgd-acceptance 为模型价格中心生成验收清单，要求覆盖报价生效、毛利预警、审批和历史价格回溯。
```

### 3.10 复盘

```text
$pgd-retro [功能名或复盘内容]
```

作用：

- 沉淀关键决策。
- 记录偏离原计划的地方。
- 记录后续需求。
- 更新 `.product/STATE.md`。

示例：

```text
$pgd-retro 复盘资源池动态路由策略，本次新增客户折扣、货源等级和探测风险后，还有哪些后续需求需要进入需求池？
```

## 4. 里程碑管理建议

PGD 当前没有完全复制 GSD 的 milestone 命令体系，但推荐用 `.product/ROADMAP.md` 管理版本需求。

建议把一个 milestone 理解为一个版本，例如：

```text
M1 文档治理与产品工作台
M2 资源池动态路由专业化
M3 模型价格与渠道报价
M4 可演示 Prototype Demo
```

里程碑本身不直接产出 PRD 或原型，它负责管理一组 feature / phase。

推荐操作方式：

```text
$pgd-new-product [版本目标]
$pgd-intake [版本中的原始需求]
$pgd-define-feature [拆出的功能 1]
$pgd-define-feature [拆出的功能 2]
$pgd-plan-release [这个版本的交付计划]
```

在关闭一个版本前，建议执行：

```text
$pgd-review [本版本所有 PRD 和 Prototype Demo]
$pgd-acceptance [本版本核心功能]
$pgd-retro [本版本复盘]
```

## 5. 阶段管理建议

如果你已经知道某个版本要做哪些功能，可以直接手动创建 feature / phase。

推荐顺序：

```text
$pgd-intake [原始需求]
$pgd-research [需要调研的问题]
$pgd-define-feature [功能定义]
$pgd-write-prd [功能 PRD]
$pgd-prototype [功能 Prototype Demo]
$pgd-plan-release [交付计划]
$pgd-review [产品评审]
$pgd-acceptance [验收清单]
$pgd-retro [复盘]
```

如果是大模型聚合平台相关需求，例如资源池、模型接入、价格中心、渠道报价、供应商、CRM/RPM、结算，需要同时使用领域包：

```text
$pm-llm-platform + $pgd-write-prd 为渠道报价配置写 PRD
```

或者直接说明：

```text
$pgd-write-prd 使用 pm-llm-platform 的领域知识，为模型价格中心写 PRD
```

## 6. 常用命令速查

| 命令 | 用途 | 典型输出 |
|---|---|---|
| `$pgd-new-product` | 初始化产品工作台 | `.product/PRODUCT.md`、`ROADMAP.md`、`STATE.md` |
| `$pgd-intake` | 需求录入与澄清 | 结构化需求、开放问题、需求池条目 |
| `$pgd-research` | 竞品/市场/用户研究 | 对比矩阵、设计启发、产品决策 |
| `$pgd-define-feature` | 定义功能范围 | `context.md`、实体、字段、状态、权限 |
| `$pgd-write-prd` | 写 PRD | `docs/prd.md` |
| `$pgd-prototype` | 生成 Prototype Demo | `index.html`、`styles.css`、`app.js`、mock data、spec |
| `$pgd-plan-release` | 做版本/交付计划 | 里程碑、依赖、风险、上线清单 |
| `$pgd-review` | 产品评审 | P0/P1/P2/P3 问题清单 |
| `$pgd-acceptance` | 验收设计 | UAT、验收标准、证据要求 |
| `$pgd-retro` | 复盘沉淀 | 决策、经验、后续需求 |

## 7. 当前项目推荐用法

当前项目是大模型聚合平台，建议先按这个顺序推进：

```text
$pgd-review 审查 docs/功能文档/资源池动态路由策略/当前方案.html，重点看客户折扣、货源分层、毛利保护和客户探测风险。
```

```text
$pgd-write-prd 使用 pm-llm-platform 领域知识，将资源池动态路由策略整理为 .product/features/resource-pool-routing/docs/prd.md。
```

```text
$pgd-prototype 为资源池动态路由策略生成 Prototype Demo，要求拆分 index.html、styles.css、app.js、sample-data.json、copy.zh-CN.json、product-spec.json。
```

```text
$pgd-acceptance 为资源池动态路由策略生成验收清单，覆盖不同客户折扣、不同货源等级、毛利下限、探测风险和路由审计。
```

## 8. 注意事项

- PGD 不是让 AI 一次性替你“想完全部产品”，而是把产品工作拆成可持续维护的上下文和交付物。
- 不要只让 AI 输出一篇 PRD；优先让它同时维护 `.product/` 结构。
- Prototype Demo 默认是演示工具，不是生产代码。
- 涉及最新价格、云厂商、模型目录、竞品能力时，要显式要求联网核对并标注日期。
- 涉及大模型聚合平台时，优先让 PGD 读取 `pm-llm-platform` 领域知识。

