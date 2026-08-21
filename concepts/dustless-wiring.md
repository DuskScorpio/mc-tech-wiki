---
type: concept
title: Dustless Wiring
created: 2026-08-18
updated: 2026-08-18

description: "> **Goal:** reduce lag — not to be dustless for its own sake."
edition: java
version: 1.20.1
confidence: high
tags: [techniques, dustless, high-speed, source-gtmc]
sources:
- id: gtmc-tree-farm-dustless-wiring
  resource: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
  title: GTMC Tree Farm Dustless Wiring
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Dustless Wiring

> **Goal:** reduce lag — not to be dustless for its own sake. Forcing dustless designs can *increase* lag, defeating the purpose.[^gtmc-tree-farm-dustless-wiring]

The methods below split into two groups by **whether they introduce macro delay**. Delay comes from components that *schedule a TT tick* to recompute their state (Tree/Scaffolding/Wall power); methods that keep the signal propagating inside the **BE phase** avoid that tick and thus have no macro delay.

## Delay-bearing methods (schedule a TT tick)

These change state via an update that runs in Tile Tick (1gt later, or immediately if already in TT), so they add macro delay:

- **Tree / Scaffolding / Wall power:** wireless PP (±NC) updates. Tree power = leaves schedule a TT tick to recompute distance-to-log; scaffolding power adds **1gt delay per scaffold** (distance check scheduled in TT); wall power is an **instant component** (state change emits PP immediately, caught by observers).[^gtmc-tree-farm-dustless-wiring]

## No macro delay (signal stays in the BE phase)

These keep the change inside the Block-Event phase, so no TT tick is scheduled:

- **Slime sticks:** slime blocks delete pushed blocks in the BE phase, changing another piston's state in the same gt. **Falling-edge** transmission has no macro delay; **rising edges** have **3gt delay per piston** — each stick gets a 3gt auto-reset.[^gtmc-tree-farm-dustless-wiring]
- **Rails + BUD:** rails are instant components; updating a BUD via rails and having the BUD re-power a rail chain keeps the signal propagating within the BE phase (zero-delay transmission).[^gtmc-tree-farm-dustless-wiring]

## Zero-delay rising edge (unique case)

- **Redstone redirection:** the **only** dustless method that outputs a **zero-delay rising edge**. Redirection produces **PP only**, so NC must be supplied separately.[^gtmc-tree-farm-dustless-wiring] Variants: vertical columns, the standard **3gt generator** (3gt push / 3gt pull piston action), and the **0t generator** (redirection-based).

## Related

- [updates-nc-pp](/concepts/updates-nc-pp.md) — NC vs PP basis
- [0-tick](/concepts/0-tick.md) — redirection-based 0t generators
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — modular dustless 0t generators
- [glossary](/concepts/glossary.md) — DL, 0t, HS, NC/PP term definitions
- [rails](/concepts/rails.md) — rail NC-update order + directional connectivity (the instant component behind dustless wiring)

[^gtmc-tree-farm-dustless-wiring]: [gtmc-tree-farm-dustless-wiring.md](raw/articles/gtmc-tree-farm-dustless-wiring.md)