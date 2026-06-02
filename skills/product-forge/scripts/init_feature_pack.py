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
    parser = argparse.ArgumentParser(description="Create a ProductForge feature pack.")
    parser.add_argument("name", help="Feature name.")
    parser.add_argument("--slug", help="Feature slug. Defaults to generated slug.")
    parser.add_argument("--root", default=".", help="Project root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = args.slug or slugify(args.name)
    feature = root / ".product" / "features" / slug

    write_if_missing(feature / "00-intake.md", f"# {args.name} Intake\n\n## 背景\n\n## 目标用户\n\n## 问题定义\n\n## 范围\n\n## 风险\n\n## 待确认问题\n")
    write_if_missing(feature / "discovery.md", f"""# {args.name} Discovery

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
""")
    write_if_missing(feature / "opportunity-solution-tree.md", f"""# {args.name} Opportunity Solution Tree

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
""")
    write_if_missing(feature / "01-research.md", f"# {args.name} Research\n\n## 调研问题\n\n## 对比矩阵\n\n## 产品决策启发\n\n## 对 SPEC 的影响\n")
    write_if_missing(feature / "PRFAQ.md", f"""# {args.name} PRFAQ

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
""")
    write_if_missing(feature / "02-define.md", f"# {args.name} Define\n\n## 功能目标\n\n## 用户与 Jobs\n\n## 实体与字段\n\n## 状态与流转\n\n## 权限\n\n## 业务规则\n\n## 边界与依赖\n")
    write_if_missing(feature / "SPEC.md", f"""# {args.name} SPEC

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
""")
    write_if_missing(feature / "docs" / "prd.md", f"# {args.name} PRD\n\n## 1. 背景与问题\n\n## 2. 目标与非目标\n\n## 3. 用户与场景\n\n## 4. Capability Traceability\n\n## 5. 功能范围\n\n## 6. 业务规则\n\n## 7. 数据对象与字段\n\n## 8. 权限与状态\n\n## 9. 验收标准\n")
    write_if_missing(feature / "metrics.md", f"""# {args.name} Metrics

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
""")
    write_if_missing(feature / "acceptance.md", f"# {args.name} Acceptance\n\n## 验收标准\n\n## Capability 覆盖\n\n## UAT 场景\n\n## 上线门禁\n\n## 证据要求\n")
    write_if_missing(feature / "review.md", f"# {args.name} Review\n\n## P0\n\n## P1\n\n## P2\n\n## P3\n")
    write_if_missing(feature / "decision-log.md", f"# {args.name} Decision Log\n\n")
    write_if_missing(feature / "source-map.md", f"# {args.name} 来源映射\n\n")
    write_if_missing(feature / "prototype" / "index.html", "<!doctype html>\n<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"><title>Prototype Demo</title><link rel=\"stylesheet\" href=\"./styles.css\"></head><body><div id=\"app\" data-pm-id=\"app.root\"></div><script src=\"./app.js\"></script></body></html>\n")
    write_if_missing(feature / "prototype" / "styles.css", "body{margin:0;font-family:\"Avenir Next\",\"PingFang SC\",sans-serif;background:#f6f3ed;color:#1f2a24}.app{padding:24px}.card{background:#fffaf1;border:1px solid #ddd3c2;border-radius:16px;padding:20px}\n")
    write_if_missing(feature / "prototype" / "app.js", "document.querySelector('#app').innerHTML='<main class=\"app\" data-pm-id=\"prototype.main\"><section class=\"card\" data-pm-id=\"prototype.card\"><h1>Prototype Demo</h1><p>请基于 PRD、sample-data 和 product-spec 扩展产品演示。</p></section></main>';\n")
    write_if_missing(feature / "prototype" / "data" / "sample-data.json", json.dumps({"records": []}, ensure_ascii=False, indent=2) + "\n")
    write_if_missing(feature / "prototype" / "data" / "copy.zh-CN.json", json.dumps({"title": args.name}, ensure_ascii=False, indent=2) + "\n")
    write_if_missing(feature / "prototype" / "spec" / "product-spec.json", json.dumps({"capabilities": [], "pages": [], "entities": [], "statuses": [], "actions": [], "permissions": []}, ensure_ascii=False, indent=2) + "\n")
    (feature / "versions").mkdir(parents=True, exist_ok=True)

    print(feature)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
