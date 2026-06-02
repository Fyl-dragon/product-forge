---
name: pf-accept
description: Generate ProductForge acceptance criteria, UAT scenarios, product demo verification steps, rollout gates, and evidence requirements for feature packs.
---

# PF Accept

Define how product work is proven complete.

## Workflow

1. Read `SPEC.md`, PRD, metrics, prototype demo, product spec, review findings, and release plan.
2. Create `.product/features/<feature-slug>/acceptance.md`.
3. Include:
   - 功能验收标准
   - capability ID 覆盖
   - 角色/权限验收
   - 状态流转验收
   - 异常场景
   - 业务规则与数据一致性
   - 数据展示验收
   - 原型 Demo 验收
   - 灰度与上线门槛
   - 指标基线、目标与观察周期
   - 验收证据
4. Every scenario should name the observable evidence needed to pass.
