---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/GameMechanics/BlockUpdates.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: e2077fb1e12532afd027bf6335a541ec9d7c93406476724d9c2f5839f0b505de
---

# Block updates and update detectors (TMWiki)

Minecraft has Updates. Redstone components, liquids, sand rely on them to decide if something needs doing.

## Block updates (Neighbor changed / "updates" / NC)
Created by:
- A block changing to another (player place in replaceable spot, fill cmd, falling block landing, trees setting blocks, block→Moving_Piston, dispenser placing/removing liquid/fire).
- Placing/removing redstone components & rails (by player or piston, including conversion to Moving_Piston).
- Some components changing state (powered rails, pressure plates/tripwire via mobs, repeater power/delay, comparator input/mode, note/bell power 1.13+, redstone dust power level, bubble columns, scaffolding distance, waterlogged→not).
- A tile tick executing and sending updates despite no state change (tripwires, comparators).

On receiving: may change state, break/remove self, schedule tick, schedule tick (liquids).

## State update (Observer / shape / post placement / PP)
Sent typically when a block changes state (see debug menu right side). Exceptions: blocks generated/loaded, sticky piston heads removed while retracting, moving powered observer turning to block (MC-107664).
- Most blocks sending state updates also send block updates; some (trapdoors) do NOT send block updates.
- Redstone dust sends state updates diagonally adjacent in some conditions but won't trigger observers there.
On receiving: change state, break/remove self, schedule ticks (falling blocks, liquids, scaffolding, leaves).

## Comparator updates
Update comparators without block updates (comparators also respond to block updates).
Created by: composter/cauldron fill change; inventory changes; hopper pulling; detector rail colliding with entity.
Detected ONLY by a comparator, and only if horizontally adjacent or 1 block away with a conductive block between.

## BUDs ("budded")
A block in a state where it will react to block updates is "Budded." BUDs react to block updates and reset after receiving them.
- Pistons budded by failing to extend when powered, or retracting into a powered position where they can't extend.
- Droppers/Dispensers/Pistons budded by QC.
- Powered/activator rails budded by power-state decisions.
- By piston pushing what powered it before finishing extension.
- Rails budded for direction/slope when moved.
- Redstone dust direction change buds components (sends no block updates).

Cross-check vs GTMC: TMWiki's "block update" = GTMC's NC; "state update" = GTMC's PP. Aligns.
