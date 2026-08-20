---
type: concept
title: MC Timing Model (intra-tick phases)
created: 2026-08-18
updated: 2026-08-18

description: "Minecraft timing has two scales: **inter-tick timing** (whole gt units) and **intra-tick timing** (the finer ordering *within* one gt)."
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, timing, micro-timing, source-gtmc, source-tmwiki]
sources:
- id: gtmc-intra-tick-timing
  resource: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
  title: GTMC Intra Tick Timing
- id: gtmc-scheduled-ticks
  resource: https://www.techmc.wiki/en/articles/micro-timing/scheduled-ticks
  title: GTMC Scheduled Ticks
- id: gtmc-block-events
  resource: https://www.techmc.wiki/en/articles/micro-timing/block-events
  title: GTMC Block Events
- id: gtmc-block-entities
  resource: https://www.techmc.wiki/en/articles/micro-timing/block-entities
  title: GTMC Block Entities
- id: tmwiki-game-tick
  resource: https://github.com/TechMCDocs/pages/blob/master/GameTick.md
  title: TechMCDocs/pages (Technical Minecraft Wiki)
- id: tmwiki-tile-ticks
  resource: https://github.com/TechMCDocs/pages/blob/master/GameTick/TileTicks.md
  title: TechMCDocs/pages (Technical Minecraft Wiki)
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# MC Timing Model (intra-tick phases)

Minecraft timing has two scales: **inter-tick timing** (whole gt units) and **intra-tick timing** (the finer ordering *within* one gt). MC is single-threaded, so even "same gt" events always execute in a fixed priority order.[^gtmc-intra-tick-timing]

## The authoritative intra-tick phase order (within 1gt)
1. **WTU** — World Tick Update: the world "timer" increments by 1.
2. **TT** — Scheduled/Tile Tick (Next Tick Entry): delayed components execute here.
3. **CT** — Chunk Tick: lightning, snow, Random Tick (crop growth, grass spread, water freeze) near the player.
4. **BE** — Block Event: piston push/pull, note-block sound. A piston adds its block event when its actual state ≠ powered state.
5. **EU** — Entity Update: entity movement/AI, TNT, non-player plate/tripwire activation.
6. **TE** — Block Entity: hoppers absorb/transfer; b36 pushes entities (first two TE) and reverts on the third.
7. **AT/NU** — Async Task / Network Update (Player Action): player-action packets executed at the *end* of the tick.

> **Correction note:** an earlier simplified GTMC page listed this order loosely ("NU→TT→BE→TE"). The full GTMC intra-tick chapter gives the precise order above (WTU→TT→CT→BE→EU→TE→AT), and TMWiki's `GameTick.md` independently lists a compatible order (tile ticks → ChunkManager → BlockEvent → entities → block entities → player inputs). The order above is now treated as authoritative.[^gtmc-intra-tick-timing] [^tmwiki-game-tick]

## Depth (BE ordering) — what 0-tick exploits
Pistons (BE components) execute when their actual state ≠ powered state. Block Events process **FIFO with depth**: the initial event is depth 0; events it directly causes are depth 1, and so on — a breadth-first search over the "piston graph." This is **Block Event Delay (BED)**. A 0-tick pulse acts within BE depth before a later event can interrupt it. Note blocks do **not** increase depth.[^gtmc-block-events]

The canonical tree-farm example is a **0t bottom-retraction base**: 0gt AT lever → 1gt BE depth0 sticky piston retracts → depth1 pulls podzol + dust redirects → depth2 bottom-retraction piston self-checks & extends → depth3 powered block removed, bottom piston queues retract but is still extending → **0t**. 3gt TE everything placed.[^gtmc-block-events]

## Scheduled ticks (TT detail)
A Scheduled Tick carries only `triggerTick, subTickOrder, priority, pos, type` — no action; the block decides on execution. Execution order: **triggerTick (macro) > priority (lower = earlier) > subTickOrder (add order)**. Repeater = `delay×2gt`; comparator = `2gt`; observer/torch = `2gt` (priority 0). Observers check `isQueued` (not current-gt), which is the basis of **4gt Observer high-frequency** used in 4gt tree farms.[^gtmc-scheduled-ticks]

## Component phase table (key rows)[^gtmc-intra-tick-timing]
| Component | Phase |
|---|---|
| Repeater / Comparator / Observer / Redstone Torch on-off | TT |
| Redstone Dust, Rails state change | Instant (any phase, on block update) |
| Fence Gates, Trapdoors, Dispenser/Dropper state, Hopper state, Lamp on, Buttons/Plates/Tripwire on | Instant |
| Hopper absorb/transfer items | TE |
| Note/Bell sound | BE |
| Dispenser dispense / Dropper drop | TT |
| Lamp off, Button/Plate/Tripwire off | TT |
| Piston extend/retract | BE |
| b36 push entity / natural land | TE |
| b36 retracted + landed by sticky piston | BE |
| Falling block decide | TT; fall/land | EU |

> **Confidence note:** upgraded from `medium` to `high` after reading GTMC's full intra-tick, scheduled-tick, block-event, and block-entity theory chapters (which supersede the simplified "basics" page). Phase order and component phases are now sourced to those chapters. Still Java 1.20.1; treat exact phase *names* as conventional but the ordering is well-established.

## Related
- [piston-action-timing](/concepts/piston-action-timing.md) — how depth produces 0-tick
- [update-theory](/concepts/update-theory.md) — NC/PP/Comparator/Self-inspection, QC, flags
- [continuous-updates](/concepts/continuous-updates.md) — DFS propagation order (note: NC propagation, distinct from BE BFS)
- [special-update-behaviors](/concepts/special-update-behaviors.md) — dust 2nd-order, diagonal rails, lit-observer quirk
- [tick-micro-timing](/concepts/tick-micro-timing.md) — game tick, inter/intra-tick, tile-tick table
- [piston-mechanics](/concepts/piston-mechanics.md) — self-check, QC, push limit, b36, instant placement
- [moving-block-b36](/concepts/moving-block-b36.md) — B36 properties & NBT
- [0-tick](/concepts/0-tick.md) — using depth for speed
- [block-nature](/concepts/block-nature.md) — Block vs BlockState (pointer)

[^gtmc-intra-tick-timing]: https://www.techmc.wiki/en/articles/micro-timing/intra-tick-timing
[^tmwiki-game-tick]: https://github.com/TechMCDocs/pages/blob/master/GameTick.md
[^gtmc-block-events]: https://www.techmc.wiki/en/articles/micro-timing/block-events
[^gtmc-scheduled-ticks]: https://www.techmc.wiki/en/articles/micro-timing/scheduled-ticks
