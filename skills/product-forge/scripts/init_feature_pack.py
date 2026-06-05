#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


STAGE_ORDER = [
    "intake",
    "discovery",
    "research",
    "narrative",
    "define",
    "spec",
    "prd",
    "metrics",
    "prototype",
    "acceptance",
    "review",
    "source-map",
]


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


def feature_templates(name: str) -> dict[str, dict[str, str]]:
    return {
        "intake": {
            "00-intake.md": f"# {name} Intake\n\n## 背景\n\n## 目标用户\n\n## 问题定义\n\n## 范围\n\n## 风险\n\n## 待确认问题\n"
        },
        "discovery": {
            "discovery.md": f"""# {name} Discovery

## 发现目标 / Outcome

TODO

## 机会树质量标准

| Outcome | Opportunity | Solution | Assumption Test | Evidence Quality | Decision Rule |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

## 客户机会 / Opportunities

| ID | Opportunity | 用户/场景 | 证据 | Evidence Quality | 影响 | 信心 | 状态 |
|---|---|---|---|---|---|---|---|

## 方案候选 / Solutions

| ID | Solution | Linked Opportunity | 价值假设 | 主要风险 | 状态 |
|---|---|---|---|---|---|

## 假设与 Assumption Tests

| ID | Assumption | Assumption Test | 需要证据 | 成功信号 | Decision Rule | Owner | 状态 |
|---|---|---|---|---|---|---|---|

## Evidence Quality

| Evidence | Type | Source | Freshness | Confidence | Decision Impact |
|---|---|---|---|---|---|

## 决策规则 / Decision Rule

TODO
""",
            "opportunity-solution-tree.md": f"""# {name} Opportunity Solution Tree

## Outcome

TODO

## Opportunities

| ID | Opportunity | Evidence Quality | Linked Outcome | Priority |
|---|---|---|---|---|

## Solutions

| ID | Solution | Linked Opportunity | Key Assumption | Risk |
|---|---|---|---|---|

## Assumption Tests

| ID | Assumption Test | Evidence Needed | Success Signal | Owner | Decision Rule |
|---|---|---|---|---|---|
""",
        },
        "research": {
            "01-research.md": f"# {name} Research\n\n## 调研问题\n\n## 对比矩阵\n\n## 产品决策启发\n\n## 对 SPEC 的影响\n"
        },
        "narrative": {
            "PRFAQ.md": f"""# {name} PRFAQ

## Press Release

TODO

## Customer FAQ

| Question | Answer | Evidence / Source |
|---|---|---|

## Internal FAQ

| Question | Answer | Owner / Evidence |
|---|---|---|

## Risks

| Risk | Type | Impact | Mitigation | Owner |
|---|---|---|---|---|

## Rejected Alternatives

| Alternative | Why Rejected | Tradeoff | Evidence |
|---|---|---|---|

## Open Questions

| Question | Owner | Next Evidence | Decision Deadline |
|---|---|---|---|
"""
        },
        "define": {
            "02-define.md": f"# {name} Define\n\n## 功能目标\n\n## 用户与 Jobs\n\n## 实体与字段\n\n## 状态与流转\n\n## 权限\n\n## 业务规则\n\n## 边界与依赖\n"
        },
        "spec": {
            "SPEC.md": f"""# {name} SPEC

## Problem

TODO

## Users / Jobs

TODO

## Capabilities

| ID | Intent | Success |
|---|---|---|
| CAP-1 | TODO | TODO |

## Constraints

TODO

## Non-goals

TODO

## Business Rules

TODO

## States

TODO

## Success Signals

TODO

## Assumptions

TODO

## Open Questions

TODO

## Companions

TODO
"""
        },
        "prd": {
            "docs/prd.md": f"# {name} PRD\n\n## 1. 背景与问题\n\n## 2. 目标与非目标\n\n## 3. 用户与场景\n\n## 4. Capability Traceability\n\n## 5. 功能范围\n\n## 6. 业务规则\n\n## 7. 数据对象与字段\n\n## 8. 权限与状态\n\n## 9. 验收标准\n"
        },
        "metrics": {
            "metrics.md": f"""# {name} Metrics

## North Star Contribution

| Metric | Customer Value Link | Business Value Link | Baseline | Target | Owner | Review Cadence |
|---|---|---|---|---|---|---|

## Input Metrics

| Metric | Definition | Linked Capability | Baseline | Target | Owner | Review Cadence |
|---|---|---|---|---|---|---|

## Guardrail Metrics

| Metric | Guardrail Risk | Baseline | Threshold | Owner | Review Cadence |
|---|---|---|---|---|---|

## Launch Metrics

| Metric | Source | Launch Target | Review Cadence | Decision Rule |
|---|---|---|---|---|

## Review Cadence

TODO
"""
        },
        "prototype": {
            "prototype/index.html": "<!doctype html>\n<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Prototype Demo</title><link rel=\"stylesheet\" href=\"./styles.css\"></head><body><div id=\"app\" data-pm-id=\"app.root\"></div><script src=\"./app.js\"></script></body></html>\n",
            "prototype/styles.css": "body{margin:0;font-family:\"Avenir Next\",\"PingFang SC\",sans-serif;background:#f6f3ed;color:#1f2a24}.app{padding:24px}.card{background:#fffaf1;border:1px solid #ddd3c2;border-radius:16px;padding:20px}\n",
            "prototype/app.js": "document.querySelector('#app').innerHTML='<main class=\"app\" data-pm-id=\"prototype.main\"><section class=\"card\" data-pm-id=\"prototype.card\"><h1>Prototype Demo</h1><p>请基于 PRD、sample-data 和 product-spec 扩展产品演示。</p></section></main>';\n",
            "prototype/data/sample-data.json": json.dumps({"records": []}, ensure_ascii=False, indent=2) + "\n",
            "prototype/data/copy.zh-CN.json": json.dumps({"title": name}, ensure_ascii=False, indent=2) + "\n",
            "prototype/spec/product-spec.json": json.dumps({"capabilities": [], "pages": [], "entities": [], "statuses": [], "actions": [], "permissions": []}, ensure_ascii=False, indent=2) + "\n",
        },
        "acceptance": {
            "acceptance.md": f"# {name} Acceptance\n\n## 验收标准\n\n## Capability 覆盖\n\n## UAT 场景\n\n## 上线门禁\n\n## 证据要求\n"
        },
        "review": {
            "review.md": f"# {name} Review\n\n## P0\n\n## P1\n\n## P2\n\n## P3\n"
        },
        "source-map": {
            "source-map.md": f"# {name} 来源映射\n\n"
        },
    }


