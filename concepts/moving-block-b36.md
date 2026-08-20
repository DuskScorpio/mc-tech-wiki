---
type: concept
title: Moving Block (B36)
created: 2026-08-18
updated: 2026-08-18

description: '`Moving_Piston` = "B36" / "Block 36" (pre-Flattening ID 36).'
edition: java
version: 1.20.1
confidence: high
tags: [mechanics, piston-action, b36, source-tmwiki, source-gtmc]
sources:
- id: tmwiki-moving-block36
  resource: https://github.com/TechMCDocs/pages/blob/master/Blocks/MovingBlock36.md
  title: TechMCDocs/pages (Technical Minecraft Wiki)
- id: gtmc-pistons
  resource: https://www.techmc.wiki/en/articles/redstone-components/pistons
  title: GTMC Pistons
generated: { by: /, at: "2026-08-18T00:00:00Z" }
status: stable
---

# Moving Block (B36)

`Moving_Piston` = "B36" / "Block 36" (pre-Flattening ID 36). Created by pistons when pushing; the piston head also becomes B36. Not redstone-conductive; invisible but has a hitbox.[^tmwiki-moving-block36]

## Properties (useful in farms)
- Prevents falling blocks from aging (won't break inside B36).
- Tags: dragon_immune, wither_immune.
- Entities see through but can't pathfind through it.
- Only destructible by explosion.
- Unreplaceable by player right-click.[^tmwiki-moving-block36]

## Hitbox offset
B36 hitbox can sit offset from its logical position (e.g. at the world border, tile entity unprocessed → hitbox stays server-side at origin). When processed, entity moves hitbox + entities by half a block per tick; 3 ticks for a full extension. Final convert-back tick can be forced in BE phase when a sticky piston retracts a B36.[^tmwiki-moving-block36]

## NBT (`/data get block`)
`Extending` (1/0), `Facing` (0=down..5=east), `Progress` (0..1), `Source` (1 if piston head itself).[^tmwiki-moving-block36]

## Arrival in tree farms
Normal arrival = 3gt (GTMC "3-gt piston delay"); instant placement (`finish`) forces arrival in BE. See [piston-mechanics](/concepts/piston-mechanics.md).

## Related
- [piston-mechanics](/concepts/piston-mechanics.md) — arrival timing, instant placement
- [piston-action-timing](/concepts/piston-action-timing.md) — how arrival slots into the action budget

[^tmwiki-moving-block36]: [tmwiki-moving-block36.md](raw/articles/tmwiki-moving-block36.md)