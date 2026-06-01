#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_SKILLS = [
    "product-gsd",
    "pgd-new-product",
    "pgd-intake",
    "pgd-research",
    "pgd-define-feature",
    "pgd-write-prd",
    "pgd-prototype",
    "pgd-plan-release",
    "pgd-review",
    "pgd-acceptance",
    "pgd-retro",
]

REQUIRED_PRODUCT_FILES = [
    ".product/PRODUCT.md",
    ".product/REQUIREMENTS.md",
    ".product/ROADMAP.md",
    ".product/STATE.md",
]


def find_skill_base(root: Path) -> Path:
    repo_layout = root / "skills"
    workspace_layout = root / ".product" / "skill-pack"
    if (repo_layout / "product-gsd" / "SKILL.md").exists():
        return repo_layout
    return workspace_layout


def main() -> int:
    root = Path.cwd()
    base = find_skill_base(root)
    missing = []

    for skill in REQUIRED_SKILLS:
        path = base / skill / "SKILL.md"
        if not path.exists():
            missing.append(str(path))

    if (root / ".product").exists():
        for file in REQUIRED_PRODUCT_FILES:
            path = root / file
            if not path.exists():
                missing.append(str(path))

    demo = base / "product-gsd" / "assets" / "templates" / "prototype-demo"
    for rel in ["index.html", "styles.css", "app.js", "data/sample-data.json", "data/copy.zh-CN.json", "spec/product-spec.json"]:
        if not (demo / rel).exists():
            missing.append(str(demo / rel))

    if missing:
        print("Validation failed. Missing files:")
        for item in missing:
            print("-", item)
        return 1

    print(f"Validation passed: Product GSD skill pack is complete at {base}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
