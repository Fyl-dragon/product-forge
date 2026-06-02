#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_SKILLS = [
    "product-forge",
    "pf-help",
    "pf-init",
    "pf-intake",
    "pf-discovery",
    "pf-research",
    "pf-roadmap",
    "pf-metrics",
    "pf-narrative",
    "pf-define",
    "pf-spec",
    "pf-prd",
    "pf-prototype",
    "pf-plan",
    "pf-project",
    "pf-review",
    "pf-accept",
    "pf-retro",
]

REQUIRED_PRODUCT_FILES = [
    ".product/PRODUCT.md",
    ".product/REQUIREMENTS.md",
    ".product/DISCOVERY.md",
    ".product/PRIORITIZATION.md",
    ".product/METRICS.md",
    ".product/ROADMAP.md",
    ".product/STATE.md",
    ".product/config.yaml",
]

FORBIDDEN_SKILL_DIRS = [
    "product-" + "gsd",
    "p" + "gd-new-product",
    "p" + "gd-intake",
    "p" + "gd-research",
    "p" + "gd-define-feature",
    "p" + "gd-write-prd",
    "p" + "gd-prototype",
    "p" + "gd-plan-release",
    "p" + "gd-review",
    "p" + "gd-acceptance",
    "p" + "gd-retro",
]

PROJECT_TEMPLATE_FILES = [
    "project-plan.md",
    "raid-log.md",
    "stakeholder-update.md",
    "decision-log.md",
    "launch-readiness.md",
    "acceptance-tracker.md",
]

REQUIRED_REFERENCES = [
    "methodology.md",
    "method-library.md",
    "project-workspace.md",
    "prototype-demo.md",
    "review-checklist.md",
    "usage-guide.md",
    "domain-packages.md",
]

REQUIRED_CONTENT = {
    "pf-discovery/SKILL.md": [
        "outcome",
        "opportunity",
        "solution",
        "assumption test",
        "evidence quality",
        "decision rule",
    ],
    "pf-metrics/SKILL.md": [
        "north star",
        "input metrics",
        "guardrails",
        "baseline",
        "target",
        "owner",
        "review cadence",
    ],
    "pf-narrative/SKILL.md": [
        "press release",
        "customer faq",
        "internal faq",
        "risks",
        "rejected alternatives",
        "open questions",
    ],
    "pf-project/SKILL.md": [
        "raid escalation rule",
        "stakeholder update cadence",
        "decision log",
        "launch readiness gate",
        "acceptance progress state",
    ],
    "product-forge/scripts/init_product_workspace.py": [
        "Assumption Test",
        "Evidence Quality",
        "Decision Rule",
        "Baseline",
        "Target",
        "Review Cadence",
    ],
    "product-forge/scripts/init_feature_pack.py": [
        "Assumption Test",
        "Evidence Quality",
        "Decision Rule",
        "Rejected Alternatives",
        "Baseline",
        "Target",
        "Review Cadence",
    ],
    "product-forge/scripts/init_project_pack.py": [
        "Escalation Rules",
        "Update Cadence",
        "Decision Requests",
        "Readiness Gate Summary",
        "Status Rules",
    ],
    "product-forge/assets/templates/project-pack/raid-log.md": [
        "Escalation Rules",
        "Severity",
        "Trigger",
        "Decision Needed",
    ],
    "product-forge/assets/templates/project-pack/stakeholder-update.md": [
        "Update Cadence",
        "Audience",
        "Decision Requests",
    ],
    "product-forge/assets/templates/project-pack/decision-log.md": [
        "Decision Type",
        "Status",
        "Evidence",
        "Revisit Condition",
    ],
    "product-forge/assets/templates/project-pack/launch-readiness.md": [
        "Readiness Gate Summary",
        "PASS/CONCERN/FAIL",
        "Required Evidence",
        "Actual Evidence",
    ],
    "product-forge/assets/templates/project-pack/acceptance-tracker.md": [
        "Status Rules",
        "Evidence Ready",
        "Business Rule / Permission / State Coverage",
    ],
    "product-forge/references/method-library.md": [
        "outcome",
        "assumption test",
        "baseline",
        "target",
        "rejected alternatives",
        "RAID escalation rules",
        "launch readiness gate",
    ],
}


def find_skill_base(root: Path) -> Path:
    repo_layout = root / "skills"
    workspace_layout = root / ".product" / "skill-pack"
    if (repo_layout / "product-forge" / "SKILL.md").exists():
        return repo_layout
    return workspace_layout


def frontmatter_name(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    return None


def check_required_content(base: Path, problems: list[str], missing: list[str]) -> None:
    for rel, tokens in REQUIRED_CONTENT.items():
        path = base / rel
        if not path.exists():
            missing.append(str(path))
            continue
        text = path.read_text(encoding="utf-8").lower()
        for token in tokens:
            if token.lower() not in text:
                problems.append(f"{path}: missing required method/template field {token!r}")


def main() -> int:
    root = Path.cwd()
    base = find_skill_base(root)
    missing = []
    problems = []

    for skill in REQUIRED_SKILLS:
        path = base / skill / "SKILL.md"
        if not path.exists():
            missing.append(str(path))
            continue
        declared = frontmatter_name(path)
        if declared != skill:
            problems.append(f"{path}: frontmatter name is {declared!r}, expected {skill!r}")

    for skill in FORBIDDEN_SKILL_DIRS:
        if (base / skill).exists():
            problems.append(f"Forbidden old skill directory remains: {base / skill}")

    if (root / ".product").exists():
        for file in REQUIRED_PRODUCT_FILES:
            path = root / file
            if not path.exists():
                missing.append(str(path))

    demo = base / "product-forge" / "assets" / "templates" / "prototype-demo"
    for rel in ["index.html", "styles.css", "app.js", "data/sample-data.json", "data/copy.zh-CN.json", "spec/product-spec.json"]:
        if not (demo / rel).exists():
            missing.append(str(demo / rel))

    project_demo = base / "product-forge" / "assets" / "templates" / "project-pack"
    for rel in PROJECT_TEMPLATE_FILES:
        if not (project_demo / rel).exists():
            missing.append(str(project_demo / rel))

    reference_root = base / "product-forge" / "references"
    for rel in REQUIRED_REFERENCES:
        if not (reference_root / rel).exists():
            missing.append(str(reference_root / rel))

    check_required_content(base, problems, missing)

    if missing or problems:
        print("Validation failed. Missing files:")
        for item in missing:
            print("-", item)
        if problems:
            print("Validation failed. Problems:")
            for item in problems:
                print("-", item)
        return 1

    print(f"Validation passed: ProductForge skill pack is complete at {base}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
