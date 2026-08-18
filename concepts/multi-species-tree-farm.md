---
title: Multi-Species Tree Farm
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [farms, multi-species, tree-farm, source-gtmc]
sources: [raw/articles/gltmc-tree-farm-multi-species.md]
---

# Multi-Species Tree Farm

A farm handling birch, oak, jungle, spruce, and acacia together. Design takes the union of species requirements (see [[tree-species-requirements]]).^[raw/articles/gltmc-tree-farm-multi-species.md]

## Example architecture (PTHSUTF-like)

- **Honey-slime triple recursion** on the main pusher
- **Center consolidation** for side branches
- **Honey-slime walls** for leaf processing
- Manually placed **obsidian** for oak height limiting^[raw/articles/gltmc-tree-farm-multi-species.md]

## Block stream → drops

Multi-species output is irregular, so it must be **reorganized** before the explosion chamber: two piston rows merge the two log outputs into a 2-wide stream, or a side-suction base converts them to a fixed ~6gt interval. Avoid 2-block-thick streams (lowers drop recovery). Use **milk explosions** or **b36 push explosions** for high-volume irregular streams.^[raw/articles/gltmc-tree-farm-multi-species.md]

## Wiring concerns

- **Acacia timing switching:** add delay to the two side walls vs normal timing.
- **Automatic oak height limiting:** place an unpushable block via flying machine.
- **Speed limiter:** prevent premature re-trigger before reset (see [[detection-methods]]).^[raw/articles/gltmc-tree-farm-multi-species.md]

## Related

- [[tree-species-requirements]] · [[trunk-processing]] · [[block-to-drop]]
- [[4gt-tree-farm]] — the clock-driven evolution of this design
