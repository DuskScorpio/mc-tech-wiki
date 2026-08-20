---
type: concept
title: Large Spruce Tree Farm
created: 2026-08-18
updated: 2026-08-18

description: The most log-efficient wood farm (2x2 large spruce).[^gtmc-tree-farm-large-spruce]
edition: java
version: 1.20.1
confidence: high
tags: [farms, large-spruce, tree-farm, source-gtmc, version-sensitive]
sources:
- id: gtmc-tree-farm-large-spruce
  resource: https://www.techmc.wiki/en/articles/tree-farm/large-spruce-farm
  title: GTMC Tree Farm Large Spruce
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Large Spruce Tree Farm

The most log-efficient wood farm (2x2 large spruce).[^gtmc-tree-farm-large-spruce]

## Growth mechanics

- Detection range: **3x3 at the sapling layer (NW corner sapling), expanding to 5x5 above**.
- Max height 28 (29 at the NW corner). Full-height handling is assumed.[^gtmc-tree-farm-large-spruce]

## Architecture

Double recursion for the trunk, honey-slime walls for leaves. Vertical signal via stick BUD; trunk/side-wall activation via redirection dust or wall power. After pushing from the core, split left/right then reassemble. A naive build lands ~100k efficiency.[^gtmc-tree-farm-large-spruce]

## Speed history

- **2016** Laoxian 12gt (upward push), first past 300k.
- **2020-02-12** gpw sprucemacy v1: observer root detection + **corner down-suction**.
- **2021-04-15** gpw sprucemacy v2: **corner side-suction**.
- **2022-02-08** floppy 12gt Spruce v2: 3gt bonemealed planting.
- **2024-08** Qontrol: viable corner side-suction base, 6gt reset.
- **ITT/IF 6gt** large spruce: 1.12 god-tech.[^gtmc-tree-farm-large-spruce]

## Planting timing caveat

- Corner **down-suction** (auto-clicker) and **pig boats** are current viable planting methods.
- **Llama boats broke in 1.21**; single boats desync client/server.[^gtmc-tree-farm-large-spruce]

## Related

- [trunk-processing](/concepts/trunk-processing.md) · [sapling-recycling](/concepts/sapling-recycling.md) · [tree-species-requirements](/concepts/tree-species-requirements.md)
- [high-speed-tree-farms](/concepts/high-speed-tree-farms.md) — base/suction concepts that carry over

[^gtmc-tree-farm-large-spruce]: [gtmc-tree-farm-large-spruce.md](raw/articles/gtmc-tree-farm-large-spruce.md)