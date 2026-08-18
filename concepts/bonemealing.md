---
title: Bonemealing
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [methods, bonemealing, source-gtmc]
sources: [raw/articles/gltmc-tree-farm-basics.md, raw/articles/gltmc-tree-farm-high-speed.md, raw/articles/gltmc-tree-farm-4gt.md]
---

# Bonemealing

Dispensers fire bone meal onto saplings. A dispenser holds little, so bone meal is fed in through hoppers or droppers, with an **unloader** moving it from shulker boxes into the chain.^[raw/articles/gltmc-tree-farm-basics.md]

## High-speed: stacking dispensers

In high-speed farms, bonemealing means **stacking dispensers** — don't worry about consumption. More dispensers widen the *growth window* after a sapling can grow. This introduces **cross bonemealing**: staggering when dispensers fire, generally by 2gt.^[raw/articles/gltmc-tree-farm-high-speed.md]

## 4gt clock: synchronized bonemealing

Because a clock-based 4gt farm has only one growth window every 4gt, it uses **synchronized bonemealing** (not cross), typically a "three-shot + side suction" base.^[raw/articles/gltmc-tree-farm-4gt.md]

## Related

- [[high-speed-tree-farms]] — base design and cross bonemealing
- [[4gt-tree-farm]] — synchronized bonemealing on a 4gt clock
- [[sapling-recycling]] — the other half of the base
