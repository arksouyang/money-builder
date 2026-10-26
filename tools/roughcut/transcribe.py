r"""Transcribe raw takes with word-level timestamps.

Usage: .venv\Scripts\python tools\roughcut\transcribe.py "raw vids\<name>.mp4" ...
Writes work\transcripts\<name>.json (list of words with start/end in seconds).
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
os.environ.setdefault("HF_HOME", str(ROOT / "hf-cache"))

from faster_whisper import WhisperModel  # noqa: E402

# Names from the scripts, so Whisper spells them right.
PROMPT = (
    "Psychology Shorts. Inside Out, Bing Bong, Joy, Sadness, Pixar, matching hypothesis, "
    "Cohen and Wills. Cast Away, Tom Hanks, Chuck, Wilson, Holt-Lunstad. The Bear, Carmy, "
    "Friedman and Rosenman, Type A, cardiologists, upholsterer, hostility, Yes, Chef. "
    "Ellen Langer, Judith Rodin, nursing home, houseplant."
)


def main(paths):
    out_dir = ROOT / "work" / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    model = WhisperModel("medium.en", device="cpu", compute_type="int8", cpu_threads=12)
    for p in map(Path, paths):
        # Decode with ffmpeg ourselves (faster-whisper's PyAV decoder breaks with newer PyAV).
        pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(p), "-ac", "1", "-ar", "16000",
                              "-f", "f32le", "-"], check=True, capture_output=True).stdout
        segments, _ = model.transcribe(
            np.frombuffer(pcm, np.float32), word_timestamps=True, initial_prompt=PROMPT,
            condition_on_previous_text=False, beam_size=5,
        )
        words = []
        for seg in segments:
            for w in seg.words:
                words.append({"w": w.word.strip(), "s": round(w.start, 3),
                              "e": round(w.end, 3), "p": round(w.probability, 3)})
        (out_dir / f"{p.stem}.json").write_text(json.dumps(words, indent=1), encoding="utf-8")
        print(f"{p.name}: {len(words)} words")


if __name__ == "__main__":
    main(sys.argv[1:])
