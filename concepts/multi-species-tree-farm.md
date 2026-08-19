---
type: concept
title: Multi-Species Tree Farm
created: 2026-08-18
updated: 2026-08-18

description: A farm handling birch, oak, jungle, spruce, and acacia together.
edition: java
version: 1.20.1
confidence: high
tags: [farms, multi-species, tree-farm, source-gtmc]
sources:
- id: gtmc-tree-farm-multi-species
  resource: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
  title: GTMC Tree Farm Multi Species
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Multi-Species Tree Farm

A farm handling birch, oak, jungle, spruce, and acacia together. Design takes the union of species requirements (see [tree-species-requirements](/concepts/tree-species-requirements.md)).[^gtmc-tree-farm-multi-species]

## Example architecture (PTHSUTF-like)

- **Honey-slime triple recursion** on the main pusher
- **Center consolidation** for side branches
- **Honey-slime walls** for leaf processing
- Manually placed **obsidian** for oak height limiting[^gtmc-tree-farm-multi-species]

## Block stream → drops

Multi-species output is irregular, so it must be **reorganized** before the explosion chamber: two piston rows merge the two log outputs into a 2-wide stream, or a side-suction base converts them to a fixed ~6gt interval. Avoid 2-block-thick streams (lowers drop recovery). Use **milk explosions** or **b36 push explosions** for high-volume irregular streams.[^gtmc-tree-farm-multi-species]

## Wiring concerns

- **Acacia timing switching:** add delay to the two side walls vs normal timing.
- **Automatic oak height limiting:** place an unpushable block via flying machine.
- **Speed limiter:** prevent premature re-trigger before reset (see [detection-methods](/concepts/detection-methods.md)).[^gtmc-tree-farm-multi-species]

## Related

- [tree-species-requirements](/concepts/tree-species-requirements.md) · [trunk-processing](/concepts/trunk-processing.md) · [block-to-drop](/concepts/block-to-drop.md)
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — the clock-driven evolution of this design
[^gtmc-tree-farm-multi-species]: https://www.techmc.wiki/en/articles/tree-farm/multi-species-design
