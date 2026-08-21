#!/usr/bin/env python3
"""
vault_lint.py — single source of truth for mc-tech-wiki invariants.

Encodes EVERY rule established during the vault's cleanup (2026-08). Running
this with zero HIGH/MED failures means the vault is internally consistent:
raw mirrors pristine, concept pages OKF-valid with graph-visible local
citations, footnotes clickable in Obsidian, no contamination.

Designed to run in a git pre-commit hook (exit non-zero => block commit).

Severity model:
  HIGH  -> blocks commit (structural / provenance / OKF break)
  MED    -> blocks commit (Obsidian rendering or graph break)
  LOW    -> warning only (does not block)

Run:  python vault_lint.py            (exit 1 if any HIGH/MED)
      python vault_lint.py --strict   (also fail on LOW)
"""
import sys, os, re, glob, hashlib, argparse
try:
    import yaml
except ImportError:
    yaml = None

VAULT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(VAULT, 'raw', 'articles')
CON = os.path.join(VAULT, 'concepts')
META = ['README.md', 'SCHEMA.md', 'index.md', 'log.md', 'todo.md']

# OKF validator (optional; repo still lints if not present).
# Search common locations so the hook works regardless of where kc/ is cloned.
OKF = None
_OKF_CANDIDATES = [
    os.environ.get('OKF_SRC', ''),
    os.path.join(os.path.dirname(VAULT), 'kc', 'okf', 'src'),
    r'C:/Hermes-Workspace/kc/okf/src',
    os.path.join(VAULT, 'kc', 'okf', 'src'),
]
for _c in _OKF_CANDIDATES:
    _c = _c.strip()
    if not _c or not os.path.isdir(_c):
        continue
    try:
        sys.path.insert(0, _c)
        from reference_agent.bundle.document import OKFDocument
        OKF = OKFDocument
        break
    except Exception:
        continue

ANNOT_VOICE = re.compile(r'(Cross-check vs|IMPORTANT DISTINCTION|our wiki|Do not conflate|NOTE:|TODO|FIXME)')
FN_DEF = re.compile(r'^\[\^([a-z0-9_-]+)\]:\s*(.*)$', re.M)
FN_REF = re.compile(r'\[\^([a-z0-9_-]+)\]')
FN_ID_SAFE = re.compile(r'^[a-z0-9_-]+$')
SRC_ID = re.compile(r'-\s*id:\s*(\S+)')
CARET = re.compile(r'\^\[raw/')


def err(sev, f, d, bag):
    bag.append((sev, f, d))


def lint_raw(bag):
    for p in sorted(glob.glob(os.path.join(RAW, '*.md'))):
        fn = os.path.basename(p)
        t = open(p, encoding='utf-8').read()
        if t.count('---') < 2:
            err('HIGH', fn, 'raw missing frontmatter delimiters', bag); continue
        fm = t.split('---', 2)[1]; body = t.split('---', 2)[2]
        if 'type: source' not in fm:
            err('HIGH', fn, 'raw missing type: source', bag)
        if 'source_url:' not in fm:
            err('MED', fn, 'raw missing source_url', bag)
        m = re.search(r'sha256:\s*(\S+)', t)
        if not m:
            err('HIGH', fn, 'raw missing sha256', bag)
        else:
            h = hashlib.sha256(body.encode('utf-8')).hexdigest()
            if m.group(1).strip().strip('"') != h:
                err('HIGH', fn, 'raw sha256 mismatch (body changed without recompute)', bag)
        if '[[' in t:
            err('HIGH', fn, 'raw contains [[ wikilink (must be pristine)', bag)
        if '/concepts/' in t:
            err('HIGH', fn, 'raw contains /concepts/ link in body', bag)
        if ANNOT_VOICE.search(t):
            err('HIGH', fn, 'raw contains annotation voice (editorial contamination)', bag)
        if FN_DEF.search(t):
            err('MED', fn, 'raw contains footnote def in body', bag)


