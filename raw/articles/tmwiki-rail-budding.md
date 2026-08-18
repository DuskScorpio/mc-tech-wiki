---
source_url: https://github.com/TechMCDocs/pages/blob/master/GameMechanics/RailBudding.md
source_repo: TechMCDocs/pages (Technical Minecraft Wiki)
ingested: 2026-08-18
sha256: 9223d317cf52bd8bcb8ceccd4be9bbd8d5a2c339b7ec81ab747302bcec5162f0
---

# Rail Budding (TMWiki)

## Powering mechanics
- A rail that is updated does NOT send further updates if it is already in the correct state (no power/depower change needed).
- Block-update notifiers are always from above to below: top notifier if sloped, then notifier on self, then notifier below.
- If you only push the rail without changing its state, it sends updates only around itself.
- On power/unpower, a rail sends updates around the block below, and above if sloped, to notify rails going up/down of the power change.
- It searches for a power source through connected rails in the same direction, pointed to by the previous rail (upward if sloped, else same level or below), within a limit of **9 rails including itself**.
- A rail can point to another that does not point back -> rail searches power only one way (acts like a diode).
- Sometimes a rail cannot update another rail pointing into it -> the rest of the rails get BUDded. Classic BUD setup: place power source, place another where rail already powered, remove first -> no rails unpower (update didn't change state, no further updates), but some are budded (no power source within 9 blocks).
- General BUD methods (dust redirection, moving detector rail) also work on rails.

## Instant BUD wires
Bud a long rail line, then rebud the whole line: detect rail depowering + rebud here via redstone dust redirection or moving detector rail; or moving power source using rail update order that updates observers (observers repower the line, depower with next observer powering, ending at a permanently powered tail without updating budded rails).
