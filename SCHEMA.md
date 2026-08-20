---
type: doc
---

# Wiki Schema — MC Technical Wiki

## Domain
Technical Minecraft mechanics. Java Edition unless a page says otherwise. Source material is primarily **Graduate Texts in Minecraft (GTMC)**, decompiled against `1.20.1-yarn`, cross-checked against Technical Minecraft Wiki (TechMCDocs/pages), Minecraft Wiki, Bilibili, and TechMC-Glossary. Treat every mechanical claim as **version-sensitive** — exploits and behaviors change per Minecraft version.

## Language rule (do not violate)
- **Concept pages are English only.** Every file under `concepts/` is written in English. No Chinese / other-language translations inside concept page bodies. The wiki is a reference, not a translation deliverable.
- **A source MUST be translated to English before it is ingested.** Any non-English source (e.g. a Chinese Bilibili original) is translated to English as a `raw/articles/<name>-en.md` companion **before** any concept page is compiled from it. Ingestion of a concept from a non-English source without its `-en` translation is not allowed. The original non-English source may also be kept in `raw/articles/` as provenance, but the English `-en` file is what concepts are compiled from.
- **Translation of sources is our own step.** We translate at ingest into the `-en` raw file. It is NOT delegated to TechMCTranslationWorkflow — we only share *source-repo provenance* with that project, not a translation pipeline.
- Term definitions in `[[glossary]]` are **English term + English definition**, like a normal wiki. Source-language names (e.g. Chinese community terms) may appear ONLY as a brief parenthetical for disambiguation, or as original-author proper nouns in source attribution — but are never the page's purpose.
- Rationale: user wants the wiki fully English; non-English material is translated to English before it enters the concept layer, and confined to `raw/` as source/provenance.

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
- **English only** — see Language rule above. No translations in page bodies.

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

## Source repositories (provenance)
Same set as README "Sources" + index.md. All ingested captures live in `raw/articles/`, sha256-tracked:
- `techmc-wiki/articles` (GTMC) — primary
- `TechMCDocs/pages` (TMWiki) — 2nd source
- `minecraft.wiki` — 3rd cross-source
- `TechMC-Glossary/TechMC-Glossary` — term definitions
- Bilibili creators (per-article attribution)

## OKF (Open Knowledge Format) compliance
This vault is an **OKF v0.2** bundle. Authoritative spec:
`https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md` (v0.2).
Contract (derived from SPEC.md, not from the validator's tolerance):
- **Concept = one `.md` file.** File path (minus `.md`) = concept id / link target (§2, §6).
- **Required frontmatter:** `type` (short string; producer-defined values allowed, e.g. `concept`, `source`, `doc`). §4.1.
- **Recommended frontmatter:** `title`, `description` (one-line agent summary), `resource` (URI of the asset the concept describes), `tags` (list), plus the v0.2 provenance/trust/lifecycle families (§5).
- **Provenance — `sources:` is a LIST of entries** (§5.1), NOT a bare string list:
  ```yaml
  sources:
  - id: gtmc-rails
    resource: https://www.techmc.wiki/en/articles/redstone-components/rails
    title: GTMC — Rails
  ```
  `resource` is REQUIRED within an entry and SHOULD be a concrete artifact a consumer can follow (canonical URL, or a bundle-relative path, or a `references/`-style path). Our `raw/articles/*.md` files are local mirrors kept for drift detection; the canonical `resource` points at the upstream URL.
- **Per-claim attribution uses markdown footnotes** keyed to `sources[].id` (§5.1): `claim.[^gtmc-rails]` with `[^gtmc-rails]: GTMC — Rails` at the bottom. NOT inline `^[raw/...]` carets.
- **Freshness — `generated: { by, at }`** (§5.2). `by` uses the actor convention (§7): `/` for agents, `human:` for people, `process:` for automation. The v0.1 `timestamp` field is SUPERSEDED (§13.1) — do not use it.
- **Trust — `verified:`** (§5.2/§5.3): list of `{ by, at }` verification events. `human:` verifier ⇒ human-reviewed tier. Our `confidence:` field is an extra producer key (allowed) but does NOT replace `verified`.
- **Lifecycle — `status:`** (§5.4): `draft | stable | deprecated`. Absent ⇒ `stable`.
- **Links:** ordinary markdown, two forms — bundle-relative (leading `/`, recommended, §6.1) or relative. Broken links are tolerated (§6.1). Obsidian also renders `[[wikilinks]]`; path links are canonical for OKF consumers.
- **`index.md`** = progressive-disclosure entry (§8; may carry `okf_version: "0.2"` in frontmatter, the only permitted frontmatter). **`log.md`** = dated changelog, headings `## YYYY-MM-DD` (§9).
- **Reserved filenames:** only `index.md` + `log.md` (§3.1). Every other `.md` is a concept document — including `README.md`/`SCHEMA.md`, which we type as `doc` (producer-defined, legal) but are repo docs, not knowledge concepts.
- **`raw/articles/` split:** our convention (sources as `type: source` concepts + `concepts/` as compiled `type: concept`). This is NOT an OKF requirement — OKF has no source/resource division — but it is legal (producer-defined types) and the validator tolerates it. Provenance is encoded per §5.1 above, not via the directory alone.
- Paths are stable (git-backed). Renaming a concept file breaks inbound edges — treat paths as identity.
- English-only (see Language rule). No translations in page bodies.
- **Footnote formatting (Obsidian + OKF):** citations use `[^id]` inline references and `[^id]: <url>` definitions at the bottom (OKF v0.2 §5.1). CRITICAL: the footnote-definition block must be **preceded by a blank line** — Obsidian fails to register defs attached directly to a preceding list/paragraph, which breaks ALL footnotes in the file (they render as literal `.id` text). Every `[^id]:` def must have a URL or `/concepts/` path (a def with no link target also breaks Obsidian's parser). Lint must flag: (a) any `[^id]:` not preceded by a blank line, (b) any `[^id]:` whose target is not `http(s)://` or `/concepts/`.
- **No stray files:** migration/heredoc steps must not leave temp `.md` files in the repo root (a `^gtmc-...md` junk file once appeared). Clean up temp scripts and verify `git status` is clean after any batch edit.

## Pitfalls
- GTMC is **Java 1.20.1**. Never generalize a Java mechanic to Bedrock without a Bedrock source.
- "Basics section" in GTMC may use generalized (slightly imprecise) statements marked with superscripts — the precise version is in the Advanced section. Prefer the precise statement.
- 1.14-and-below behavior (jungle/acacia height increase, spruce retractable wall) is explicitly out of scope for the 1.15+ pages — do not mix them.
