---
title: Piston Mechanics
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, source-gtmc]
sources: [raw/articles/gltmc-pistons.md]
---

# Piston Mechanics

Piston = base + head; states retracted/extended. A **headless piston** (base only) believes its head still exists in front of it.^[raw/articles/gltmc-pistons.md]

## Self-check & QC
- Self-check triggers: placed by player (onPlaced→tryMove), NC update (neighborUpdate→tryMove), or onBlockAdded when block type changed.
- Self-check is instantaneous and can happen at any stage; "attempt" may fail.
- **shouldExtend** checks the piston's own 6 directions (excluding facing), then the block BELOW, then the block ABOVE's 6 directions. This is the origin of **QC** and why BUDs only detect NC updates.^[raw/articles/gltmc-pistons.md]

## Push / pull
- A block is movable only if not immovable and the moved list stays ≤ **12** (push limit).
- Structure analysis uses movedBlocks + brokenBlocks lists (alternating linear/branch on a stack). Use Fallen_Breath's **PistOrder** mod to view attempt order in-game.
- b36 arrival/removal order = reverse of the moved/broken lists.^[raw/articles/gltmc-pistons.md]

## b36 (moving_piston) & placement
- Normal: b36 gains 0.5 progress/tick in the TE phase; from 0gt AT it's fully placed at **3gt AT** → the "3-gt piston delay".^[raw/articles/gltmc-pistons.md]
- **Instant placement (finish):** triggered when a sticky piston has a b36 one block outside its extension direction with matching movement direction, or when the piston-head position is b36 (instant retract). Progress set to 1.0, original block placed, updates sent — but only the single block in front of the sticky piston. No entity displacement, no waterlogged removal.^[raw/articles/gltmc-pistons.md]

## Push-limit detection (advanced)
- "Deceiving" the piston: its planned action can differ from the actual push structure at execution time. Core of **push-limit detection** (discovered by _Kayleigh and Landmining; simplified by Bright_Observer) — the detection method used in tree farms. See [[detection-methods]].^[raw/articles/gltmc-pistons.md]

## Piston head (advanced)
- `canSurvive`: head valid iff the block behind (opposite push dir) is an extending piston with same facing, OR a b36 behind with same dir.
- PP update behind → canSurvive check (invalid → disappears). NC update never removes the head.^[raw/articles/gltmc-pistons.md]

## Related
- [[piston-action-timing]] — 3gt default, 0-tick
- [[update-theory]] — QC/Bud wiring
- [[tick-micro-timing]] — BE phase = piston extend/retract
- [[detection-methods]] — push-limit detection in practice
- [[moving-block-b36]] — B36 properties, hitbox, NBT
- **Cross-source:** TMWiki `Blocks/Piston.md` confirms block-event creation-order execution + 2-tick arrival (→ "3gt delay") and pushed-block order `-y;+y;-z;+z;-x;+x`. Aligns with GTMC. See ^[raw/articles/tmwiki-piston.md].
