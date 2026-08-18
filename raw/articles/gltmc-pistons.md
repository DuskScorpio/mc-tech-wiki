---
source_url: https://www.techmc.wiki/en/articles/redstone-components/pistons
ingested: 2026-08-18
sha256: fbb66a2db19fcf96c45417d198ce5ce59ba93196d18f9df86434122340bd9fae
---

# 02 Pistons (GTMC)

> Decompiled against 1.20.1-yarn.

## Composition
- Piston = base + head. States: retracted / extended. Can create **headless piston** (base only) or head-only.

## Self-check mechanism
- Trigger: (a) placed by player (onPlaced -> tryMove), (b) NC update (neighborUpdate -> tryMove), (c) onBlockAdded when block type changed and no block entity.
- Self-check is instantaneous, can occur at any stage; "attempt" doesn't guarantee success.
- **Redstone signal check / QC**: piston checks first-order adjacency of itself and the block ABOVE it. shouldExtend: checks piston's own 6 directions (excluding facing) for redstone power; then block below; then block ABOVE's 6 directions. This is why QC works and why BUDs only detect NC.

## Push / pull and movable blocks
- Movable block must satisfy: not immovable, size of moved list <= 12 (push limit), structure analysis passes.
- Piston maintains movedBlocks and brokenBlocks lists; alternating linear + branch (stack) analysis. Use Fallen_Breath's PistOrder mod to view order in-game.
- b36 arrival/reverse lists give b36 arrival and destruction order.

## b36 and block placement
- Normal: in Block Entity phase, b36 adds 0.5 progress/tick; from 0gt AT, fully placed at 3gt AT -> "3-gt piston delay."
- **Instant placement (finish)**: triggered when sticky piston has b36 one block outside extension direction with matching movement direction, or piston head position is b36 (instant retract). Instant sets progress=1.0, removes b36 entity, replaces with original block, sends updates. Only affects the one block directly in front of the sticky piston.
- Instant push does NOT displace surrounding entities or remove waterlogged status.

## Piston event response (onSyncedBlockEvent)
- actionType: 0 = extend, 1 = retract, 2 = instant retract.
- Instant retract (actionType 2) when target b36 is extending with progress <0.5 or same tick, etc.

## Push limit detection (advanced)
- "Deceiving" the piston: planned action may differ from actual push structure at execution. Core of push-limit detection (discovered by _Kayleigh and Landmining; simplified by Bright_Observer). Used in tree-farm detection.

## Piston head (advanced)
- canSurvive: piston head valid iff block behind (opposite push dir) is an extending piston with same facing, OR b36 behind with same dir.
- PP update behind -> canSurvive check; invalid -> disappears. NC update never removes head.

*Created 2024-12-28 | Last edited 2026-07-17. License CC BY-NC-SA 4.0.*
