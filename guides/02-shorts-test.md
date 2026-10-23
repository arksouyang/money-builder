# Guide 02: The Shorts test

**Question we're answering:** which of your 4 topics do people actually watch?
**How:** the same number of Shorts per channel, posted the same way, judged by the numbers, not by feelings.

## The 4 channels (confirm the mapping)
1. **Psychology**: your major, so lean on it. "Why your brain does X."
2. **World History**: one surprising story or "why did X happen" per Short.
3. **Anime & Webtoons**: theories, character breakdowns, recommendations. Talk to camera.
4. **Movies & TV**: same approach: takes, breakdowns, hidden details.

**Copyright rule for 3 and 4:** you on camera, with little or no clips or panels. YouTube allows reused footage only when your video is meaningfully different from the original, and copyright still applies on top of that. Rights holders have gone after anime commentary channels in 2026. Your face and your opinion are the content.

## Format
- **30–60 seconds**, vertical, face + voice.
- **First 2 seconds = the hook.** Start mid-thought, never "Hey guys."
- **Burned-in captions** (many people watch muted).
- **One idea per Short.** The end can tease the next one.

## Weekly rhythm (~9 hrs, all estimates)
| Block | Time | What |
|---|---|---|
| Script batch | ~1.5 h | With Claude: 6 scripts (hook + 3 beats + ending). Mix the 4 channels. |
| Film batch | ~1.5 h | Film all 6 in one sitting. Same spot, same light, phone camera. |
| Edit | ~4.5 h | ~45 min per Short: cut, captions, title. Gets faster with practice. |
| Post | ~1 h | YouTube Shorts first, then TikTok + Reels (same file). |
| Track | ~30 min | Once a week: fill in the 7-day numbers in `content-tracker.csv`. |

**Editing: CapCut Pro + Claude rough cut**
1. AirDrop the raw clips from your phone to the SSD (`work/raw/`).
2. *(If the rough-cut tool is built)* A local Claude Code session cuts the pauses, evens out the volume, frames it 9:16, and suggests titles. Output goes to `work/rough/`.
3. Open each in **CapCut Pro**: auto-captions, hook text, music. Export to `work/final/`.
4. Upload the **same clean export** to YouTube Shorts, TikTok, and Reels. Never re-upload a video downloaded from another app (watermarks).

**Laptop space:** keep footage on the SSD, never the Mac's internal drive. In CapCut's settings, point the project and cache folders at the SSD if possible.

## Fair-test rules
- **Same number per channel** before judging (Round 1: 5 each; Round 2: 10 each).
- **Wait 7 days** after posting before recording a Short's numbers.
- **Judge the median, not the best.** One lucky viral Short doesn't make a winner.
- **Main signals, in order:**
  1. **Average % viewed** (do people stay?)
  2. **Views** (does the algorithm push it?)
  3. **Subs gained per Short** (do people want more?)
- Rotate posting days so no channel always gets the "good" day.

## Reassessment (after Round 2: 40 Shorts)
With Claude, look at `content-tracker.csv` per channel and decide:
- **Winner(s):** move to longform + keep Shorts as trailers.
- **Middle:** keep at low frequency or merge into the winner's angle.
- **Losers:** pause (not delete).
