---
type: concept
title: Piston Mechanics
created: 2026-08-18
updated: 2026-08-18

description: Piston = base + head; states retracted/extended.
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, source-gtmc]
sources:
- id: gtmc-pistons
  resource: https://www.techmc.wiki/en/articles/redstone-components/pistons
  title: GTMC Pistons
- id: tmwiki-piston
  resource: https://github.com/TechMCDocs/pages/blob/master/Blocks/Pistons.md
  title: TechMCDocs/pages (Technical Minecraft Wiki) — Pistons
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Piston Mechanics

Piston = base + head; states retracted/extended. A **headless piston** (base only) believes its head still exists in front of it.[^gtmc-pistons]

## Self-check & QC
- Self-check triggers: placed by player (onPlaced→tryMove), NC update (neighborUpdate→tryMove), or onBlockAdded when block type changed.
- Self-check is instantaneous and can happen at any stage; "attempt" may fail.
- **shouldExtend** checks the piston's own 6 directions (excluding facing), then the block BELOW, then the block ABOVE's 6 directions. This is the origin of **QC** and why BUDs only detect NC updates.[^gtmc-pistons]

## Push / pull
- A block is movable only if not immovable and the moved list stays ≤ **12** (push limit).
- Structure analysis uses movedBlocks + brokenBlocks lists (alternating linear/branch on a stack). Use Fallen_Breath's **PistOrder** mod to view attempt order in-game.
- b36 arrival/removal order = reverse of the moved/broken lists.[^gtmc-pistons]

## b36 (moving_piston) & placement
- Normal: b36 gains 0.5 progress/tick in the TE phase; from 0gt AT it's fully placed at **3gt AT** → the "3-gt piston delay".[^gtmc-pistons]
- **Instant placement (finish):** triggered when a sticky piston has a b36 one block outside its extension direction with matching movement direction, or when the piston-head position is b36 (instant retract). Progress set to 1.0, original block placed, updates sent — but only the single block in front of the sticky piston. No entity displacement, no waterlogged removal.[^gtmc-pistons]

## Push-limit detection (advanced)
- "Deceiving" the piston: its planned action can differ from the actual push structure at execution time. Core of **push-limit detection** (discovered by _Kayleigh and Landmining; simplified by Bright_Observer) — the detection method used in tree farms. See [detection-methods](/concepts/detection-methods.md).[^gtmc-pistons]

## Piston head (advanced)
- `canSurvive`: head valid iff the block behind (opposite push dir) is an extending piston with same facing, OR a b36 behind with same dir.
- PP update behind → canSurvive check (invalid → disappears). NC update never removes the head.[^gtmc-pistons]

## Related
- [piston-action-timing](/concepts/piston-action-timing.md) — 3gt default action, 1gt/2gt costs, 0-tick basis
- [update-theory](/concepts/update-theory.md) — QC/Bud wiring
- [tick-micro-timing](/concepts/tick-micro-timing.md) — BE phase = piston extend/retract (order AT last per GTMC intra-tick)
- [Rails](/concepts/rails.md) — rails drive adjacent pistons via their NC-update emission
- [Flying Machines](/concepts/flying-machines.md) — Slime Tech flying machines sequence piston pushes/pulls over 9/10/12gt
- [Slime Tech Engines and Mobility](/concepts/slime-tech-engines.md) — engine definition + mobilizing structures
- [Linkages](/concepts/linkages.md) — zero-delay piston-chain retraction, BUD linkages
- [detection-methods](/concepts/detection-methods.md) — push-limit detection in practice
- [moving-block-b36](/concepts/moving-block-b36.md) — B36 properties, hitbox, NBT
- **Cross-source:** TMWiki `Blocks/Piston.md` confirms block-event creation-order execution + 2-tick arrival (→ "3gt delay") and pushed-block order `-y;+y;-z;+z;-x;+x`. Aligns with GTMC. See [^tmwiki-piston].

[^gtmc-pistons]: https://www.techmc.wiki/en/articles/redstone-components/pistons
[^tmwiki-piston]: https://github.com/TechMCDocs/pages/blob/master/Blocks/Pistons.md
