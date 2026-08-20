---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/GameTick.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: 334c800467261f87d5bd6c98bc1086a34e29347a51533b559928fc436a38955c
---

# Game Tick (TMWiki)

A gametick (gt/tick) is part of the game loop where logic is processed. Commonly used technical-MC tick phases:
1. Block/fluid tile ticks
2. ChunkManager tick
3. BlockEvent processing
4. Regular entities ticking
5. Block entities ticking
6. Player actions and other scheduled tasks

## Block Event Phase detail
Block events (piston extend/retract, noteblock, chest/shulker/enderchest open/close, bell, gateway cooldown, mobspawner) stored in a LinkedHashSet (`synchedBlockEventQueue`), processed in order; a block event can chain another appended to the end (multiple in one tick).
- Order is BOTH locational and directional (hashset). Hash depends on position (x,y,z), block type+attributes, event type, event data.
- At processing, game re-reads the block at the event position; if it no longer matches, the event is skipped.
- Event types/data: Bell type1 (dir hit); Noteblock type0; Extending Piston type0 (facing); Retracting Piston type1 (facing); Moving Piston type2 (facing); Chest/Shulker/EnderChest type1 (viewer count); End Gateway type1; Mob Spawner type1.

## Tile Entity Phase
Moving blocks turn to normal blocks; moving blocks push entities / slime gives velocity; furnaces check inventory; hoppers push/pull; sculk sensors activate.

## Player Inputs Phase
Levers, buttons, place/break blocks.

## Recursive updators (instant updators)
Rails and redstone dust are calculated recursively, independent of ticks, can happen in ALL phases. (This is GTMC's "instant" component behavior.)

Cross-check vs GTMC intra-tick: TMWiki's phase list (tile ticks → ChunkManager → BlockEvent → entities → block entities → player inputs) aligns with GTMC's AT→...→BE→TE→EU ordering in substance; GTMC uses NU/TT/BE/TE/EU labels and adds NU. Both agree pistons act in BlockEvent/BE and B36 arrival in block entity/TE. Minor labeling difference, not a contradiction.
