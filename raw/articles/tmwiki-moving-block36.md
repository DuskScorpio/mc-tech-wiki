---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/Blocks/MovingBlock36.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: 0a402cbe685d314c742f5747c9692a67fdf964a5b22b7cba09a8cad4f9d0067d
---

# Moving Block (Block 36) — B36 (TMWiki)

Moving_Piston is commonly called B36 / Block 36 (pre-Flattening ID 36). Created by pistons when pushing; the piston head also converts to B36. Not redstone-conductive; invisible but has a hitbox.

## Useful properties
- Prevents falling blocks from aging (won't break while inside B36).
- Block Tags: dragon_immune, wither_immune.
- Entities can see through it but cannot pathfind through it.
- Only destructible by explosion.
- Unreplaceable by the player (can't mine/replace by right-clicking with another block item).

## Hitbox
B36 hitbox can be offset from its actual position. Example: piston facing world border with water beyond; power+break piston → invisible B36 on far side, with hitbox still server-side at original position (tile entity not processed outside border / in border-loaded chunks). When processed, tile entity moves hitbox + colliding entities by half a block; piston extensions are 3 ticks, so 3 times; final tick turns B36 back into normal blocks. Final tick can be forced in the block event phase when a sticky piston retracts a B36, or a headless sticky piston retracts into a B36 with a movable block in front.

## Creating a B36
Hard without it converting back. Tile-entity-less B36 possible pre-1.17 (data stored globally since 1.17, so no longer). Post-1.19 can be created via update suppression in the tick (crash) — see UpdateSuppression.

## Tile entity data (/data get block)
- blockState: the moving block represented.
- Name: namespaced ID. Properties (optional): block states.
- Extending: 1/0 (true/false) — true if being pushed.
- Facing: 0=down,1=up,2=north,3=south,4=west,5=east.
- Progress: how far moved.
- Source: 1/0 — true if represents the piston head itself.

Cross-check vs GTMC: GTMC calls it "b36" and covers instant placement (finish) + normal 3gt arrival. TMWiki adds hitbox-offset + NBT + creation methods. Complementary.
