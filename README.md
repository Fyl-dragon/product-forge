# ProductForge

ProductForge 是面向产品经理的 AI 工作流技能框架，可以理解为产品经理版 GSD。

它把产品工作拆成可持续维护的流程和资产：

- 需求录入与澄清
- 竞品/市场/用户研究
- 功能定义
- PRD 编写
- Prototype Demo 生成
- 版本/项目计划
- 产品评审
- 验收设计
- 复盘沉淀

## 目录结构

```text
skills/
  product-gsd/
  pgd-new-product/
  pgd-intake/
  pgd-research/
  pgd-define-feature/
  pgd-write-prd/
  pgd-prototype/
  pgd-plan-release/
  pgd-review/
  pgd-acceptance/
  pgd-retro/
docs/
  PGD使用手册.md
```

## Codex 使用方式

Codex 中使用 `$` 前缀：

```text
$pgd-new-product [产品背景或版本目标]
$pgd-intake [原始需求]
$pgd-research [调研问题]
$pgd-define-feature [功能需求]
$pgd-write-prd [功能名或需求说明]
$pgd-prototype [功能名或原型要求]
$pgd-plan-release [版本目标或功能名]
$pgd-review [PRD、原型或功能名]
$pgd-acceptance [功能名]
$pgd-retro [功能名或复盘内容]
```

完整说明见 [docs/PGD使用手册.md](docs/PGD使用手册.md)。

## Prototype Demo

ProductForge 默认生成轻量 Prototype Demo，而不是单个静态 HTML：

```text
prototype/
  index.html
  styles.css
  app.js
  data/sample-data.json
  data/copy.zh-CN.json
  spec/product-spec.json
```

目标是比静态原型更强，比真实开发项目更轻，适合产品经理演示、评审和快速迭代。

## 安装到 Codex Skills

仓库根目录执行：

```bash
python3 skills/product-gsd/scripts/install_to_codex_skills.py --source skills --target ~/.codex/skills
```

