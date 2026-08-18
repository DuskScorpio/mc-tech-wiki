---
title: Moving Block (B36)
created: 2026-08-18
updated: 2026-08-18
type: concept
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, b36, source-tmwiki, source-gtmc]
sources: [raw/articles/tmwiki-moving-block36.md, raw/articles/gltmc-pistons.md]
---

# Moving Block (B36)

`Moving_Piston` = "B36" / "Block 36" (pre-Flattening ID 36). Created by pistons when pushing; the piston head also becomes B36. Not redstone-conductive; invisible but has a hitbox.^[raw/articles/tmwiki-moving-block36.md]

## Properties (useful in farms)
- Prevents falling blocks from aging (won't break inside B36).
- Tags: dragon_immune, wither_immune.
- Entities see through but can't pathfind through it.
- Only destructible by explosion.
- Unreplaceable by player right-click.^[raw/articles/tmwiki-moving-block36.md]

## Hitbox offset
B36 hitbox can sit offset from its logical position (e.g. at the world border, tile entity unprocessed → hitbox stays server-side at origin). When processed, entity moves hitbox + entities by half a block per tick; 3 ticks for a full extension. Final convert-back tick can be forced in BE phase when a sticky piston retracts a B36.^[raw/articles/tmwiki-moving-block36.md]

## NBT (`/data get block`)
`Extending` (1/0), `Facing` (0=down..5=east), `Progress` (0..1), `Source` (1 if piston head itself).^[raw/articles/tmwiki-moving-block36.md]

## Arrival in tree farms
Normal arrival = 3gt (GTMC "3-gt piston delay"); instant placement (`finish`) forces arrival in BE. See [[piston-mechanics]].

## Related
- [[piston-mechanics]] — arrival timing, instant placement
- [[piston-action-timing]] — how arrival slots into the action budget
