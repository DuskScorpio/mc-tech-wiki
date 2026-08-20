---
type: source
source_url: https://github.com/TechMCDocs/pages/blob/master/Blocks/Piston.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: 79c90c1fb2d1f4cfa04f96355ea6e6555d5d22db730af088d590c85192c01217
---

# Piston (TMWiki)

## Activation mechanics
- Powered by adjacent block or QC (block above the piston).
- When updated, checks retract/extend. If yes and NOT pushlimited, creates a block event with its position + action, unless one already exists (except in 1.15).
- A piston trying to extend can fail; retraction cannot (if pushlimited, retracts without pulling).
- Block event phase: game iterates block event list in CREATION ORDER; re-checks at execution. A pulse that turns off before the block event phase won't extend the piston.

## Movement
- On activation, replaces pushed destinations with Moving_Piston (B36). Extending: sets extended, replaces front with B36 head. Retracting: replaces self with B36 of full extended hitbox.
- For the next TWO ticks (block entity phase), B36s move hitboxes (push entities). After 2 ticks, pushed blocks arrive & convert back.
- If a sticky piston's extension is interrupted by retraction, the directly pushed block arrives IMMEDIATELY (same tick retraction starts); retraction doesn't pull it → it's dropped. Achievable via 0/1/2-tick pulse. Indirectly pushed blocks arrive normally.

## Pushed blocks order
- Searches the line in front, nearest→farthest (push) or farthest→nearest (pull).
- Sticky blocks stored in order `-y;+y;-z;+z;-x;+x`, then re-searches added lines.
- Game loops the list in REVERSE creating moving blocks. Lines iterated farthest→nearest; tiebreaker `+x;-x;+z;-z;+y;-y` (reversed from before).

## Block updates on push
- Create B36 in front of each block to move; following update order, send state updates at each new block position; delete old blocks from hashmap (locational order); send block updates around all removed blocks + the moving piston head.

Cross-check vs GTMC: TMWiki's "2 ticks to arrive + convert" matches GTMC's "3gt piston delay" (0gt AT start → 3gt AT placed). Block-event re-check at execution = why a pre-BE-off pulse doesn't extend. Aligns.
