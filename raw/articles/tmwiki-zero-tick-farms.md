---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/BugsAndExploits/ZeroTickFarms.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: b6a724a872bea3ada3067b0d8365ed92e2b5c4159cb95fea2895565e970c3b72
---

# Zero-Tick Farming (TMWiki)

A Zero-Tick Farm relies on replacing the block a CROP (which grows on top of itself) is resting on, forcing it to grow a stage. **Patched in 20w12a; does NOT work in 1.16+.**

## Mechanic
Deleting the block a plant rests on schedules a tile tick on some crops that don't break instantly. The crop then checks 1 gt later if it should now break. If the block has been replaced before that check, it executes the rest of the tile tick that grows the plant — normally only called when the plant is randomticked.

> IMPORTANT DISTINCTION: This is CROP zero-ticking (e.g. cactus/sugar cane/other self-stacking crops), a growth bug patched in 1.16. It is NOT the same as the GTMC "0-tick" REDSTONE GENERATORS used in tree farms ([[0-tick]]), which exploit intra-tick piston/redstone depth and still work. Do not conflate the two.
