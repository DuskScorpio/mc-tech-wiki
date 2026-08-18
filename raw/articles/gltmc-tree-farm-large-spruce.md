---
source_url: https://www.techmc.wiki/en/articles/tree-farm/large-spruce-farm
ingested: 2026-08-18
sha256: 1d0f884b0819578ee7052ae68a77dc2ffbd8b1df84392479428b56b827d8ab56
---

# 08 Large Spruce Tree Farms (GTMC)

Welcome to the definitive guide on mid-to-late game wood production. Here we'll walk you through designing the most log-efficient tree farm in Minecraft.

## 1 Introduction to Large Spruce Tree Farms

### 1.1 Large Spruce Growth Mechanics and Architecture Design
The growth detection range for large spruce is: **3x3 at the sapling layer (centered on the northwest corner sapling), expanding to 5x5 above**. The maximum height of a large spruce is 28 blocks (the northwest corner sapling gets one extra, for 29 total). We need double recursion to handle the trunk logs, then push the leaves away with honey-slime walls.

### 1.2 Vertical Signal Transmission — use stick BUD to pull it up. For trunk and side wall activation, consider redirecting dust or wall power.
### 1.3 Processing — after pushing out from the core, split left and right, then reassemble as usual. Without optimization, efficiency will only be around 100k.

## 2 High-Speed Large Spruce Part 1: Corner Down-Suction
### 2.1 Origin — In 2016, Laoxian released his 12gt large spruce tree farm (upward-pushing), breaking 300k. On 2020-02-12, gpw released sprucemacy v1 (observer-powered tree root detection + corner down-suction). On 2021-04-15, gpw released sprucemacy v2 (corner side-suction).
### 2.2 Concept — down-suction the corner log; gpw had the player plant the corner sapling at 8/10gt.
### 2.3 Limitations — In 1.14, Mojang modified player right-click placement. Llama boats broke in 1.21.

## 3 High-Speed Large Spruce Part 2: Corner Side-Suction (Corner Retraction)
### 3.1 Origin — 2021-04-15 gpw sprucemacy v2; 2022-02-08 floppy's 12gt Spruce v2 (3gt bonemealed planting); 2024-08 Qontrol developed a practically viable corner side-suction base with 6gt reset.
### 3.2 Concept — side-suction the corner; down-suction one log, conventional parallel side-suction for the other.
### 3.3 Too Difficult to Build — complexity is the biggest drawback.

## 4 High-Speed Large Spruce Part 3: The Return of Corner Down-Suction / Pig Boat Planting Timing
### 4.1 Auto-clicker planting timing for corner down-suction.
### 4.2 Why Pig Boats — minecarts roll away; single boats desync between client/server; llama boats broke.

## 5 ITT/IF 6gt Large Spruce
A god-tier tech from 1.12.

*Created: 2024-12-28 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
