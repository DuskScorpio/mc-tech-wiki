---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/GameTick/TileTicks.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: a994423b82437209a138a9f10137067be76b22b55744466bca0bcb91224bc5aa
---

# Tile Ticks (TMWiki)

Tile ticks = actions scheduled to happen in N ticks at a block. On execution, the block acts per its type.

## Tile tick phase
Game selects scheduled tile ticks whose processing tick (tick# + delay) ≤ current tick, moves them to an execution list. Some components (observers, lamps) don't check if a tile tick is already in the executing list before scheduling (MC-189954). Two schedulers run back-to-back: block ticks, then fluid ticks.

## Tile tick cap
Max 65536 tile ticks execute per tick; unexecuted ones delay to next tick.

## Player input bug
Player inputs execute after block event phase and before world counter increment. A player-input-created tile tick schedules from the current tick; depending on where you split ticks, it either loses 1gt of delay or its block event only runs next tick.

## Delay length (gt)
Tall Plants / Leaves / Command Blocks = 1; Sand, Anvil, Concrete powder = 2; Repeater = 2/4/6/8; Comparator = 2; Redstone Torch = 2; Observer = 2; Lectern = 2; Dispenser = 4; Dropper = 4; Redstone Lamp = 4; Dragon Egg = 5; Water = 5; Lightning Rod = 8; Target = 8; Tripwire Hook = 10; Tripwire = 10; Weighted Pressure Plate = 10; Stone Button & Pressure Plate = 20; Detector Rail = 20; Composter = 20; Wooden Button & Pressure Plate = 30; Lava = 30; Big Dripleaf = 10/10/100.
*Tall plants: Big Dripleaf Stem, Bamboo, Cactus, Sugar Cane, Weeping/Twisting Vines, Kelp, Chorus Plant/Flower, Cave Vines.
*Water/lava use fluid ticks.

## Tile tick priority (TTP)
Higher priority = lower value executes first. TTP only relevant to repeater/comparator (everything else = 0).
SCHEDULED TICK PRIORITIES:
- Redstone diode? YES → Repeater facing another diode? YES → PRIORITY -3; NO → Powering -1 / Depowering -2.
- Comparator facing another diode? YES → -1; NO → 0.
- Not a diode → 0.
- Special: unpowered repeater not receiving power when ticked → -2.
- "Facing another diode" means "facing a diode that is NOT facing it."

Cross-check vs GTMC: confirms repeater 2/4/6/8gt and comparator 2gt ([[tick-micro-timing]]). Adds precise TTP and cap.
