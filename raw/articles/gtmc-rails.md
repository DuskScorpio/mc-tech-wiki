---
source_url: https://www.techmc.wiki/en/articles/redstone-components/rails
ingested: 2026-08-18
sha256: 8d19fd64932876a55c02a1048b33056cccaf2b41d4b7d71baaae1a5bc066d5a7
---

# 01 Rails (GTMC)

## 1 Rail Updates
Special rails (Powered, Activator, Detector) have special update ranges, unlike plain rails.

### 1.1 Powered/Activator Rail Updates
Powered and Activator Rails share the `PoweredRailBlock` class -> identical update behavior. When activation state changes, they emit NC updates in sequence:
- Flat rail: 4 NC updates, sources **itself -> below -> itself -> below**.
- Sloped rail: 6 NC updates, sources **above -> itself -> below -> itself -> below -> above** (above only if sloped).
So a sloped rail emits the top-ends extra. These NC updates are what let rails power adjacent pistons/BUDs.

### 1.2 Detector Rail Updates
Not yet completed (GTMC article).

## 2 Rail Activation Detection ("rails" = Powered + Activator here)
### 2.1 Activation methods
Two ways to activate a rail:
- **Direct activation:** rail directly adjacent to a redstone signal source.
- **Indirect activation:** among the 8 rails connected to it (excluding itself), at least one is directly adjacent to a signal source.

### 2.2 "Connected" judgment (the search)
A non-directly-activated rail searches for a connected, directly-activated rail within 8 blocks of itself, walking along the rail chain.
- Flat rail checks: both ends at same height; both ends one block lower.
- Sloped rail checks: lower end at same height; lower end one block lower; higher end one block higher.
- Connectivity depends on (a) own shape (sloped?), (b) next rail's position, (c) next rail's direction. **Independent of the next rail's shape.**
- Therefore **connectivity is unidirectional**: rail A may consider B connected while B does not consider A connected -> one-directional rail signal chains (diode behavior).

### 2.3 Direction of search
Each end searched independently, unidirectional (no backtracking).
- N-S rails: search south first, then north.
- E-W rails: search west first, then east.
So which rails count as connected depends on distance AND search-direction order.

> Footnote: PoweredRail and ActivatorRail are both `PoweredRailBlock`; identical at source level. Their different effects on minecarts are handled by the minecart, not the rail.
