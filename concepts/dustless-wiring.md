---
title: Dustless Wiring
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [techniques, dustless, high-speed, source-gtmc]
sources: [raw/articles/gltmc-tree-farm-dustless-wiring.md]
---

# Dustless Wiring

> **Goal:** reduce lag — not to be dustless for its own sake. Forcing dustless designs can *increase* lag, defeating the purpose.^[raw/articles/gltmc-tree-farm-dustless-wiring.md]

## Signal-transmission methods

- **Rails + Observers:** rails emit PP updates on state change, caught by observers; a vertical observer column activates a whole piston row at once. BUD rails give zero-delay transmission.^[raw/articles/gltmc-tree-farm-dustless-wiring.md]
- **Tree / Scaffolding / Wall power:** wireless PP (±NC) updates. Tree power = leaves distance-to-log; scaffolding power = +1gt/scaffold; wall power = instant walls emitting PP on state change.^[raw/articles/gltmc-tree-farm-dustless-wiring.md]
- **Slime sticks:** slime blocks delete pushed blocks in BE phase, changing another piston's state same gt (falling edge no macro delay; rising edge 3gt/piston — needs 3gt auto-reset).^[raw/articles/gltmc-tree-farm-dustless-wiring.md]
- **Rails + BUD:** keep signal in BE phase.^[raw/articles/gltmc-tree-farm-dustless-wiring.md]
- **Redstone redirection:** the *only* dustless method giving a **zero-delay rising edge**; redirection produces PP only, so NC must be supplied separately.^[raw/articles/gltmc-tree-farm-dustless-wiring.md]

## Related

- [[updates-nc-pp]] — NC vs PP basis
- [[0-tick]] — redirection-based 0t generators
- [[4gt-tree-farm]] — modular dustless 0t generators