def lint_concept(bag):
    raw_ids = set(os.path.basename(x)[:-3] for x in glob.glob(os.path.join(RAW, '*.md')))
    for p in sorted(glob.glob(os.path.join(CON, '*.md'))):
        fn = os.path.basename(p)
        t = open(p, encoding='utf-8').read()
        if t.count('---') < 2:
            err('HIGH', fn, 'concept missing frontmatter', bag); continue
        fm = t.split('---', 2)[1]
        if yaml is not None:
            try:
                yaml.safe_load(fm)
            except Exception as e:
                err('HIGH', fn, f'strict YAML FAIL: {str(e).splitlines()[0][:90]}', bag); continue
        else:
            err('LOW', fn, 'PyYAML unavailable; skipped strict-YAML check', bag)
        if OKF is not None:
            try:
                OKF.parse(t).validate()
            except Exception as e:
                err('HIGH', fn, f'OKF validate FAIL: {str(e)[:90]}', bag)
        else:
            err('LOW', fn, 'OKF lib unavailable; skipped OKF validate', bag)
        if not re.search(r'^type:\s*\S+', fm, re.M):
            err('HIGH', fn, 'concept missing type in frontmatter', bag)
        # sources[]
        sids = SRC_ID.findall(fm)
        if not sids:
            err('HIGH', fn, 'concept has no sources[] entries', bag)
        else:
            for sid in sids:
                if not re.search(r'-\s*id:\s*' + re.escape(sid) + r'\s*\n\s*resource:\s*\S+', fm):
                    err('MED', fn, f'source id {sid} missing resource', bag)
                if not re.search(r'-\s*id:\s*' + re.escape(sid) + r'\s*\n\s*resource:[^\n]*\n\s*title:', fm):
                    err('LOW', fn, f'source id {sid} missing title', bag)
                if sid not in raw_ids:
                    err('HIGH', fn, f'source id {sid} has NO raw/articles/{sid}.md mirror', bag)
        # footnote integrity
        refs = set(FN_REF.findall(t))
        defs = set(m.group(1) for m in FN_DEF.finditer(t))
        for r in refs:
            if r not in defs and r not in sids:
                err('HIGH', fn, f'inline footnote [^{r}] has no def and no sources[] id', bag)
            if not FN_ID_SAFE.match(r):
                err('HIGH', fn, f'footnote id "{r}" not [a-z0-9_-] safe (spaces/dots break Obsidian)', bag)
        for d in defs:
            if not FN_ID_SAFE.match(d):
                err('HIGH', fn, f'footnote def id "{d}" not [a-z0-9_-] safe', bag)
        # every def MUST be a markdown link to an existing local raw file (never a URL)
        for m in FN_DEF.finditer(t):
            val = m.group(2).strip()
            lm = re.match(r'\[([^\]]+)\]\(([^)]+)\)', val)
            if not lm:
                err('MED', fn, f'footnote def [^{m.group(1)}] not a markdown link: "{val[:60]}"', bag); continue
            target = lm.group(2)
            if target.startswith('http') or target.startswith('/'):
                err('MED', fn, f'footnote def [^{m.group(1)}] must point to local raw/articles/ (got "{target}")', bag)
            elif not os.path.exists(os.path.join(VAULT, target)):
                err('HIGH', fn, f'footnote def [^{m.group(1)}] links to missing file: {target}', bag)
        # stale caret citations
        if CARET.search(t):
            err('HIGH', fn, 'stale pre-OKF ^[raw/...] caret citation in body', bag)
        # double-bracket footnote (creates stray note)
        if re.search(r'\[\[\^[a-z0-9_-]+\]\]', t):
            err('HIGH', fn, 'double-bracket [[^id]] footnote (creates stray Obsidian note)', bag)
        # blank line before first def (Obsidian collapses footnotes otherwise)
        lines = t.split('\n')
        for i, l in enumerate(lines):
            if FN_DEF.match(l):
                if i > 0 and lines[i-1].strip() != '' and not FN_DEF.match(lines[i-1]):
                    err('MED', fn, f'footnote def at line {i+1} not preceded by blank line', bag)
                break
        # graph visibility: every sources[] id must be linked via markdown in SOME concept body
        # (checked globally in lint_graph below)


def lint_graph(bag):
    """Every raw source must be reachable by a markdown link from >=1 concept body
    (otherwise it is invisible/isolated in Obsidian's Graph View).
    Skipped when there are no concept files (e.g. a raw-only branch)."""
    concept_files = glob.glob(os.path.join(CON, '*.md'))
    if not concept_files:
        return
    raw_ids = set(os.path.basename(x)[:-3] for x in glob.glob(os.path.join(RAW, '*.md')))
    inbound = {r: 0 for r in raw_ids}
    for p in glob.glob(os.path.join(CON, '*.md')):
        t = open(p, encoding='utf-8').read()
        for r in raw_ids:
            if re.search(r'\]\(raw/articles/' + re.escape(r) + r'\.md\)', t):
                inbound[r] += 1
    for r, c in inbound.items():
        if c == 0:
            err('HIGH', r, 'source has NO inbound markdown link from any concept (isolated in Obsidian graph)', bag)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true', help='also fail on LOW')
    args = ap.parse_args()
    bag = []
    lint_raw(bag)
    lint_concept(bag)
    lint_graph(bag)
    # meta doc sanity (wikilinks allowed as prose; just report count)
    by = {'HIGH': [], 'MED': [], 'LOW': []}
    for sev, f, d in bag:
        by[sev].append(f"{f}: {d}")
    for sev in ['HIGH', 'MED', 'LOW']:
        if by[sev]:
            print(f"\n{sev} ({len(by[sev])}):")
            for it in by[sev]:
                print("  -", it)
    block = by['HIGH'] + by['MED']
    if args.strict:
        block += by['LOW']
    if not bag:
        print("OK: no problems found.")
    elif not block:
        print(f"\nOK: only LOW warnings ({len(by['LOW'])}).")
    else:
        print(f"\nFAILED: {len(block)} blocking issue(s) (HIGH+MED). Commit blocked.")
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
