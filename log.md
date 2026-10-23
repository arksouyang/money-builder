# Session log

## 2026-10-22 — Session 1 (Thu evening, ET)

**What we did**
- Gathered context and verified platform facts by web search. Key finding: **YouTube doubles its Partner Program entry bar on Feb 1, 2027** (8,000 watch hrs or 20M Shorts views).
- Evaluated all ideas (see `ideas.md`). First pick was **bilingual sermon subtitles** (primary) + table tennis (secondary).
- Ark's answers changed the plan step by step:
  - Table tennis is out of the project.
  - Fall hold is **$3,800.48** after all aid. No grants or emergency funds. Partial payment doesn't lift it. Registration Mon Nov 9, 9 AM; can go ~1 week late. Parents would cover it at real cost to them.
  - Ark interprets **live**, doesn't want their own church involved, and doesn't want to interpret in person. Verified: YouTube's terms forbid downloading videos without permission.
  - Without the church, the subtitle plan became cold-messaging strangers, which **felt bad**. Content is the real dream, and Ark is now **OK with face + voice**.
- **New direction (end of session):** Shorts test across **4 YouTube channels** (Psychology, World History, Anime & Webtoons, Movies & TV), cross-posted to TikTok + Reels. Real estate excluded. Reassess after the test, then the winner goes longform.
- **Ark self-funds Claude Pro** for now (no cash side-path).
- Created and pushed: `CLAUDE.md`, `GOALS.md`, `ledger.csv`, `content-tracker.csv`, `ideas.md`, `log.md`, `.gitignore`, `guides/01-first-sermon.md` (parked except Step 1), `guides/02-shorts-test.md`.

**What worked**
- Honest check-in on *why* Ark wanted to switch. The subtitle plan would have failed on motivation, not on skill.

**What didn't**
- I built the first plan around a church network before knowing Ark wanted the church kept separate. Lesson: ask about boundaries earlier.

**Update (late Thu): accounts + editing**
- New `.archive` YouTube channels (one Google account can own all 4). New matching TikTok + Instagram accounts, never personal ones.
- Ark edits in **CapCut Pro** on the Mac. Verified: CapCut has no official automation API, so Claude won't edit inside CapCut. Offered: a Claude Code rough-cut tool → Ark polishes in CapCut.

**Open questions for Ark**
1. Exact `.archive` names + confirm topic mapping.
2. Build the rough-cut tool? (yes/no)
3. SSD format; credit card 0% end date.

---

### Plan: this weekend → Round 1 (20 Shorts by Sun Nov 15)
| Day | Time | Task |
|---|---|---|
| Thu 10/22 (tonight) | 0–15 min | Optional: jot 3 Short ideas per channel in your notes app. Then sleep. |
| Fri 10/23 | ~1 h | **Accounts:** create 4 new `.archive` YouTube channels under one Google account + 4 TikTok + 4 Instagram accounts with matching names (each needs its own email/phone). In CapCut settings, move the project/cache folders to the SSD. |
| Sat 10/24 | ~3–4 h | **Script 6 with Claude** (cloud or local session) → **film all 6** in one sitting (same spot, window light). Start editing. |
| Sun 10/25 | ~3 h | Finish editing. **Post the first Shorts** (at least 1 per channel). Log each one in `content-tracker.csv`. Commit + push. |
| Weekdays after | ~1–1.5 h/day | Weekly rhythm from `guides/02-shorts-test.md`: ~6 Shorts/week, rotating channels. |
| Sun 11/1 | 30 min | First check: fill in 7-day numbers for last weekend's Shorts. No judging yet, just recording. |
| Sun 11/15 | — | **Round 1 target: 20 posted (5 per channel).** |

Optional (whenever, local session on the Mac): `guides/01-first-sermon.md` Step 1 sets up speech-to-text on the SSD, which gives you auto-captions for your Shorts.

**Next step:** Friday, set up the accounts (~1 h). Saturday, script and film your first 6.

## 2026-10-23 — Session 2 (Fri, ET, local session on the Mac)

