#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_SKILLS = [
    "product-forge",
    "pm-help",
    "pm-init",
    "pm-intake",
    "pm-discovery",
    "pm-research",
    "pm-roadmap",
    "pm-metrics",
    "pm-narrative",
    "pm-define",
    "pm-spec",
    "pm-prd",
    "pm-prototype",
    "pm-plan",
    "pm-project",
    "pm-review",
    "pm-accept",
    "pm-retro",
]

REQUIRED_PRODUCT_FILES = [
    ".product/PRODUCT.md",
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
    "p" + "f-help",
    "p" + "f-init",
    "p" + "f-intake",
    "p" + "f-discovery",
    "p" + "f-research",
    "p" + "f-roadmap",
    "p" + "f-metrics",
    "p" + "f-narrative",
    "p" + "f-define",
    "p" + "f-spec",
    "p" + "f-prd",
    "p" + "f-prototype",
    "p" + "f-plan",
    "p" + "f-project",
    "p" + "f-review",
    "p" + "f-accept",
    "p" + "f-retro",
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
    "interaction-protocol.md",
    "methodology.md",
    "method-library.md",
    "project-workspace.md",
    "prototype-demo.md",
    "review-checklist.md",
    "usage-guide.md",
    "domain-packages.md",
]

INTERACTIVE_SKILL_TOKENS = [
    "interaction-protocol.md",
    "boundary question",
    "three options",
    "请回复 a / b / c",
]

REQUIRED_CONTENT = {
    "pm-discovery/SKILL.md": [
        "outcome",
        "opportunity",
        "solution",
        "assumption test",
        "evidence quality",
        "decision rule",
    ],
    "pm-metrics/SKILL.md": [
        "north star",
        "input metrics",
        "guardrails",
        "baseline",
        "target",
        "owner",
        "review cadence",
    ],
    "pm-narrative/SKILL.md": [
        "press release",
        "customer faq",
        "internal faq",
        "risks",
        "rejected alternatives",
        "open questions",
    ],
    "pm-project/SKILL.md": [
        "raid escalation rule",
        "stakeholder update cadence",
        "decision log",
        "launch readiness gate",
        "acceptance progress state",
    ],
    "product-forge/SKILL.md": [
        "interaction-protocol.md",
        "boundary question",
        "stage-only",
        "lazy generation",
    ],
    "product-forge/references/interaction-protocol.md": [
        "exactly one high-leverage boundary question",
        "exactly three mutually exclusive options",
        "do not generate formal artifacts before the user chooses",
        "stage-only generation",
        "请回复 a / b / c",
    ],
    "product-forge/scripts/init_product_workspace.py": [
        "boundary_confirmation",
        "question_format",
        "workspace_init: minimal",
        "feature_pack: stage-only",
        "project_pack: stage-only",
        "Assumption Test",
        "Evidence Quality",
        "Decision Rule",
        "Baseline",
        "Target",
        "Review Cadence",
    ],
    "product-forge/scripts/init_feature_pack.py": [
        "--stage",
        "\"all\"",
        "--include-shared",
        "Assumption Test",
        "Evidence Quality",
        "Decision Rule",
        "Rejected Alternatives",
        "Baseline",
        "Target",
        "Review Cadence",
    ],
    "product-forge/scripts/init_project_pack.py": [
        "--stage",
        "\"all\"",
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


def check_interactive_skills(base: Path, problems: list[str], missing: list[str]) -> None:
    for skill in REQUIRED_SKILLS:
        if not skill.startswith("pm-"):
            continue
        path = base / skill / "SKILL.md"
        if not path.exists():
            missing.append(str(path))
            continue
        text = path.read_text(encoding="utf-8").lower()
        for token in INTERACTIVE_SKILL_TOKENS:
            if token not in text:
                problems.append(f"{path}: missing interactive workflow token {token!r}")


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
    check_interactive_skills(base, problems, missing)

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
