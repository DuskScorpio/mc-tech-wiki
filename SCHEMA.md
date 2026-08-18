# Wiki Schema — MC Technical Wiki (Tree Farms)

## Domain
Technical Minecraft mechanics, focused initially on tree farms. Java Edition unless a page says otherwise. All source material so far is from **Graduate Texts in Minecraft (GTMC)**, decompiled against `1.20.1-yarn`. Treat every mechanical claim as **version-sensitive** — exploits and behaviors change per Minecraft version.

## Correctness rules (this is the whole point)
- Every wiki page MUST carry `edition:` and `version:` frontmatter. No exceptions.
- Every mechanical claim that comes from a source gets a `^[raw/articles/file.md]` marker at the end of the paragraph/sentence.
- `confidence:` is required: `high` only when the claim is directly stated in the curated source AND not contradicted; `medium` for inferred/synthesized claims; `low` for anything unverified or version-uncertain.
- If two sources disagree, do NOT silently pick one. Mark `contested: true`, record both with dates/versions, and flag for human review.
- Raw sources are IMMUTABLE. Corrections go in wiki pages, never by editing `raw/`.

## Conventions
- File names: lowercase, hyphens, no spaces (`trunk-processing.md`).
- Every wiki page starts with YAML frontmatter (see below).
- Use `[[wikilinks]]` between pages (min 2 outbound links per page).
- On update, bump `updated:` date.
- Every new page added to `index.md` under the correct section.
- Every action appended to `log.md`.

## Frontmatter (wiki pages)
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | entity | comparison | query
edition: java | bedrock
version: 1.20.1        # or "1.15+" for claims that hold across versions
confidence: high | medium | low
contested: false
tags: [from taxonomy]
sources: [raw/articles/gtmc-tree-farm-basics.md]
---
```

## Frontmatter (raw sources)
```yaml
---
source_url: https://...
ingested: YYYY-MM-DD
sha256: <auto-filled by ingest script>
---
```
Raw files are append-only. The ingest script (terminal) computes sha256 over the body (everything after the closing `---`) so re-ingests can detect source drift.

## Tag Taxonomy
Add new tags HERE before using them.
- mechanics: timing, updates, piston-action, redstone-phase, block-update, micro-timing, dust-update, qc, bud
- structures: architecture, base, module, block-stream
- structures: architecture, base, module, block-stream
- methods: detection, bonemealing, trunk-processing, leaf-processing, sapling-recycling, block-to-drop
- techniques: 0-tick, dustless, high-speed, clock, cross-bonemealing
- trees: birch, oak, spruce, jungle, acacia, dark-oak, cherry, azalea
- farms: tree-farm, 4gt, multi-species, large-spruce
- meta: source-gtmc, version-sensitive

## Page Thresholds
- Create a page when a concept appears in 2+ sources OR is central to one source (e.g. a whole GTMC chapter).
- Split when a page exceeds ~200 lines.
- Archive to `_archive/` when fully superseded by a newer version-specific page.

## Related vaults (cross-link later, do not auto-merge)
- `C:\GitHub Related\TechMC-Glossary` — GTMC glossary, useful for `[[term]]` definitions.
- `C:\GitHub Related\tmc-glossary-web` — web build of the same glossary.

## Pitfalls
- GTMC is **Java 1.20.1**. Never generalize a Java mechanic to Bedrock without a Bedrock source.
- "Basics section" in GTMC may use generalized (slightly imprecise) statements marked with superscripts — the precise version is in the Advanced section. Prefer the precise statement.
- 1.14-and-below behavior (jungle/acacia height increase, spruce retractable wall) is explicitly out of scope for the 1.15+ pages — do not mix them.
