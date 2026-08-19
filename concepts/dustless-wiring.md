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
resource: "https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring"
sources:
- id: gtmc-tree-farm-dustless-wiring
  resource: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
  title: GTMC Tree Farm Dustless Wiring
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Dustless Wiring

> **Goal:** reduce lag — not to be dustless for its own sake. Forcing dustless designs can *increase* lag, defeating the purpose.[^gtmc-tree-farm-dustless-wiring]

## Signal-transmission methods

- **Rails + Observers:** rails emit PP updates on state change, caught by observers; a vertical observer column activates a whole piston row at once. BUD rails give zero-delay transmission.[^gtmc-tree-farm-dustless-wiring]
- **Tree / Scaffolding / Wall power:** wireless PP (±NC) updates. Tree power = leaves distance-to-log; scaffolding power = +1gt/scaffold; wall power = instant walls emitting PP on state change.[^gtmc-tree-farm-dustless-wiring]
- **Slime sticks:** slime blocks delete pushed blocks in BE phase, changing another piston's state same gt (falling edge no macro delay; rising edge 3gt/piston — needs 3gt auto-reset).[^gtmc-tree-farm-dustless-wiring]
- **Rails + BUD:** keep signal in BE phase.[^gtmc-tree-farm-dustless-wiring]
- **Redstone redirection:** the *only* dustless method giving a **zero-delay rising edge**; redirection produces PP only, so NC must be supplied separately.[^gtmc-tree-farm-dustless-wiring]

## Related

- [updates-nc-pp](/concepts/updates-nc-pp.md) — NC vs PP basis
- [0-tick](/concepts/0-tick.md) — redirection-based 0t generators
- [4gt-tree-farm](/concepts/4gt-tree-farm.md) — modular dustless 0t generators
- [glossary](/concepts/glossary.md) — DL, 0t, HS, NC/PP term definitions
- [rails](/concepts/rails.md) — rail NC-update order + directional connectivity (the instant component behind dustless wiring)
[^gtmc-tree-farm-dustless-wiring]: https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring
