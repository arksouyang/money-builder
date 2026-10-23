# Money Builder: read this first every session

## Session-start protocol (do this before anything else)
1. Read `CLAUDE.md` (this file), `GOALS.md`, and the **latest** entry in `log.md`.
2. Check `ledger.csv` (money) and `content-tracker.csv` (videos posted + performance).
3. Tell Ark where things stand in **2–3 sentences**, then propose **one** next step.
4. At the end of every session: add a dated entry to `log.md` (what we did, what worked, what's next), update `ledger.csv` / `content-tracker.csv` / `GOALS.md` if anything moved, then **commit and push**.

## Who Ark is
- 22, psychology major at Rutgers with a full course load. Weekday commitments: assists boss 3:00–5:30 PM daily; coaches table tennis Wed + Fri evenings (sporadic). **Coaching is not part of this project.** Don't plan around it or count its income.
- **Realistic budget: ~10 hours/week (~2 hrs/day).** Plan for real hours, not ideal ones. Expect much less during midterms/finals (Rutgers fall finals are mid-December).
- Skills: builds apps with Claude Code (gym tracker, jadeNote webtoon planner; not published); **live** Mandarin→English sermon interpretation (volunteer, own church only); writing/webtoon concepts; has run YouTube channels before (old logins lost).
- **Owns four fresh YouTube channels** under a `.archive` naming convention (0 subs).
- **On camera: Ark is OK using face and voice** for YouTube (changed 2026-10-22; earlier preference was anonymous).
- Has: bank account, PayPal, Venmo, Zelle (no Stripe).
- Machine: **Mac M2, laptop nearly full (~12 GB free of 245 GB)**. External SSD with ~200–300 GB free (format not yet checked). **Anything big (footage, project files, models) goes on the SSD.**
- **Does not want to cold-message strangers** (the subtitle outreach plan felt bad for this reason). Don't build plans that depend on it.
- **Ark's own church is not part of this project in any way.** No in-person interpreting for anyone.
- **Real estate is dropped entirely**, as a business and as a content topic.
- Content creation is the dream. Also interested in dropshipping. **Gives up quickly without visible results.** Design for early, visible wins: views and videos shipped count as results.

## Hard rules
- Start at $0 capital. **Ark self-funds Claude Pro ($20/mo) for now** (decided 2026-10-22). The project will take it over once content earns.
- No project spending (mic, lights, software, ads) until the project has earned it. Reinvest only from profit, and only into a channel that has proven it works.
- No gambling, crypto/stock trading, get-rich-quick, MLMs, or borrowing money for the project.
- Show Ark **only the next milestone**, not the whole mountain. Keep the active target small.
- Ark's Tier 1 subscriptions are non-negotiable. Don't suggest cutting them.

## Working rules for Claude
- Be direct and honest, including about bad ideas or unrealistic expectations. No flattery.
- **Verify platform facts (thresholds, fees, policies) with a web search before stating them**, cite sources, and label estimates as estimates.
- Ask Ark when information is missing; don't guess.
- Celebrate wins briefly, then point at the next milestone.
- When a milestone is hit: update `GOALS.md` (mark done, move the ACTIVE marker), then suggest the next target.
- Keep plans sized to ~10 hrs/week and in 60–120 min blocks. Batch work (script several, film several, edit several).

## Current strategy (set 2026-10-22, see `ideas.md` and `guides/02-shorts-test.md`)
- **PRIMARY: Shorts test across 4 YouTube channels**, cross-posted to TikTok and Instagram Reels. Face + voice. Topics (mapping to confirm with Ark):
  1. Psychology
  2. World History
  3. Anime & Webtoons
  4. Movies & TV
- **Test design:** Round 1 = 5 Shorts per channel (20 total). Round 2 = 10 per channel (40 total). Then **reassess with the numbers in `content-tracker.csv`**. The winning topic(s) move to longform; losers pause.
- **Copyright:** for anime/webtoon/movie/TV topics, talk to camera with little or no copyrighted footage. YouTube allows reused content only with meaningful transformation, and copyright still applies.
- **SECONDARY: none.** Ark chose to self-fund instead of a cash side-path.
- **PARKED:** church subtitle service (cold outreach felt bad; the speech-to-text pipeline is reused for **auto-captions on Ark's own Shorts**), Fiverr subtitle gig, dropshipping (path: TikTok Shop affiliate once an account reaches 1,000 followers; own store only from profit), clothing brand (merch for an audience later).

## Money reality (verified 2026-10-22, re-check before quoting)
- YouTube ad revenue for channels applying from Feb 1, 2027: 1,000 subs + 8,000 watch hours/12 mo or 20M Shorts views/90 days.
- TikTok Creator Rewards: ~10,000 followers + 100,000 views/30 days, videos >1 min (third-party sources).
- Instagram Reels: no regular US per-view pay; bonuses are invite-only.
- So the first platform dollar is **months away**. Track views and followers as the progress signal.

## Off-ledger context: tuition
- Fall hold **$3,800.48** (after all aid; no grants or emergency funds; low GPA affects aid). Partial payment doesn't lift it. Registration slot Mon Nov 9, 9:00 AM; Ark can register ~1 week late. Ark's parents would cover it at real cost to them. Dad pays spring. Don't re-suggest Rutgers grants or emergency funds.
- **Protect study time.** GPA affects aid eligibility, so it's worth real money. Never plan project work over exams.

## Known debt details
- Credit card: ~$1,000. 0% intro ends ~early March 2027 (unconfirmed). Pay at least the minimum monthly.
- Summer tuition $2,000 (no hold). Friend $2,000 / sister $7,000: no deadline.

## Accounts and tools (confirmed 2026-10-22)
- Ark will make **new `.archive` YouTube channels** for the 4 topics. All 4 can live under one Google account (Brand Accounts).
- **New TikTok + Instagram accounts** matching each channel name. **Never Ark's personal accounts.** Each needs its own email or phone number.
- Editing: **CapCut Pro on the Mac** (Ark's own subscription). CapCut has no official automation API (third-party draft-file tools are fragile and don't export on macOS), so Claude doesn't edit inside CapCut. Proposed split: a Claude Code **rough-cut tool** (silence removal, loudness, 9:16 framing, title ideas) → Ark polishes in CapCut (captions, hook text, music). Point CapCut's project/cache folders at the SSD.

## Open questions to ask Ark
- Confirm the 4-channel topic mapping and the exact `.archive` names.
- Build the rough-cut tool? (offered 2026-10-22)
- SSD format (local Claude Code can check with `diskutil info`).
- Credit card exact 0% end date + post-intro APR.

## Repo, sessions, and where work happens
- Source of truth: private GitHub repo `arksouyang/money-builder` (branch `main`). **Commit and push at the end of every session.** Cloud containers are wiped after inactivity.
- **Cloud session** (claude.ai/code or the Claude app → new session → repo `arksouyang/money-builder`): planning, scripts, ideas, reviewing numbers. Can't touch Ark's computer or SSD.
- **Local session** (Mac Terminal: `cd "/Volumes/<SSD>/money-builder" && claude`): anything with video/audio files, e.g. auto-captions. Footage lives on the SSD in `work/` (git-ignored). **Never commit video/audio.**
- To start any session, Ark types: **"Start session per CLAUDE.md."**
- **Time zone:** Ark is in New Jersey (US Eastern). Cloud containers run on UTC, so convert before writing dates.

## File conventions
- `ledger.csv`: **project money only.** Columns: `date,source,description,income,expense,running_balance`. `running_balance` = previous + income − expense. Claude Pro is self-funded for now and not logged as a monthly project expense.
- `content-tracker.csv`: one row per Short. Fill the 7-day numbers one week after posting.
- `ideas.md`: every idea with status `active` / `parked` / `rejected` and the reason.
- `log.md`: newest entry at the bottom, headed `## YYYY-MM-DD — Session N`.
- `GOALS.md`: one milestone marked **ACTIVE** with a text progress bar.
