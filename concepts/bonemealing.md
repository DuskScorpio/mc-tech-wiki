---
type: concept
title: Bonemealing
created: 2026-08-18
updated: 2026-08-18

description: Dispensers fire bone meal onto saplings.
edition: java
version: 1.20.1
confidence: high
tags: [methods, bonemealing, source-gtmc]
sources:
- id: gtmc-tree-farm-basics
  resource: https://www.techmc.wiki/en/articles/block-update
  title: GTMC Tree Farm Basics
- id: gtmc-tree-farm-high-speed
  resource: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
  title: GTMC Tree Farm High Speed
- id: gtmc-tree-farm-4gt
  resource: https://www.techmc.wiki/en/articles/tree-farm/4gt-farms
  title: GTMC Tree Farm 4gt
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Bonemealing

Dispensers fire bone meal onto saplings. A dispenser holds little, so bone meal is fed in through hoppers or droppers, with an **unloader** moving it from shulker boxes into the chain.[^gtmc-tree-farm-basics]

## High-speed: stacking dispensers

In high-speed farms, bonemealing means **stacking dispensers** — don't worry about consumption. More dispensers widen the *growth window* after a sapling can grow. This introduces **cross bonemealing**: staggering when dispensers fire, generally by 2gt.[^gtmc-tree-farm-high-speed]

## 4gt clock: synchronized bonemealing

Because a clock-based 4gt farm has only one growth window every 4gt, it uses **synchronized bonemealing** (not cross), typically a "three-shot + side suction" base.[^gtmc-tree-farm-4gt]

## Related

- [high-speed-tree-farms](/concepts/high-speed-tree-farms.md) — base design and cross bonemealing
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — synchronized bonemealing on a 4gt clock
- [sapling-recycling](/concepts/sapling-recycling.md) — the other half of the base

[^gtmc-tree-farm-basics]: https://www.techmc.wiki/en/articles/block-update
[^gtmc-tree-farm-high-speed]: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
[^gtmc-tree-farm-4gt]: https://www.techmc.wiki/en/articles/tree-farm/4gt-farms
