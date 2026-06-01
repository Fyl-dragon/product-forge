# Domain Packages

`product-gsd` is the generic PM workflow framework. Domain packages add industry knowledge.

## Built-In Recommendation

Use `pm-llm-platform` for LLM aggregation platform work:

- model catalog and routing
- resource pools and source channels
- cloud vendors and account structures
- pricing matrix and gross margin
- suppliers, distributors, channels, CRM/RPM, settlement
- B-end operational consoles

## Routing Rule

When a user asks about LLM platform PRDs, model access, pricing, source routing, resource pools, supplier switching, channel quotation, or customer discount policies:

1. Start with the relevant `pgd-*` workflow.
2. Load `pm-llm-platform` as the domain package.
3. Keep the final PM artifact under `.product/features/<feature-slug>/`.

