---
type: source
source_url: https://www.techmc.wiki/en/articles/tree-farm/high-speed-intro
ingested: 2026-08-18
sha256: b2a62f792d7510ec9160cdfc88fdbdf43546fd15a42fa7eb127025bf83559b2c
---

# 04 Why Your Tree Farm Is Slow — Introduction to High-Speed Tree Farms (GTMC)

Barring any surprises, the tree farm you designed in the previous chapter probably tops out around 10,000 efficiency, with processing cycles easily stretching past 30 or even 40gt.

## 1 Before We Begin — 0-tick

Minecraft's timing is divided into **inter-tick timing** and **intra-tick timing**. If we can move functionality from inter-tick to intra-tick timing, we've successfully sped up a tree farm. The most important way to do this is through the **piston action and wiring pattern** known as **0-tick**.

### 1.1 The Concept of 0-tick
BE components (pistons and note blocks) execute operations in the order they receive updates confirming state changes. This order is sometimes called **depth**. Note blocks do not increase depth.

So imagine a piston: At 0gt BE, it receives a rising edge signal at a certain depth. After it extends, it receives a falling edge signal at a deeper depth (deeper means later in the BE execution queue). Obviously, it should extend when powered and retract when depowered. This completes a **0-tick action**. For sticky pistons, the first block it pushes arrives one piston depth deeper than the falling edge signal, while pulling behaves normally.

### 1.2 Common 0-tick Generators
The idea: before BE ends within the same gt, give the piston a rising edge at an earlier point and a falling edge at a later point, and we get a 0-tick action.

Classic 0-tick generator based on the execution order difference between comparators and repeaters in TT. Another based on Redstone Dust (Redstone Dust is instantaneous). Note that Redstone Dust turning only triggers PP updates; we need additional NC updates to the target piston to complete the rising edge signal.

## 2 "Base"

For high-speed tree farms, we need to design bonemealing, detection, trunk processing, and sapling cycling as an integrated unit, called the **base**.

### 2.1 Trunk Processing
Trunk processing generally has four methods: processing together with the trunk, **upward push**, **downward suction**, and **side suction**. Processing together with the trunk means we can only use one dispenser for bonemealing. With upward push, we can plant trees at the earliest at 6gt. Downward suction gets us to 3gt, and side suction can be as fast as 0gt. In high-speed tree farms, we generally choose downward suction or side suction.

### 2.2 Bonemealing and Sapling Cycling
Bonemealing in high-speed tree farms essentially means **stacking dispensers**. Don't worry about bone meal consumption. Place as many bonemealing dispensers as possible to increase pre-bonemealing cycles and widen the growth window. This introduces **cross bonemealing**, which staggers when dispensers fire bone meal, generally by 2gt.

The biggest problem high-speed bonemealing faces comes from sapling cycling. Crowded base space causes the bone meal supply chain and sapling cycling hoppers to constantly clash.

For sapling cycling, since leaves drop sticks, we need more droppers. We also need to "straighten" the hopper chain and adopt a zoned collection strategy.

### 2.3 Push-Limit Detection
This is a push-limit detection unit made by Bright_Observer. When the upward-pushing piston is updated during the TT phase, it plans its push. When a piston plans to push, it checks whether it has reached the push limit. This unit runs at an **8gt cycle**. To align with the cross bonemealing clock, we can stack four layers of this unit, each staggered by 2gt.

## 3 Core Architecture — Trunk and Leaves Processing

### 3.1 Timing Design
For a given architecture, we need to analyze how it processes trees and design the shortest possible timing. In tree farms, we can generally think of time in 3gt units.

### 3.2 Architecture Design
If timing design on existing architectures still doesn't get you to the speed you need, you need to design faster architectures. Designing faster architectures comes down to: reduce piston actions that must occur at different macro timings.

## 4 Wiring

### 4.1 Wiring Methods
A classic **double-edge 0-tick generator** based on Redstone Dust and depth. Connect a sticky piston to its output, pushing and pulling a redstone block, to get a signal with the same macro timing as the input that doesn't increase macro delay but has a deeper rising edge.

### 4.2 Wiring Inspection
Analyze your wiring and see exactly where the timing problem is. For high-speed farm wiring, the best approach is to study and wire a few yourself.

*Created: 2024-12-28 | Last edited: 2026-07-17*
*License: CC BY-NC-SA 4.0 (GTMC Collective)*
