---
type: concept
title: Dustless Wiring
created: 2026-08-18
updated: 2026-08-18
timestamp: "2026-08-18T00:00:00Z"
description: "> **Goal:** reduce lag — not to be dustless for its own sake."
edition: java
version: 1.20.1
confidence: high
tags: [techniques, dustless, high-speed, source-gtmc]
resource: "https://www.techmc.wiki/en/articles/tree-farm/dustless-wiring"
sources: [raw/articles/gtmc-tree-farm-dustless-wiring.md]
---

# Dustless Wiring

> **Goal:** reduce lag — not to be dustless for its own sake. Forcing dustless designs can *increase* lag, defeating the purpose.^[raw/articles/gtmc-tree-farm-dustless-wiring.md]

## Signal-transmission methods

- **Rails + Observers:** rails emit PP updates on state change, caught by observers; a vertical observer column activates a whole piston row at once. BUD rails give zero-delay transmission.^[raw/articles/gtmc-tree-farm-dustless-wiring.md]
- **Tree / Scaffolding / Wall power:** wireless PP (±NC) updates. Tree power = leaves distance-to-log; scaffolding power = +1gt/scaffold; wall power = instant walls emitting PP on state change.^[raw/articles/gtmc-tree-farm-dustless-wiring.md]
- **Slime sticks:** slime blocks delete pushed blocks in BE phase, changing another piston's state same gt (falling edge no macro delay; rising edge 3gt/piston — needs 3gt auto-reset).^[raw/articles/gtmc-tree-farm-dustless-wiring.md]
- **Rails + BUD:** keep signal in BE phase.^[raw/articles/gtmc-tree-farm-dustless-wiring.md]
- **Redstone redirection:** the *only* dustless method giving a **zero-delay rising edge**; redirection produces PP only, so NC must be supplied separately.^[raw/articles/gtmc-tree-farm-dustless-wiring.md]

## Related

- [updates-nc-pp](concepts/updates-nc-pp.md) — NC vs PP basis
- [0-tick](concepts/0-tick.md) — redirection-based 0t generators
- [4gt-tree-farm](concepts/4gt-tree-farm.md) — modular dustless 0t generators
- [glossary](concepts/glossary.md) — DL, 0t, HS, NC/PP term definitions
- [rails](concepts/rails.md) — rail NC-update order + directional connectivity (the instant component behind dustless wiring)
