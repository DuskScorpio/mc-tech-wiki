---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/block-entities
ingested: 2026-08-18
sha256: 6368b0c845bdc03414dc7b3bfb9bcae3b04b5b00a1ee5a34d76b594cabd8f71d
---

# 04 Block Entities (GTMC)

## 1 Block entities
Give blocks: data storage, extra logic, the three capabilities. Bound to a block position (one instance per pos). Added/removed with block; update suppression can keep BE after block removed.

## 2 Notable
### Hopper (block entity)
Data: inventory, transferCooldown, lastTickTime, facing.
Workflow each gt: decrease cooldown; execute transfer. Output (insert()) first, then pull from above; on success set cooldown.
- Hopper-to-hopper special timing: when target hopper empty, `from` applies 8gt cooldown but `to` subtracts 1 on its next tick -> effectively 7gt.

### Moving Piston (b36)
BE data: pushedBlock, facing, extending, source, progress, savedWorldTime. Workflow: progress>=1 -> places pushedBlock (final).

## 3 Timing between block entities (advanced)
Two lists in LevelChunk: pendingBlockEntityTickers, blockEntityTickers (both ArrayLists -> insertion order).
- New BE during tick -> pending; otherwise blockEntityTickers.
- On reload, order within chunk follows BlockPos.hashCode(); across chunks follows chunk load order.
- TL;DR: before unload, order = placement order; after reload, within-chunk = pos hash, across-chunks = load order.
