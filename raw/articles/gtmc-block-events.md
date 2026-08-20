---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/block-events
ingested: 2026-08-18
sha256: 95ec397bec3928f79fbb59c19d2825e6aeca492b788e55e41fc10f7577d1cb01
---

# 05 Block Events (GTMC)

## 1 What
Server->client "an event happened here, simulate locally" to save bandwidth. Block Event structure: pos, block(type), type(action), data(params).

## 2 Sources (key)
- Piston: Extend 0, Retract 1, Instant retract 2; data = direction 0-5.
- Note Block: 0 / 0. Bell: 1 / hit dir.

## 3 Block Event Delay (BED)
Events in same gt execute in fixed order = BED. Mental model: ticket queue FIFO. Depth: initial event depth0, events it directly causes depth1, etc (chain of cause).
- Example: 0gt AT lever pulled -> 1gt BE depth0 sticky piston retracts -> depth1 pulls podzol, dust changes -> depth2 bottom-retraction piston self-checks, extends -> depth3 powered block removed, bottom piston self-checks, queues retract but still extending -> 0t. 3gt TE all placed. 4gt BE depth0 top/bottom regular pistons extend... etc. (0t bottom retraction base in a tree farm is the canonical BED example.)
- Block event queue = BFS: FIFO, new events appended at tail in NC update order; execute all depth0, then depth1... multi-source BFS on "piston graph"; children join in NC update order (direction relative to parent); already-visited children not re-added.
