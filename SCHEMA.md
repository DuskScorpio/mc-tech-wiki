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
- trees: birch, oak, spruce, jungle, acacia, dark-oak, cherry, azalea, mangrove
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
- **Concept = one `.md` file.** File path (minus `.md`) = concept id / link target (OKF SPEC §2 Terminology, §6 Cross-linking and paths).
- **Required frontmatter:** `type` (short string; producer-defined values allowed, e.g. `concept`, `source`, `doc`). OKF SPEC §4.1.
- **Recommended frontmatter:** `title`, `description` (one-line agent summary), `resource` (URI of the asset the concept describes), `tags` (list), plus the v0.2 provenance/trust/lifecycle families (OKF SPEC §5).
- **Provenance — `sources:` is a LIST of entries** (OKF SPEC §5.1), NOT a bare string list:
  ```yaml
  sources:
  - id: gtmc-rails
    resource: https://www.techmc.wiki/en/articles/redstone-components/rails
    title: GTMC — Rails
  ```
  `resource` is REQUIRED within an entry and MUST be the **canonical upstream URL** (the source of truth, used for OKF consumers + drift detection). Our `raw/articles/<id>.md` files are local mirrors of every cited source.
- **Citation split (enforced):** `sources[].resource` = canonical URL (machine-readable, OKF). The bottom `[^id]:` footnote block = a **local mirror link** `raw/articles/<id>.md` (human-clickable in Obsidian, offline). Every `sources[]` id MUST have a downloaded `raw/articles/<id>.md` mirror, and every `[^id]:` def MUST point to that local file (never a URL). Raw mirrors are PRISTINE source extracts — no annotations, no `[[wikilinks]]` (see No stray files / raw-purity rule).
- **Per-claim attribution uses markdown footnotes** keyed to `sources[].id` (OKF SPEC §5.1): `claim.[^gtmc-rails]` with `[^gtmc-rails]: raw/articles/gtmc-rails.md` at the bottom. NOT inline `^[raw/...]` carets.
- **Freshness — `generated: { by, at }`** (OKF SPEC §5.2). `by` uses the actor convention (OKF SPEC §7): `/` for agents, `human:` for people, `process:` for automation. The v0.1 `timestamp` field is SUPERSEDED (OKF SPEC §13.1) — do not use it.
- **Trust — `verified:`** (OKF SPEC §5.2/§5.3): list of `{ by, at }` verification events. `human:` verifier ⇒ human-reviewed tier. Our `confidence:` field is an extra producer key (allowed) but does NOT replace `verified`.
- **Lifecycle — `status:`** (OKF SPEC §5.4): `draft | stable | deprecated`. Absent ⇒ `stable`.
- **Links:** ordinary markdown, two forms — bundle-relative (leading `/`, recommended, OKF SPEC §6.1) or relative. Broken links are tolerated (OKF SPEC §6.1). Obsidian also renders `[[wikilinks]]`; path links are canonical for OKF consumers.
- **`index.md`** = progressive-disclosure entry (OKF SPEC §8; may carry `okf_version: "0.2"` in frontmatter, the only permitted frontmatter). **`log.md`** = dated changelog, headings `## YYYY-MM-DD` (OKF SPEC §9).
- **Reserved filenames:** only `index.md` + `log.md` (OKF SPEC §3.1). Every other `.md` is a concept document — including `README.md`/`SCHEMA.md`, which we type as `doc` (producer-defined, legal) but are repo docs, not knowledge concepts.
- **`raw/articles/` split:** our convention (sources as `type: source` concepts + `concepts/` as compiled `type: concept`). This is NOT an OKF requirement — OKF has no source/resource division — but it is legal (producer-defined types) and the validator tolerates it. Provenance is encoded per §5.1 above, not via the directory alone.
- Paths are stable (git-backed). Renaming a concept file breaks inbound edges — treat paths as identity.
- English-only (see Language rule). No translations in page bodies.
- **Frontmatter must be strict-valid YAML.** Lint with a real YAML parser (`yaml.safe_load`), NOT regex. Known failure modes that pass lenient checks but break the OKF viewer ("Invalid properties"): list items inside `sources:`/`tags:` with a **leading space** before the `-` (e.g. ` - id:` instead of `- id:`), unquoted backticks/`"` in `description:`, and unterminated blocks. The OKF `OKFDocument.validate()` only checks `type`, so it will NOT catch these — strict YAML parsing is required. Every concept file must pass `yaml.safe_load(frontmatter)` with no exception (this is the same check the OKF visualizer runs).
- **Footnote formatting (Obsidian + OKF):** citations use `[^id]` inline references and `[^id]: [file.md](raw/articles/file.md)` definitions at the bottom (OKF v0.2 §5.1). CRITICAL: (1) the def block must be **preceded by a blank line**. (2) refs are SINGLE-bracket `[^id]` — NEVER `[[^id]]` (double creates a stray note). (3) footnote **ids must be URL/path-safe** (only `[a-z0-9_-]`): no spaces, no dots, no `:`. (4) every `[^id]:` def MUST be a markdown link to the local mirror `raw/articles/<id>.md` (enforced citation split — see Provenance above); NEVER a bare URL or `/concepts/` path. A spaced/malformed id (e.g. `[^ Sapling]`) is unresolvable. Lint must flag: `[[^id]]` double-bracket; id with space/illegal char; def not preceded by blank line; def not a markdown link to an existing `raw/articles/<id>.md`.
- **No stray files:** migration/heredoc steps must not leave temp `.md` files in the repo root (a `^gtmc-...md` junk file once appeared). Clean up temp scripts and verify `git status` is clean after any batch edit.
- **Automated guardrail (enforced):** `vault_lint.py` is the single source of truth for ALL the rules above (raw purity + sha256, strict YAML, OKF validate, `sources[]`→mirror + graph-visibility, footnote formatting/clickability, no carets/double-brackets/spaced-ids). It runs as a **git `pre-commit` hook** (install via `bash install-hooks.sh`) and **blocks any commit that violates a HIGH/MED rule** — so the past issues (raw contamination, malformed/non-clickable footnotes, unconnected sources, stale carets, non-strict YAML, OKF "Invalid properties") cannot be reintroduced by a careless edit. Run `python vault_lint.py` locally to see violations before committing. `OKF_SRC` env var points the hook at the knowledge-catalog validator if not at the default path.

## Pitfalls
- GTMC is **Java 1.20.1**. Never generalize a Java mechanic to Bedrock without a Bedrock source.
- "Basics section" in GTMC may use generalized (slightly imprecise) statements marked with superscripts — the precise version is in the Advanced section. Prefer the precise statement.
- 1.14-and-below behavior (jungle/acacia height increase, spruce retractable wall) is explicitly out of scope for the 1.15+ pages — do not mix them.
