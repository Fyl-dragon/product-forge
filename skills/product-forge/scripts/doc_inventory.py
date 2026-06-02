#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path


KEYWORDS = {
    "task-center": ["任务", "异步"],
    "message-center": ["消息"],
    "resource-pool-routing": ["资源池动态路由", "路由策略"],
    "source-pool-usage-dashboard": ["货源", "用量看板"],
    "customer-usage": ["客户用量"],
    "model-call-log": ["调用日志"],
}


def classify(path: Path) -> str:
    text = "/".join(path.parts)
    for slug, words in KEYWORDS.items():
        if any(word in text for word in words):
            return slug
    return path.parent.name


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory product documents and group by feature.")
    parser.add_argument("--docs", default="docs", help="Docs directory.")
    args = parser.parse_args()

    docs = Path(args.docs)
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(docs.rglob("*")):
        if path.is_file() and path.name != ".DS_Store":
            groups[classify(path)].append(path)

    for slug, files in sorted(groups.items()):
        print(f"## {slug}")
        for file in files:
            print(f"- {file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

