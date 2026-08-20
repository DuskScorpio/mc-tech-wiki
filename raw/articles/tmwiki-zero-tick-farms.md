---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/BugsAndExploits/ZeroTickFarms.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: 2f5047e97d3523b37c08696c08e2146619fed61ebe197298d937b7802f000d61
---

# Zero-Tick Farming (TMWiki)

A Zero-Tick Farm relies on replacing the block a CROP (which grows on top of itself) is resting on, forcing it to grow a stage. **Patched in 20w12a; does NOT work in 1.16+.**

## Mechanic
Deleting the block a plant rests on schedules a tile tick on some crops that don't break instantly. The crop then checks 1 gt later if it should now break. If the block has been replaced before that check, it executes the rest of the tile tick that grows the plant — normally only called when the plant is randomticked.

