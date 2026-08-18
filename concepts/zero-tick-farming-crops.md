---
title: Zero-Tick Farming (crops) — distinction from 0-tick redstone
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: "<=1.15 (patched 20w12a)"
confidence: high
contested: false
tags: [bugs, zero-tick, crops, source-tmwiki, version-sensitive, patched]
sources: [raw/articles/tmwiki-zero-tick-farms.md]
---

# Zero-Tick Farming (crops) — distinction from 0-tick redstone

**Zero-tick farming** (as the term is used on the Technical Minecraft Wiki) is a *crop*-growth exploit: replace the block a self-stacking crop rests on, which schedules a tile tick; if the block is replaced before the 1gt-later check, the crop executes the growth tile tick early. **Patched in 20w12a / 1.16+ — does not work in modern versions.**^[raw/articles/tmwiki-zero-tick-farms.md]

> ⚠️ **Do not conflate with the tree-farm "0-tick" generators.** In our tree-farm pages, [[0-tick]] refers to **0-tick redstone generators** (repeater/redstone-dust/redirection) that exploit intra-tick piston/redstone *depth* — these still work in 1.20+. The crop version is a different, patched mechanic. Same name, different thing.

## Related
- [[0-tick]] — the working redstone-generator technique used in tree farms
- [[tick-micro-timing]] — tile tick phase, where the 1gt-later check lives
