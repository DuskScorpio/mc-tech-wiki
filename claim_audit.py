#!/usr/bin/env python3
"""
claim_audit.py — OPTIONAL manual aid for the SCHEMA "Claim-to-source
traceability" rule. NOT part of the blocking pre-commit hook.

Why separate: structural lint cannot judge whether a citation actually
supports a claim (semantic attribution). A keyword-presence heuristic is
unreliable (false positives), so it must not block commits. This script
merely *surfaces* citations whose claim sentence shares no topical keyword
with the cited raw file, for the author to verify by reading the source.

Run:  python claim_audit.py [concept.md ...]
      (no args = all concepts)
Exit code is always 0 (informational only).
"""
import sys, os, re, glob

VAULT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(VAULT, 'raw', 'articles')
CON = os.path.join(VAULT, 'concepts')
FN_DEF = re.compile(r'^\[\^([a-z0-9_-]+)\]:\s*(.*)$', re.M)
FN_REF = re.compile(r'\[\^([a-z0-9_-]+)\]')
RE_RAW = re.compile(r'raw/articles/([a-z0-9_-]+)\.md')
STOP = set('the a an and or of to in for with is are was were be been being this that these those it its as at by from on into not no but if then than so such can may will would should could must every most all some any each only also e.g i.e via per under over above below out up down their our your his her they we you he she them us which who what when where why how more less using used use uses make makes made get gets got see sees our their'.split())

def audit(paths):
    for p in paths:
        t = open(p, encoding='utf-8').read()
        fn = os.path.basename(p)
        defmap = {}
        for m in FN_DEF.finditer(t):
            tm = re.match(r'\[[^\]]*\]\(([^)]+)\)', m.group(2).strip())
            if tm and RE_RAW.search(tm.group(1)):
                defmap[m.group(1)] = RE_RAW.search(tm.group(1)).group(1)
        raw_ids = set(os.path.basename(x)[:-3] for x in glob.glob(os.path.join(RAW, '*.md')))
        raw_text = {r: open(os.path.join(RAW, r + '.md'), encoding='utf-8').read().lower()
                    for r in raw_ids}
        print(f"\n=== {fn} ===")
        flagged = 0
        for m in FN_REF.finditer(t):
            cid = m.group(1)
            if cid not in defmap or defmap[cid] not in raw_ids:
                continue
            raw_id = defmap[cid]
            start = t.rfind('.', 0, m.start()); start = 0 if start < 0 else start + 1
            end = t.find('.', m.end()); end = len(t) if end < 0 else end
            sent = t[start:end]
            # keywords: real words, exclude the source id token + markers
            kws = [w for w in re.findall(r'[a-z][a-z-]{4,}', sent.lower())
                   if w not in STOP and raw_id not in w and cid not in w
                   and 'raw/articles' not in w]
            hit = [k for k in kws if k in raw_text[raw_id]]
            if not hit and kws:
                flagged += 1
                print(f"  ? [^{cid}] -> {raw_id}.md  | claim: {sent.strip()[:90]}")
                print(f"      keywords not found in source: {', '.join(kws[:8])}")
        if flagged == 0:
            print("  (no keyword mismatches — still verify attributions by reading sources)")

if __name__ == '__main__':
    args = sys.argv[1:]
    paths = [a for a in args] if args else sorted(glob.glob(os.path.join(CON, '*.md')))
    # filter to existing files
    paths = [p for p in paths if os.path.isfile(p)]
    if not paths:
        paths = sorted(glob.glob(os.path.join(CON, '*.md')))
    audit(paths)
