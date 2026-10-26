r"""Print a transcript as timed phrases (split on pauses) to pick keep ranges by hand.

Usage: .venv\Scripts\python tools\roughcut\show.py "work\transcripts\inside out raw.json"
"""
import json
import sys

words = json.load(open(sys.argv[1], encoding="utf-8"))
line, start = [], None
for i, w in enumerate(words):
    if line and w["s"] - words[i - 1]["e"] > 0.45:
        print(f"[{start:7.2f}-{words[i - 1]['e']:7.2f}] {' '.join(line)}")
        line = []
    if not line:
        start = w["s"]
    line.append(w["w"] + ("?" if w["p"] < 0.5 else ""))
if line:
    print(f"[{start:7.2f}-{words[-1]['e']:7.2f}] {' '.join(line)}")
