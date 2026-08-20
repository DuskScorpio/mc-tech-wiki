---
type: concept
title: Slime Tech Engines and Mobility
created: 2026-08-18
updated: 2026-08-18

description: GTMC Slime Tech engine definition (anything with agency) and mobility — turning a functional structure directly mobile by reusing its pistons/observers/slime.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, slime-tech, engine, mobility, source-gtmc]
sources:
- id: gtmc-engines
  resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/engines
  title: GTMC Engines
- id: gtmc-mobility
  resource: https://www.techmc.wiki/en/articles/slime-tech/twisuki/mobility
  title: GTMC Mobility
generated: { by: /, at: 2026-08-18T00:00:00Z }
status: stable
---

# Slime Tech Engines and Mobility

## Engine (definition)
Anything with **agency** is an engine — a small core or an entire assembly. Whether it has agency (not its size) determines if it's an engine. The progression: mount functional structures onto engines -> make functional structures themselves into engines.[^gtmc-engines]

## Mobility — making a structure fly directly
Instead of mounting onto an engine, extend "mobility" into a functional structure so it moves on its own. From a 10gt flying machine, the minimal mobility structure is:[^gtmc-mobility]
- Two opposing pistons, at least one sticky.
- Two Observers, each activating one piston.
- Slime blocks for connection.

To mobilize a functional structure: fill in those three components. **Prioritize reusing the structure's existing slime blocks and observers** (avoid adding new ones). Place pistons avoiding the 12-block push limit and ensuring all parts connect. The engine need not be 10gt — the two-pistons + observers + slime principle is what matters.[^gtmc-mobility]

> Conceptual/practice-oriented chapters (single GTMC source). The mechanical core — periods, observers, push limits — is covered in [Flying Machines](/concepts/flying-machines.md) and [Piston Mechanics](/concepts/piston-mechanics.md).

## Related
- [Flying Machines](/concepts/flying-machines.md) — the 10gt engine these build on
- [Linkages](/concepts/linkages.md) — zero-delay piston-chain motion transfer
- [Piston Mechanics](/concepts/piston-mechanics.md) — 12-block push limit, sticky-piston timing
- [Glossary](/concepts/glossary.md) — slime/honey, observer, BUD definitions

[^gtmc-engines]: [gtmc-engines.md](raw/articles/gtmc-engines.md)
[^gtmc-mobility]: [gtmc-mobility.md](raw/articles/gtmc-mobility.md)