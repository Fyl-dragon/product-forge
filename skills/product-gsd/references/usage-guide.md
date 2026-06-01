# Product GSD Usage Guide

完整中文使用手册见项目内 `.product/PGD使用手册.md`。

Codex 中使用 PGD 命令时，使用 `$` 前缀：

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

PGD 的工作台目录是 `.product/`，Prototype Demo 默认是多文件结构：

```text
prototype/
  index.html
  styles.css
  app.js
  data/sample-data.json
  data/copy.zh-CN.json
  spec/product-spec.json
```

