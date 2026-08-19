---
type: concept
title: Trunk Processing
created: 2026-08-18
updated: 2026-08-18

description: Moving the grown trunk away from where it grew.
edition: java
version: 1.20.1
confidence: high
tags: [methods, trunk-processing, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
  title: GTMC Tree Farm Multi Species
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Trunk Processing

Moving the grown trunk away from where it grew. Two layers: the **main trunk** and the **root**.[^gtmc-tree-farm-basics]

## Main trunk

- **Triple push extension**
- **Pseudo double push extension**
- **Honey-slime wall double push extension** — the most widely used design today.[^gtmc-tree-farm-basics]

For birch/oak a simple push/pull works. For side-branch trees (acacia, cherry, azalea) you also need **side branch processing** — either center consolidation or additional log outputs.[^gtmc-tree-farm-multi-species]

## Root processing (four approaches)

1. Process alongside the main trunk
2. **Upward push** — slowest (earliest plant 6gt); now largely abandoned
3. **Downward pull** — ~3gt
4. **Side pull** — as fast as 0gt

Dark oak sometimes uses an **upward pull** variant.[^gtmc-tree-farm-basics] See [high-speed-tree-farms](/concepts/high-speed-tree-farms.md) for why upward push is abandoned in high-speed designs.

## Related

- [tree-species-requirements](/concepts/tree-species-requirements.md) — which method fits each species
- [multi-species-tree-farm](/concepts/multi-species-tree-farm.md) — combining methods
- [high-speed-tree-farms](/concepts/high-speed-tree-farms.md) — base design with downward/side suction
[^gtmc-tree-farm-basics]: https://www.techmc.wiki/en/articles/block-update
[^gtmc-tree-farm-multi-species]: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
