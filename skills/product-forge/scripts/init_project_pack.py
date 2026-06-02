#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATES = {
    "project-plan.md": """# {name} 项目计划

## 项目目标

TODO

## 范围

### 范围内

TODO

### 范围外

TODO

## 里程碑

| 里程碑 | 产品结果 | 负责人 | 成功信号 | 截止时间 | 状态 |
|---|---|---|---|---|---|

## 关键依赖

TODO

## 产品侧交接摘要

TODO
""",
    "raid-log.md": """# {name} RAID Log

## Escalation Rules

| Severity | Trigger | Required Action | Decision Owner | Update Cadence |
|---|---|---|---|---|
| P0 | Blocks launch, compliance, customer trust, or core acceptance | Escalate immediately and force launch decision | TODO | Daily until resolved |
| P1 | Threatens milestone, scope, or key dependency | Escalate in next stakeholder update | TODO | Twice weekly |
| P2 | Manageable risk with clear owner | Track in RAID | TODO | Weekly |

## Risks

| ID | Severity | 风险 | Trigger | 影响 | 概率 | 应对 | Decision Needed | 负责人 | 状态 |
|---|---|---|---|---|---|---|---|---|---|

## Assumptions

| ID | 假设 | 验证方式 | Evidence Required | Escalate When | Decision Rule | 负责人 | 截止时间 | 状态 |
|---|---|---|---|---|---|---|---|---|

## Issues

| ID | Severity | 问题 | Trigger | 影响 | 处理动作 | Decision Needed | 负责人 | 状态 |
|---|---|---|---|---|---|---|---|---|

## Dependencies

| ID | Severity | 依赖 | 来源 | 影响范围 | Blocker | Escalation Owner | 负责人 | 状态 |
|---|---|---|---|---|---|---|---|---|
""",
    "stakeholder-update.md": """# {name} 干系人更新

## Update Cadence

| Audience | Cadence | Channel | Owner |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

## 本期摘要

TODO

## 进展

TODO

## 关键决策

TODO

## 风险与请求

TODO

## Decision Requests

| Decision Needed | Options | Recommendation | Owner | Deadline |
|---|---|---|---|---|

## 下期计划

TODO
""",
    "decision-log.md": """# {name} Decision Log

| Date | Decision Type | Status | Decision | Rationale | Evidence | Owner | Revisit Condition |
|---|---|---|---|---|---|---|---|
""",
    "launch-readiness.md": """# {name} 上线准备

## Readiness Gate Summary

| Gate | Status (PASS/CONCERN/FAIL) | Evidence | Blocker | Decision Needed | Owner |
|---|---|---|---|---|---|

## 上线门禁

| Gate | 标准 | Required Evidence | Actual Evidence | 负责人 | 状态 |
|---|---|---|---|---|---|

## 灰度策略

TODO

## 回滚条件

TODO

## 上线后观察指标

TODO

## 支持与运营准备

TODO
""",
    "acceptance-tracker.md": """# {name} 验收推进

## Status Rules

Allowed states: Not Started, In Progress, Blocked, Evidence Ready, Accepted, Waived.

## Acceptance Progress

| Capability | 验收场景 | Business Rule / Permission / State Coverage | Evidence Link | Blocker | Owner | Status | 备注 |
|---|---|---|---|---|---|---|---|
""",
}


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
    return slug or "new-project"


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a ProductForge project-management pack.")
    parser.add_argument("name", help="Project name.")
    parser.add_argument("--slug", help="Project slug. Defaults to generated slug.")
    parser.add_argument("--root", default=".", help="Project root.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    slug = args.slug or slugify(args.name)
    project = root / ".product" / "projects" / slug

    for filename, template in TEMPLATES.items():
        write_if_missing(project / filename, template.format(name=args.name))

    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