SHARED_TEMPLATES = {
    "decision-log.md": "# {name} Decision Log\n\n",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a ProductForge feature pack.")
    parser.add_argument("name", help="Feature name.")
    parser.add_argument("--slug", help="Feature slug. Defaults to generated slug.")
    parser.add_argument("--root", default=".", help="Project root.")
    parser.add_argument(
        "--stage",
        choices=STAGE_ORDER + ["all"],
        default="intake",
        help="Feature stage to scaffold. Defaults to intake.",
    )
    parser.add_argument(
        "--mode",
        choices=["minimal", "standard"],
        default="minimal",
        help="Scaffold depth. Defaults to minimal.",
    )
    parser.add_argument(
        "--include-shared",
        action="store_true",
        help="Also create shared files such as decision-log.md.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = args.slug or slugify(args.name)
    feature = root / ".product" / "features" / slug
    templates = feature_templates(args.name)

    stages = STAGE_ORDER if args.stage == "all" else [args.stage]
    include_shared = args.include_shared or args.mode == "standard" or args.stage == "all"

    created: list[str] = []

    for stage in stages:
        for rel, content in templates[stage].items():
            path = feature / rel
            if not path.exists():
                write_if_missing(path, content)
                created.append(str(path))

    if include_shared:
        for rel, template in SHARED_TEMPLATES.items():
            path = feature / rel
            if not path.exists():
                write_if_missing(path, template.format(name=args.name))
                created.append(str(path))
        (feature / "versions").mkdir(parents=True, exist_ok=True)

    print(feature)
    if created:
        print("Created:")
        for item in created:
            print("-", item)
    else:
        print("No files created; existing files were preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
