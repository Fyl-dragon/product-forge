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
    "ROADMAP.md": """# 路线图

| 阶段 | 目标 | 主要交付 | 状态 |
|---|---|---|---|
""",
    "STATE.md": """# 产品工作台状态

## 当前状态

TODO

## 已锁定决策

TODO

## 开放问题

TODO
""",
}


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Product GSD workspace.")
    parser.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    product = root / ".product"
    created = []

    for subdir in ["features", "references"]:
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

