---
title: Large Spruce Tree Farm
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [farms, large-spruce, tree-farm, source-gtmc, version-sensitive]
sources: [raw/articles/gltmc-tree-farm-large-spruce.md]
---

# Large Spruce Tree Farm

The most log-efficient wood farm (2x2 large spruce).^[raw/articles/gltmc-tree-farm-large-spruce.md]

## Growth mechanics

- Detection range: **3x3 at the sapling layer (NW corner sapling), expanding to 5x5 above**.
- Max height 28 (29 at the NW corner). Full-height handling is assumed.^[raw/articles/gltmc-tree-farm-large-spruce.md]

## Architecture

Double recursion for the trunk, honey-slime walls for leaves. Vertical signal via stick BUD; trunk/side-wall activation via redirection dust or wall power. After pushing from the core, split left/right then reassemble. A naive build lands ~100k efficiency.^[raw/articles/gltmc-tree-farm-large-spruce.md]

## Speed history

- **2016** Laoxian 12gt (upward push), first past 300k.
- **2020-02-12** gpw sprucemacy v1: observer root detection + **corner down-suction**.
- **2021-04-15** gpw sprucemacy v2: **corner side-suction**.
- **2022-02-08** floppy 12gt Spruce v2: 3gt bonemealed planting.
- **2024-08** Qontrol: viable corner side-suction base, 6gt reset.
- **ITT/IF 6gt** large spruce: 1.12 god-tech.^[raw/articles/gltmc-tree-farm-large-spruce.md]

## Planting timing caveat

- Corner **down-suction** (auto-clicker) and **pig boats** are current viable planting methods.
- **Llama boats broke in 1.21**; single boats desync client/server.^[raw/articles/gltmc-tree-farm-large-spruce.md]

## Related

- [[trunk-processing]] · [[sapling-recycling]] · [[tree-species-requirements]]
- [[high-speed-tree-farms]] — base/suction concepts that carry over
