#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


ROOT_FILES = {
    "PRODUCT.md": """# 产品说明

## 产品定位

TODO

## 目标用户

TODO

## 业务模式

TODO

## 核心模块

TODO
""",
    "REQUIREMENTS.md": """# 需求池

| ID | 需求 | 来源 | 模块 | 优先级 | 状态 | 备注 |
|---|---|---|---|---|---|---|
""",
    "DISCOVERY.md": """# 持续发现

## 当前发现目标

TODO

## 机会树质量标准

| Outcome | Opportunity | Solution | Assumption Test | Evidence Quality | Decision Rule |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

## 客户机会

| ID | 客户机会 | 关联 Outcome | 证据 | Evidence Quality | 影响 | 信心 | 状态 |
|---|---|---|---|---|---|---|---|

## 假设与实验

| ID | 假设 | Assumption Test | 需要证据 | 成功信号 | Decision Rule | 负责人 | 状态 |
|---|---|---|---|---|---|---|---|
""",
    "PRIORITIZATION.md": """# 优先级与机会评估

## 产品目标

TODO

## 机会池

| ID | 机会 | 用户/场景 | 影响 | 信心 | 成本 | 优先级 | 备注 |
|---|---|---|---|---|---|---|---|

## 取舍说明

TODO
""",
    "METRICS.md": """# 产品指标

## North Star

TODO

## 指标质量标准

| Metric Layer | Metric | 定义 | Baseline | Target | Owner | Review Cadence |
|---|---|---|---|---|---|---|
| North Star | TODO | TODO | TODO | TODO | TODO | TODO |

## 输入指标

| Metric | 定义 | 来源 | Baseline | Target | Owner | Review Cadence |
|---|---|---|---|---|---|---|

## 护栏指标

| Metric | Guardrail Risk | Baseline | Threshold | Owner | Review Cadence |
|---|---|---|---|---|---|

## 上线观察

TODO
""",
    "ROADMAP.md": """# 路线图

| 阶段 | 产品目标 | 范围 | 成功信号 | 状态 |
|---|---|---|---|---|
""",
    "STATE.md": """# ProductForge 状态

## 当前状态

TODO

## 当前 Feature

TODO

## 当前阶段

TODO

## 下一步建议

TODO

## 已锁定决策

TODO

## 开放问题

TODO
""",
    "config.yaml": """product_name: TODO
communication_language: Chinese
document_output_language: Chinese
rigor: standard
artifact_paths:
  product_root: .product
  features: .product/features
  projects: .product/projects
workflow_gates:
  research: true
  review: true
  acceptance: true
targets:
  codex: true
""",
}


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a ProductForge workspace.")
    parser.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    product = root / ".product"
    created = []

    for subdir in ["features", "projects", "references"]:
        (product / subdir).mkdir(parents=True, exist_ok=True)

    for name, content in ROOT_FILES.items():
        if write_if_missing(product / name, content):
            created.append(str(product / name))

    print("Product workspace ready:", product)
    if created:
        print("Created:")
        for item in created:
            print("-", item)
    else:
        print("No root files created; existing files were preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
