#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def slugify(text: str) -> str:
    safe = []
    for char in text.strip().lower():
        if char.isalnum():
            safe.append(char)
        elif char in [" ", "_", "-", "/", "：", ":"]:
            safe.append("-")
    slug = "".join(safe).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "new-feature"


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Product GSD feature pack.")
    parser.add_argument("name", help="Feature name.")
    parser.add_argument("--slug", help="Feature slug. Defaults to generated slug.")
    parser.add_argument("--root", default=".", help="Project root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = args.slug or slugify(args.name)
    feature = root / ".product" / "features" / slug

    write_if_missing(feature / "docs" / "prd.md", f"# {args.name} PRD\n\n## 1. 背景与问题\n\n## 2. 目标与非目标\n\n## 3. 用户与场景\n\n## 4. 功能范围\n\n## 5. 验收标准\n")
    write_if_missing(feature / "research.md", f"# {args.name} 研究\n\n")
    write_if_missing(feature / "acceptance.md", f"# {args.name} 验收\n\n")
    write_if_missing(feature / "source-map.md", f"# {args.name} 来源映射\n\n")
    write_if_missing(feature / "prototype" / "index.html", "<!doctype html>\n<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Prototype Demo</title><link rel=\"stylesheet\" href=\"./styles.css\"></head><body><div id=\"app\" data-pm-id=\"app.root\"></div><script src=\"./app.js\"></script></body></html>\n")
    write_if_missing(feature / "prototype" / "styles.css", "body{margin:0;font-family:\"Avenir Next\",\"PingFang SC\",sans-serif;background:#f6f3ed;color:#1f2a24}.app{padding:24px}.card{background:#fffaf1;border:1px solid #ddd3c2;border-radius:16px;padding:20px}\n")
    write_if_missing(feature / "prototype" / "app.js", "document.querySelector('#app').innerHTML='<main class=\"app\" data-pm-id=\"prototype.main\"><section class=\"card\" data-pm-id=\"prototype.card\"><h1>Prototype Demo</h1><p>请基于 PRD、sample-data 和 product-spec 扩展此 Demo。</p></section></main>';\n")
    write_if_missing(feature / "prototype" / "data" / "sample-data.json", json.dumps({"records": []}, ensure_ascii=False, indent=2) + "\n")
    write_if_missing(feature / "prototype" / "data" / "copy.zh-CN.json", json.dumps({"title": args.name}, ensure_ascii=False, indent=2) + "\n")
    write_if_missing(feature / "prototype" / "spec" / "product-spec.json", json.dumps({"pages": [], "entities": [], "statuses": [], "actions": [], "permissions": []}, ensure_ascii=False, indent=2) + "\n")
    (feature / "versions").mkdir(parents=True, exist_ok=True)

    print(feature)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

