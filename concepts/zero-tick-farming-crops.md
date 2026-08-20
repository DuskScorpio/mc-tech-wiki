---
type: concept
title: Zero-Tick Farming (crops) — distinction from 0-tick redstone
created: 2026-08-18
updated: 2026-08-18

description: "**Zero-tick farming** (as the term is used on the Technical Minecraft Wiki) is a *crop*-growth exploit: replace the block a self-stacking crop rests on, which s…"
edition: java
version: <=1.15 (patched 20w12a)
confidence: high
contested: False
tags: [bugs, zero-tick, crops, source-tmwiki, version-sensitive, patched]
sources:
- id: tmwiki-zero-tick-farms
  resource: https://github.com/TechMCDocs/pages/blob/master/BugsAndExploits/ZeroTickFarms.md
  title: TechMCDocs/pages (Technical Minecraft Wiki)
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Zero-Tick Farming (crops) — distinction from 0-tick redstone

**Zero-tick farming** (as the term is used on the Technical Minecraft Wiki) is a *crop*-growth exploit: replace the block a self-stacking crop rests on, which schedules a tile tick; if the block is replaced before the 1gt-later check, the crop executes the growth tile tick early. **Patched in 20w12a / 1.16+ — does not work in modern versions.**[^tmwiki-zero-tick-farms]

> ⚠️ **Do not conflate with the tree-farm "0-tick" generators.** In our tree-farm pages, [0-tick](/concepts/0-tick.md) refers to **0-tick redstone generators** (repeater/redstone-dust/redirection) that exploit intra-tick piston/redstone *depth* — these still work in 1.20+. The crop version is a different, patched mechanic. Same name, different thing.

## Related
- [0-tick](/concepts/0-tick.md) — the working redstone-generator technique used in tree farms
- [tick-micro-timing](/concepts/tick-micro-timing.md) — tile tick phase, where the 1gt-later check lives

[^tmwiki-zero-tick-farms]: https://github.com/TechMCDocs/pages/blob/master/BugsAndExploits/ZeroTickFarms.md
