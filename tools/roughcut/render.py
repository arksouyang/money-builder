r"""Render a vertical Short from a raw landscape take and an edit list.

Usage: .venv\Scripts\python tools\roughcut\render.py tools\roughcut\edits\P01.json

Edit list (JSON):
  source   raw file, relative to the repo root
  out      output file, relative to the repo root
  hook     on-screen hook text for the first seconds
  keep     [[start, end, zoom?], ...] source seconds to keep, in order; zoom 0/1 picks the
           framing (default: alternate on every cut)
  fixes    {"heard": "correct"} caption word replacements (matched case-insensitively)
  word_fixes [[source_time, "correct"], ...] replace only the word starting nearest that time
  stills   [{"src_start": s, "src_end": e, "image": "work/stills/x.jpg", "label": "..."}]
           shows the image (or a labelled placeholder if the file is missing) over those source seconds

Style: jump cuts on every kept piece, alternating normal / punched-in framing that follows the
face, word-by-word captions (current word yellow), loudness normalised to -14 LUFS.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parents[2]
W, H, FPS = 1080, 1920, 30
PUNCH = 1.18           # zoom on every other cut
PAD_IN, PAD_OUT = 0.04, 0.10
FONT = "Arial Black"
CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def face_center(cap, s, e, src_w, src_h):
    """Median face centre over 7 frames spread across [s, e]; None if no face is found."""
    xs, ys, sizes = [], [], []
    for k in range(7):
        cap.set(cv2.CAP_PROP_POS_MSEC, (s + (e - s) * (k + 0.5) / 7) * 1000)
        ok, frame = cap.read()
        if not ok:
            continue
        small = cv2.resize(frame, (src_w // 3, src_h // 3))
        faces = CASCADE.detectMultiScale(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY), 1.1, 4, minSize=(60, 60))
        if len(faces):
            x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
            xs.append((x + w / 2) * 3)
            ys.append((y + h / 2) * 3)
            sizes.append(h * 3)
    if not xs:
        return None
    xs.sort(); ys.sort()
    return xs[len(xs) // 2], ys[len(ys) // 2]


def crop_for(cx, cy, src_w, src_h, zoom):
    ch = src_h / zoom
    cw = ch * W / H
    x = min(max(cx - cw / 2, 0), src_w - cw)
    y = min(max(cy - ch * 0.42, 0), src_h - ch)   # face sits a bit above centre
    return int(cw) // 2 * 2, int(ch) // 2 * 2, int(x), int(y)


def ass_time(t):
    t = max(t, 0)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def ass_escape(text):
    return text.replace("\\", "").replace("{", "(").replace("}", ")")


def build_pages(words):
    """Group words into caption pages of up to 3 words / 18 letters, breaking on pauses and punctuation."""
    pages, cur = [], []
    for w in words:
        too_long = len(" ".join(x["w"] for x in cur + [w])) > 18
        if cur and (len(cur) == 3 or too_long or w["s"] - cur[-1]["e"] > 0.35
                    or re.search(r"[.?!,:]$", cur[-1]["w"])):
            pages.append(cur)
            cur = []
        cur.append(w)
    if cur:
        pages.append(cur)
    return pages


def write_ass(path, words, hook, hook_end):
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{FONT},84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,-1,0,0,0,100,100,0,0,1,7,3,2,80,80,560,1
Style: Hook,{FONT},92,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,22,0,8,90,90,260,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    if hook:
        lines.append(f"Dialogue: 1,{ass_time(0)},{ass_time(hook_end)},Hook,,0,0,0,,"
                     r"{\q0\fad(0,150)\t(0,120,\fscx100\fscy100)\fscx85\fscy85}" + ass_escape(hook.upper()))
    events = []
    for page in build_pages(words):
        texts = [ass_escape(w["w"].upper()) for w in page]
        for i, w in enumerate(page):
            start = w["s"]
            end = page[i + 1]["s"] if i + 1 < len(page) else w["e"] + 0.15
            parts = []
            for j, t in enumerate(texts):
                parts.append(r"{\c&H0000E5FF&}" + t + r"{\c&H00FFFFFF&}" if j == i else t)
            pop = r"{\fscx88\fscy88\t(0,90,\fscx100\fscy100)}" if i == 0 else ""
            events.append([start, end, pop + " ".join(parts)])
    # Never let two caption events overlap, or libass draws them on top of each other.
    for a, b in zip(events, events[1:]):
        a[1] = min(a[1], b[0])
    for start, end, text in events:
        if end - start > 0.01:
            lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Cap,,0,0,0,,{text}")
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def placeholder(path, label):
    """Grey card with the still's description, so the slot is visible until the real image arrives."""
    import numpy as np
    img = np.full((760, 940, 3), 60, np.uint8)
    cv2.rectangle(img, (0, 0), (939, 759), (0, 229, 255), 8)
    y = 330
    for line in ["STILL GOES HERE:"] + re.findall(r".{1,28}(?:\s|$)", label):
        cv2.putText(img, line.strip(), (50, y), cv2.FONT_HERSHEY_DUPLEX, 1.4, (255, 255, 255), 2, cv2.LINE_AA)
        y += 60
    cv2.imwrite(str(path), img)


