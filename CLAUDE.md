# Money Builder: read this first every session

## Session-start protocol (do this before anything else)
1. Read `CLAUDE.md` (this file), `GOALS.md`, and the **latest** entry in `log.md`.
2. Check `ledger.csv` for the current balance.
3. Tell Ark where things stand in **2–3 sentences**, then propose **one** next step.
4. At the end of every session, add a dated entry to `log.md` (what we did, what worked, what's next) and update `ledger.csv` / `GOALS.md` if money moved.

## Who Ark is
- 22, psychology major at Rutgers with a full course load. Weekday commitments: assists boss 3:00–5:30 PM daily; coaches table tennis Wed + Fri evenings (sporadic). **Coaching is not part of this project.** Ark keeps it separate, so don't plan around it or count its income.
- **Realistic budget: ~10 hours/week (~2 hrs/day).** Plan for real hours, not ideal ones. Expect less during midterms/finals.
- Skills: builds apps with Claude Code (gym tracker, jadeNote webtoon planner; not published); **live** Mandarin→English sermon interpretation (volunteer, own church only; no written translations on file); writing/webtoon concepts; YouTube (four fresh `.archive` channels, 0 subs).
- **Does not want to interpret in person** for anyone else. Remote, written/subtitle work only.
- Machine: **Mac M2, laptop nearly full (~12 GB free of 245 GB)**. External SSD with ~200–300 GB free (format not yet checked). Anything big goes on the SSD.
- Communities: own church, Taiwanese and other multicultural communities.
- Has: bank account, PayPal, Venmo, Zelle (no Stripe). Works on a PC and a Mac.
- Prefers to stay **anonymous at first** (no face on camera). Fine to deal with clients one-to-one.
- **Real estate is dropped entirely** (license needs renewal, bad relationship with the boss). Don't suggest it.
- Enjoys content creation (dream: YouTuber) and is interested in dropshipping. **Gives up quickly without visible results.** Design for early, visible wins.

## Hard rules
- Start at $0 capital (ledger starts at **−$20**: the Claude Pro subscription).
- No spending until the project has earned it. Reinvest only from profit, and only into a channel that has proven it works.
- No gambling, crypto/stock trading, get-rich-quick, MLMs, or borrowing money for the project.
- Show Ark **only the next milestone**, not the whole mountain. Keep the active target small.
- Ark's Tier 1 subscriptions are non-negotiable. Don't suggest cutting them.

## Working rules for Claude
- Be direct and honest, including about bad ideas or unrealistic expectations. No flattery.
- **Verify platform facts (thresholds, fees, policies) with a web search before stating them**, cite sources, and label estimates as estimates.
- Ask Ark when information is missing; don't guess.
- Celebrate wins briefly, then point at the next milestone.
- When a milestone is hit: update `GOALS.md` (mark done, move the ACTIVE marker), then suggest the next target.
- Keep plans sized to ~10 hrs/week and in 60–120 min blocks.

## Current strategy (set 2026-10-23, see `ideas.md` for full reasoning)
- **PRIMARY (only active path): Bilingual sermon subtitles.** Chinese→English subtitle files (SRT) and translated transcripts for Chinese-language churches that post sermons online. Ark builds a Claude Code pipeline (speech-to-text → Claude translation with a theology glossary → human review → SRT). Full ~10 hrs/week.
- **Ark's own church is completely out of this business:** no payment, no referrals, no asking them for anything. Sell to *other* churches through direct outreach. The sales sample is 5 minutes of **the target church's own public sermon**, subtitled and shared privately with that church only. Practice runs can use any public sermon but stay private.
- **SECONDARY: none for now** (decided 2026-10-23, after Ark took coaching out of the project). Revisit once Tier 0 is hit. YouTube is the leading candidate.
- **Tier 0 fallback (stays inside the primary path):** if no church has paid by day 7, widen the offer to one-off Chinese→English jobs (letters, flyers, event materials, menus, video subtitles) via a Fiverr gig and/or community contacts *outside* Ark's church (ask Ark which contacts are OK). Not certified legal/immigration documents.
- **PARKED: YouTube** (unlock: Tier 1 covered 2 months in a row), **dropshipping** (unlock: a profit-funded, capped test budget), **clothing brand** (only as merch for an audience that already exists).

## Urgent, off-ledger: Fall tuition registration hold
- The fall hold is **$3,800.48** (confirmed by Ark 2026-10-23; higher than the ~$3,000 first estimate). It blocks Spring 2027 registration. The unpaid summer balance ($2,000) is **not** part of the hold. Ark's registration slot is **Mon Nov 9, 2026, 9:00 AM** (confirmed in WebReg).
- Ark already has a backup course schedule and prefers to keep it private. Don't ask for it.
- From past calls, Ark knows **partial payment does not lift the hold**: the full $3,800.48 must clear. Ark can register up to **~1 week late (~Nov 16)** if necessary, but would prefer not to.
- $3,800.48 is what's left **after all aid**. Ark has no grants or emergency-fund money; a low GPA affects aid. Ark's parents would cover it, but it would be a heavy burden for them. Don't re-suggest Rutgers grants or emergency funds.
- **Protect study time.** GPA affects aid eligibility, so it is worth real money. Never plan project work over exams or classes.
- Ark's dad is paying Spring 2027 tuition.
- The side hustle **cannot** produce $3,800 by Nov 9. This is handled through Rutgers offices and family, not project milestones. Track progress in `log.md`.

## Known debt details
- Credit card: ~$1,000 balance. 0% intro ends **~early March 2027 (Ark's estimate, unconfirmed)**. Post-intro APR unknown. Pay at least the minimum every month.
- Friend $2,000 / sister $7,000: no deadline, no strain. Ark wants them paid within ~6 months; that's not realistic at 10 hrs/week (see GOALS.md).

## Open questions to ask Ark
- Which Rutgers campus/school? (Assumed New Brunswick.)
- Credit card: exact 0% end date and post-intro APR (printed on the statement or in the card app).
- SSD format (local Claude Code can check with `diskutil info`).
- Which community contacts *outside* Ark's church are OK to approach (Taiwanese orgs, friends, family friends)?

## Repo, sessions, and where work happens
- Source of truth: private GitHub repo `arksouyang/money-builder` (branch `main`). **Commit and push at the end of every session.** Cloud containers are wiped after inactivity, and anything not pushed is lost.
- **Cloud session** (claude.ai/code or the Claude app → new session → repo `arksouyang/money-builder`): planning, check-ins, writing, outreach drafts. Can't touch Ark's computer or SSD.
- **Local session** (Mac Terminal: `cd /Volumes/<SSD>/money-builder && claude`): the sermon pipeline (downloads, speech-to-text, video). Ark's laptop is low on space, so **everything big goes on the external SSD**: repo, Python venv, model cache (HF_HOME), audio in `work/`.
- To start any session, Ark types: **"Start session per CLAUDE.md."**
- Step-by-step pipeline walkthrough: `guides/01-first-sermon.md`.
- **Time zone:** Ark is in New Jersey (US Eastern). Cloud containers run on UTC, so convert before writing dates in logs and the ledger.

## File conventions
- `ledger.csv`: **project money only.** Columns: `date,source,description,income,expense,running_balance`. Dates as YYYY-MM-DD. `running_balance` = previous balance + income − expense. When project profit pays a debt, log it as an expense with source `Debt: <name>`.
- `ideas.md`: every idea with status `active` / `parked` / `rejected` and the reason.
- `log.md`: newest entry at the bottom, headed `## YYYY-MM-DD — Session N`.
- `GOALS.md`: one milestone marked **ACTIVE** with a text progress bar.
