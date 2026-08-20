---
type: source
source_url: https://www.techmc.wiki/en/articles/micro-timing/scheduled-ticks
ingested: 2026-08-18
sha256: 27349296214875daf823aa12418575ab08c090c38658ef36e697b26419c4523c
---

# 03 Scheduled Ticks and Scheduled Tick Components (GTMC)

## 1 Concept
Scheduled Tick = "alarm" with only: triggerTick, subTickOrder, priority, pos, type. Carries no action detail; the block decides behavior on execution.
- Repeater: delay*2 gt. If locked, adds no scheduled tick, changes nothing on execution.
- Comparator: 2gt. Compare mode: powered change -> NC->PP->NC; unchanged -> NC. Subtract: powered change -> NC->PP->NC; level change only -> NC; both unchanged -> no update.
- Observer, Redstone Torch also scheduled-tick components (priority 0).
- Redstone torch burnout: lights 8x within 60gt -> burns out; recovers after 160gt or replace.

## 1.3 Execution order
triggerTick (macro) > priority (smaller=higher) > subTickOrder (add order). "Macro timing precedence over micro."

## 2.4 Scheduled Tick class
OrderedTick: type,pos,triggerTick,priority,subTickOrder. Hashing 31*pos.hashCode()+type.hashCode().
Chunk Tick Scheduler: PriorityQueue + ObjectOpenCustomHashSet (hash set dedups by type+pos).
- Method1 (add): fails if already in set -> component won't double-add.
- Method2 (isTicking): checks if will execute THIS gt (copy of queue) -> repeater won't re-add before its tick.
- Method3 (isQueued): observers use; same as Method1 (does NOT check current-gt) -> core of 4gt Observer high-frequency.

## 4.6 Executing scheduled ticks
collect -> run -> cleanup. World-level scheduler polls chunk schedulers by Simple Comparison (ignore triggerTick) -> Scheduled Tick Suppressors: high-frequency priority-0 in one chunk suppresses priority-0 in OTHER chunks (e.g. comparators not lighting). Limit maxmaxTicks per gt.
- This suppression is the basis of 4gt Observer high-frequency and relevant to 4gt tree farms.
