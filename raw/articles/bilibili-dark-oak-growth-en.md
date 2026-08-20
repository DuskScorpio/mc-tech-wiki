---
type: source
source_url: https://www.bilibili.com/opus/1031059770508836903
source_original: raw/articles/bilibili-dark-oak-growth.md
ingested: 2026-08-18
sha256: b2622444be8009f3b6bbe2f8335c4ba23d9f95e85e1e35601018a64f2c45665c
---

# Dark Oak Growth Mechanics (English translation of the Bilibili opus) — Scorpio (天蝎君)

> English translation of `raw/articles/bilibili-dark-oak-growth.md` (original Chinese,
> Scorpio 天蝎君, edited 2025-02-09, Java ~1.21.x). This `-en` file is the source that
> concept pages are compiled from, per the SCHEMA.md Language rule (translate before ingest).
> The original is kept for provenance.

## Statement (声明)
Most of this article is cited from @Sine_Chen's dark oak article, with help on code review
from @1uu1, @Wormbo, @Dreaming_Galaxy, and @幽帘幽梦 during writing.

## Growth detection range
1. Saplings must be planted as a 2×2 of four saplings (in plan view).
2. Centered on the **northwest-corner sapling** (the sapling above the gold block): above it
   (not counting the sapling layer) needs a clear column **3×7×3 (min) to 3×10×3 (max)**,
   and below the final height at least **5×3×5** (X×Y×Z).
3. The space may contain: air, water, various leaves, logs, stripped logs, fungus stems,
   stripped fungus stems, hyphae, stripped hyphae.
4. From point 2, dark oak can be **height-limited or height-boosted**.

## Log growth mechanics
### 1. Trunk
(1) Trunk area is 2×2, and no corner grows an extra log (unlike large spruce).
(2) Trunk grows at most 9 and at least 6 blocks tall.
(3) The trunk may bend, only toward east / south / west / north.
(4) Bending starts at one of the top 1–3 layers of the trunk, shifting the whole trunk
    1 or 2 blocks (for a 9-tall trunk, bending may start at layer 9, 8, or 7).
(5) A 2-block bend = shift 1 block, then shift 1 more block on the next layer up; the
    second bend direction is the same as the first.
(6) If the 2×2 trunk's **NW corner already has a log**, that layer's other logs do not
    grow — but side branches are unaffected.
(7) If the trunk bends and the bent trunk's NW corner already has a log, that layer's
    other logs likewise do not grow.

### 2. Side branches
(1) Grow within the 12-block ring around the 2×2 root, each column has a 1/3 chance
    (so branch count is random, 0–12 possible).
(2) Branch growth range does not move with trunk bending.
(3) Branch length is random 2–4 blocks, growing downward from one layer below the trunk top.
(4) Overall, branch growth lower bound is one above the root; upper bound is one below the
    final trunk top.

## Leaf growth mechanics
### 1. Trunk
(1) Trunk leaves consist of three or four layers.
(2) Grow upward from one layer below the trunk top, centered on the trunk top (if the trunk
    bends, centered on the bent trunk).
(3) Leaves bottom-to-top: 6×6, 8×8, 6×6, 2×2 (the 2×2 layer has a 1/2 chance of not growing).
    In actual growth they are not complete squares — corners are partially missing.

### 2. Side branches
(1) Branch leaves consist of three to four layers, bottom-to-top: 3×3, 5×5.
(2) In actual growth they are not complete squares — corners are partially missing.
(3) They grow from the same layer as the branch top, centered on the branch.
(4) If the trunk bends, the center shifts the same direction by the same amount (this was
    **fixed in 1.21.4** — newer versions ignore the bend for centering: MC-237375).