**What we did**
- Checked the SSD: **exFAT, 2 TB, ~1.95 TB free** (far more than the 200–300 GB we'd assumed). Symlinks work, so Node projects can live on it.
- Ark asked to install the tools from a TikTok workflow (FFmpeg, Remotion, yt-dlp):
  - **Installed FFmpeg 9.0.2 + Node 26** via Homebrew (~1 GB on the Mac; ~10 GB left).
  - **Remotion not installed yet.** It's a per-project library, so it goes inside the rough-cut tool's folder on the SSD. Free license covers Ark (verified).
  - **yt-dlp skipped on purpose:** it downloads other people's videos, which breaks YouTube's terms and our copyright rule.
- Decided: **build the rough-cut tool after the first footage is on the SSD.** Accounts and filming come first.
- Verified handle rules for YouTube/TikTok/Instagram (now in `CLAUDE.md`).
- Fixed `ledger.csv`: removed the Claude Pro −$20 row (it's self-funded, per the file conventions). Balance is $0.

**What worked**
- Checking the machine before installing (old Homebrew, tight laptop disk) kept the install small.

**Next step**
- Lock the 4 `.archive` names, then create the 4 YouTube channels + matching TikTok/Instagram accounts (~1 h). Saturday: script and film the first 6.

**Update (Fri): channel avatars + accounts plan**
- Account plan: **one new project Gmail** for everything. YouTube = 4 Brand Account channels under it. Instagram = extra accounts made from inside the first one. TikTok = try Gmail `+` aliases, and make extra Gmails only if TikTok rejects them.
- Ark picked handles in the `.archive` style (4 example sets given; the final set isn't recorded yet).
- Drew **4 profile pictures** in the style of Ark's Notion avatar (`brand/avatars/`): psych = thought bubble with a brain, history = bicorne hat, anime = sweat drop + anger vein, movies/TV = clapperboard. Each also has a `-color.png` version with its own background (psych lavender, history sage, anime pink, movies/TV yellow) so the accounts are easy to tell apart. Rebuild with `node brand/avatars/make.mjs`.
- **Accounts progress (Fri night):** project Gmail created. **YouTube: 2 of 4 channels made (Psychology, World History).** Google asked for a video verification before more channels could be added. Ark submitted it Fri 10/23 (reply expected in ~24 h), then makes Anime & Webtoons and Movies & TV. Handles used: not recorded yet.
- Not blocked: Saturday's scripting and filming can cover all 4 topics, since videos don't need the channels to exist yet.

## 2026-10-23 — Session 3 (Fri night, ET, local session on the Mac)

**What we did**
- Recorded the handles and the account map in `CLAUDE.md`: `ark.psych.archive` (YouTube + TikTok) and `ark.history.archive` (YouTube + TikTok).
- **TikTok rejected the Gmail `+` alias.** Ark used a second email for the history TikTok. The anime and film accounts will each need their own email too.
- Ark asked about other platforms. Recommendation: **YouTube + TikTok + Reels only** for the test. Facebook Reels (via Instagram auto-share) and Snapchat Spotlight are parked until a winning channel is picked (`ideas.md`).

**What worked**
- Making accounts in small pieces kept the session moving even while Google's verification was pending.

- **Instagram made for psych + history**, both under taiwanesebeefudon@gmail.com (Instagram lets one email hold several accounts).

**Next step**
- Saturday: script the first 6 Shorts with Claude, then film them. When Google's verification clears, make the anime + film channels (each TikTok needs its own email).

## 2026-10-23 — Session 4 (Fri, ET, local session on the Mac)

**What we did**
- Wrote **Round 1 scripts for Psychology (P01–P05) and World History (H01–H05)** in `scripts/`, one file per Short: hook, 3 beats, ending, filming notes, sources.
  - Psych mixes Ark's health psych notes (Lectures 6–8) with pop culture: *Inside Out* (matching hypothesis), *Cast Away* (loneliness), *The Bear* (Type A/hostility), the houseplant study (control), bad-grade explanatory style.
  - History: Great Emu War, Napoleon's height, Dancing Plague of 1518, Boston Molasses Flood, Cleopatra/Moon landing timeline.
- Round 2 backlog (5 ideas per channel) is in `scripts/README.md`.

**What worked**
- Using Ark's own lecture notes as the source keeps the psych facts checkable and gives every Short a citation.

**Next step**
- Read each script out loud once, then film all 10 in one sitting (same spot, same light). Anime + Movies/TV scripts once those channels' handles are picked.
- **Web-checked the 5 history scripts.** Everything held up except three lines, now fixed: H01's Meredith quote (now uses the commonly cited wording), H01's ending (the emu bounty scheme already existed in 1923 and continued, so it wasn't new), and H04's law line (the engineer sign-off rules started in Boston, not as a Massachusetts law).
