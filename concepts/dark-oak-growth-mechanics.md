---
type: concept
title: Dark Oak Growth Mechanics
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: Code-level growth mechanics for 2×2 dark oak, compiled from Scorpio (天蝎君)'s Bilibili post (edited 2025-02-09, ~Java 1.21.x), which draws on Sine_Chen's dark oak…
edition: java
version: 1.21
confidence: high
contested: False
tags: [trees, dark-oak, source-bilibili, version-sensitive]
resource: "https://www.bilibili.com/opus/1031059770508836903"
sources: [raw/articles/bilibili-dark-oak-growth.md, raw/articles/gtmc-tree-farm-multi-species.md]
---

# Dark Oak Growth Mechanics

Code-level growth mechanics for 2×2 dark oak, compiled from Scorpio (天蝎君)'s Bilibili post (edited 2025-02-09, ~Java 1.21.x), which draws on Sine_Chen's dark oak work and code review by 1uu1, Wormbo, Dreaming_Galaxy, 幽帘幽梦.^[raw/articles/bilibili-dark-oak-growth.md]

> **Version note:** this page describes Java ~1.21.x; the wiki's GTMC baseline is 1.20.1. One behavior changed in 1.21.4 (leaf centering on bent trunks, MC-237375) — treat that detail as version-sensitive.^[raw/articles/bilibili-dark-oak-growth.md]

## Growth (detection) requirement

- Four saplings in a **2×2** on a plane — never grows from a single sapling.
- Centered on the **northwest-corner sapling**. Above it (not counting the sapling layer) needs a clear column **3×7×3 (min) to 3×10×3 (max)**, and below the final height at least **5×3×5** (X×Y×Z).^[raw/articles/bilibili-dark-oak-growth.md]
- Allowed blocks inside that volume: air, water, leaves, logs, stripped logs, fungus stems, stripped stems, wood, stripped wood, mycelium, stripped mycelium.
- Because of the above, dark oak can be **height-limited or height-boosted**.^[raw/articles/bilibili-dark-oak-growth.md]
- Minecraft Wiki corroborates the 2×2 NW-corner rule and the 3×3 column ≥7 above the NW sapling + 5×5 top-3-layers requirement.^[minecraft.wiki Dark_Oak / Sapling]

## Trunk (log) mechanics

- Trunk is **2×2**, no extra corner log (unlike giant spruce).
- Height **6 to 9** blocks. (Minecraft Wiki describes dark oak as "typically 6–8" — the code range is 6–9.)^[raw/articles/bilibili-dark-oak-growth.md]
- Trunk may **bend** toward E/S/W/N only.
- Bend starts 1–3 layers below the trunk top; the whole trunk shifts 1 or 2 blocks (for a 9-tall trunk, bend may start at layer 9/8/7).
- A **2-block bend** = shift 1 block, then 1 more on the next layer, same direction.
- If the 2×2 trunk's **NW corner already has a log**, that layer's other logs don't grow — but side branches are unaffected. Same rule applies on a bent layer's NW corner.^[raw/articles/bilibili-dark-oak-growth.md]

## Side branches

- Grow in the **12 blocks** around the 2×2 root ring; each column has a **1/3 chance** → 0–12 branches randomly.
- Branch range does **not** move with trunk bend.
- Branch length random **2–4**, growing downward from one layer below the trunk top (e.g. a 7-tall tree: branches from layer 6 down to layer 3).
- Lower bound = one above root; upper bound = one below final trunk top.^[raw/articles/bilibili-dark-oak-growth.md]

## Leaves

- **Trunk leaves:** 3–4 layers, from one below trunk top upward, centered on the trunk top (or bent trunk). Layers bottom→top: **6×6, 8×8, 6×6, 2×2** (the 2×2 has a 1/2 chance to not generate). Corners are often missing.
- **Side-branch leaves:** 3–4 layers, 3×3 then 5×5, centered on the branch top (same start layer as trunk leaves since the branch is one below the trunk top).
- If the trunk bends, the leaf center shifts the same direction by the same amount — **fixed in 1.21.4** (MC-237375): newer versions ignore the bend for centering.^[raw/articles/bilibili-dark-oak-growth.md]

## Farming implications

- Dark oak's 2×2 trunk + irregular branches make it a special case in multi-species farms (GTMC notes it can't be handled by some "center consolidation" methods and retains 1.14-style growth detection in 1.20.1).^[raw/articles/gtmc-tree-farm-multi-species.md]
- Sapling economy is tight: Minecraft Wiki notes only ~1 in 5 dark oak trees yield saplings plentifully; Fortune on leaves helps sustainability. The leaf sapling drop is still the standard 1/20 per leaf.^[minecraft.wiki Tutorial:Tree_farming]

## Related

- [tree-species-requirements](concepts/tree-species-requirements.md) — dark oak in the species table
- [multi-species-tree-farm](concepts/multi-species-tree-farm.md) — why dark oak is a special case
- [leaf-processing](concepts/leaf-processing.md) — 1/20 sapling drop