def main(edit_path):
    edit = json.loads(Path(edit_path).read_text(encoding="utf-8"))
    src = ROOT / edit["source"]
    out = ROOT / edit["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    words = json.loads((ROOT / "work" / "transcripts" / f"{src.stem}.json").read_text(encoding="utf-8"))
    fixes = {k.lower(): v for k, v in edit.get("fixes", {}).items()}
    for t, text in edit.get("word_fixes", []):
        min(words, key=lambda w: abs(w["s"] - t))["w"] = text
    # Glue stray tokens like "%" or "-charge" onto the word before.
    merged = []
    for w in words:
        if merged and w["w"] and not w["w"][0].isalnum() and w["w"][0] not in "\"(":
            merged[-1] = {**merged[-1], "w": merged[-1]["w"] + w["w"], "e": w["e"]}
        else:
            merged.append(dict(w))
    words = merged

    cap = cv2.VideoCapture(str(src))
    src_w, src_h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    tmp = Path(tempfile.mkdtemp(prefix="roughcut_"))
    pieces, cap_words, stills_out = [], [], []
    t_out = 0.0
    for i, k in enumerate(edit["keep"]):
        s, e = k[0], k[1]
        zoomed = k[2] if len(k) > 2 else i % 2
        s0, e0 = max(s - PAD_IN, 0), e + PAD_OUT
        dur = e0 - s0
        found = face_center(cap, s0, e0, src_w, src_h)
        if found is None:  # no face this piece: keep the last framing
            found = prev[1:] if i else (src_w / 2, src_h * 0.4)
        cx, cy = found
        # Same framing as the last piece and the face barely moved: hold the crop so it doesn't jitter.
        if i and zoomed == prev[0] and abs(cx - prev[1]) < 80:
            cx, cy = prev[1], prev[2]
        prev = (zoomed, cx, cy)
        cw, ch, x, y = crop_for(cx, cy, src_w, src_h, PUNCH if zoomed else 1.0)
        piece = tmp / f"p{i:03d}.mp4"
        fade = min(0.015, dur / 4)
        run(["ffmpeg", "-y", "-ss", f"{s0:.3f}", "-t", f"{dur:.3f}", "-i", str(src),
             "-vf", f"crop={cw}:{ch}:{x}:{y},scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p",
             "-af", f"afade=t=in:d={fade},afade=t=out:st={dur - fade:.3f}:d={fade},aresample=48000",
             "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-c:a", "pcm_s16le", str(piece)])
        pieces.append(piece)
        shift = t_out - s0
        for w in words:
            if w["s"] >= s0 - 0.01 and w["e"] <= e0 + 0.05 and s - 0.05 <= (w["s"] + w["e"]) / 2 <= e + 0.05:
                text = w["w"]
                key = re.sub(r"[^\w'-]", "", text).lower()
                if key in fixes:
                    text = re.sub(re.escape(re.sub(r"[^\w'-]", "", text)), fixes[key], text, flags=re.I)
                cap_words.append({"w": text, "s": w["s"] + shift, "e": min(w["e"], e0) + shift})
        for st in edit.get("stills", []):
            a, b = max(st["src_start"], s0), min(st["src_end"], e0)
            if a < b:
                stills_out.append({**st, "a": a + shift, "b": b + shift})
        t_out += dur
    cap.release()

    concat_list = tmp / "list.txt"
    concat_list.write_text("".join(f"file '{p.as_posix()}'\n" for p in pieces), encoding="utf-8")
    joined = tmp / "joined.mkv"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(joined)])

    hook_end = min(2.8, t_out)
    ass = tmp / "caps.ass"
    write_ass(ass, cap_words, edit.get("hook", ""), hook_end)

    # Stills: card in the upper half with a quick scale-in, captions stay on top.
    inputs, chain, last = ["-i", str(joined)], [], "0:v"
    for k, st in enumerate(stills_out):
        img = ROOT / st["image"]
        if not img.exists():
            img = tmp / f"ph{k}.png"
            placeholder(img, st.get("label", st["image"]))
        inputs += ["-loop", "1", "-t", f"{t_out:.3f}", "-i", str(img)]
        a, b = st["a"], st["b"]
        chain.append(f"[{k + 1}:v]scale=940:-2,pad=iw+16:ih+16:8:8:white,format=rgba,"
                     f"scale=w='iw*min(1,0.85+0.15*(t-{a:.3f})/0.12)':h=-2:eval=frame[s{k}]")
        chain.append(f"[{last}][s{k}]overlay=x=(W-w)/2:y=700-h/2:enable='between(t,{a:.3f},{b:.3f})'[v{k}]")
        last = f"v{k}"
    ass_arg = ass.as_posix().replace(":", r"\:")
    chain.append(f"[{last}]subtitles='{ass_arg}'[vout]")
    run(["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(chain), "-map", "[vout]", "-map", "0:a",
         "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000",
         "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", "-t", f"{t_out:.3f}", str(out)])
    print(f"{out.relative_to(ROOT)}: {t_out:.1f}s, {len(edit['keep'])} cuts, {len(stills_out)} stills")


if __name__ == "__main__":
    main(sys.argv[1])
