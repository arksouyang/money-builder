# Guide 01: Your first Mandarin sermon → English subtitles

**Goal:** a **5-minute subtitled sample clip** you can show churches by Sunday night.
**Where:** on your **Mac**, in Claude Code, with everything stored on your **external SSD**. Not in a cloud session, because cloud sessions can't reach your computer, your SSD, or (reliably) YouTube.
**Your role:** Claude Code does the installing and coding. You make decisions and **review the translation**. Your review is the product.

> Before you start: answer the 3 questions in Step 0 (in chat or in `log.md`). If your Mac is an Intel Mac or the SSD is formatted oddly, a few steps change.

---

## Step 0: Tonight (Thu, ~15 min, no installing)

1. **Pick the sermon.** Choose one your church already posted (YouTube link or audio file) that **you already translated**. Your old translation becomes the answer key for checking quality.
2. **Pick a 5-minute stretch** of it with clear audio, ideally including a Bible quote and a story. Write down the start time (e.g. `12:30`).
3. **Check three things and tell me:**
   - **Mac chip:** Apple menu  → *About This Mac* → does it say **Chip: Apple M1/M2/M3/M4…** or **Processor: Intel**?
   - **Free space on the laptop:** Apple menu  → *System Settings* → *General* → *Storage*.
   - **SSD format and free space:** plug it in → select it in Finder → press **⌘I** → read *Format* (APFS, Mac OS Extended, or exFAT) and *Available*. You'll want **~10 GB free** on it (estimate).
4. **Ask permission (in person Sunday is fine):** "Can I use a clip of Pastor's sermon as a private sample of my subtitle work?" It's their content, so ask.

That's it for tonight. Go to sleep.

---

## Step 1: Friday (~45–60 min): set up on the SSD

1. Plug in the SSD. Open **Terminal** and go to the SSD (replace `MySSD` with its real name):
   ```bash
   cd /Volumes/MySSD
   ```
2. Download the project from GitHub onto the SSD:
   ```bash
   git clone https://github.com/arksouyang/money-builder.git
   cd money-builder
   ```
   If it asks you to log in: run `gh auth login`, or use GitHub Desktop, whichever you use for your other apps.
3. Start Claude Code **inside that folder**:
   ```bash
   claude
   ```
4. Paste this to Claude Code:
   > Read CLAUDE.md and guides/01-first-sermon.md. I'm on Step 1. My Mac has [Apple M_ / Intel], my SSD is [format], mounted at /Volumes/[name]. My laptop has very little free space. Set up the sermon pipeline so that **everything big lives on the SSD**: a Python virtual environment inside this folder (use `--copies` if the SSD is exFAT), and the speech-to-text model cache on the SSD (set HF_HOME to a folder on the SSD). Install only small tools (ffmpeg, yt-dlp) on the laptop itself. Explain each install before you run it and tell me how much space it uses.
5. **Your checks:** Claude Code should tell you what it's installing and where. Approve installs; deny anything that sounds big going to the laptop's internal drive.

What gets installed *(sizes are estimates)*:
| Tool | What it does | Where | Size |
|---|---|---|---|
| ffmpeg | cuts and converts audio/video | laptop (Homebrew) | ~100–300 MB |
| yt-dlp | downloads your church's video audio | laptop or SSD | small |
| Python venv + Whisper (speech-to-text) | turns Mandarin audio into Chinese text with timestamps | **SSD** | ~1–2 GB |
| Whisper model (large-v3-turbo or similar) | the actual "ears" | **SSD** | ~1.5–3 GB |

---

## Step 2: Saturday, part A (~1.5 h): Mandarin audio → Chinese subtitles

Paste to Claude Code:
> Step 2. Download the audio from [YouTube link] into `work/` (work/ is git-ignored, so never commit audio). Cut a 5-minute clip starting at [12:30]. Transcribe it to a Chinese SRT file with timestamps using the Whisper model on the SSD, language Mandarin. Use Traditional Chinese characters [or Simplified, your choice]. Save it as work/clip.zh.srt and show me the first 20 lines.

**Your checks (this is the important part):**
- Open `work/clip.zh.srt` (any text editor) and compare against what you hear.
- Is it **mostly right**? Names, Bible books, and church words are where it usually slips.
- Note every mistake type you see (e.g. "it wrote 聖靈 as 盛靈"). These go into the glossary.

---

## Step 3: Saturday, part B (~1.5 h): Chinese → English subtitles

1. Paste:
   > Step 3. Create `glossary.md` for sermon translation: Bible book names (Chinese Union Version → English), common church terms (神, 主耶穌, 聖靈, 弟兄姊妹, 禱告, 恩典, 福音, 見證, 團契…), and these transcription fixes I found: [your list]. Then translate work/clip.zh.srt into English as work/clip.en.srt. Keep every timestamp, follow the glossary, keep lines under ~42 characters (split into 2 lines if needed), and quote Bible verses from the [ESV/NIV, ask your church which] wording.
2. **Your checks:**
   - Compare it to **your old translation** of the same passage. Is it as good? Where is it worse?
   - Fix the English by hand where needed. Every fix you make is the "human review" you're selling.
   - Add recurring fixes to `glossary.md` so next time is faster.

---

## Step 4: Saturday, part C (~1 h): make the sample video

Paste:
> Step 4. Make work/sample.mp4: the 5-minute clip video with the English subtitles burned in (readable font, bottom center, slight dark background behind the text). Also tell me how a church would upload the .srt file itself to YouTube instead.

**Your check:** watch the full 5 minutes. Would a second-gen kid who only reads English follow the sermon? If yes, you have a product.

Then **time the whole thing on a full sermon** if you have energy left (or Sunday). Track: download, transcribe, translate, *your review time*. Review time is what decides your real hourly rate.

---

## Step 5: Sunday: church + offer
- **At church:** ask your pastor for 2–3 introductions to churches that post Mandarin sermons online. Get permission for the sample. Mention you also do small one-off translation jobs.
- **Afternoon (Claude Code or a cloud session):** write the one-page offer, pricing ($40/sermon, $140/mo for 4, est.), and a list of 15 target churches.
- **End of session:** ask Claude to commit and push, so your notes and scripts are on GitHub.

---

## Rules for this pipeline
- **Never commit audio/video** to GitHub (it's large and it's the church's content). `work/` is git-ignored.
- **Always review.** Raw machine output is not the product.
- Push at the end of every session.
