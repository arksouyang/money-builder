# Guide 01: Your first Mandarin sermon → English subtitles

> **PARKED (2026-10-22).** The church subtitle service is on hold: Ark doesn't want to cold-message strangers. **Step 1 (setup on the SSD) is still useful.** The same speech-to-text setup makes burned-in captions for Ark's own Shorts. See `guides/02-shorts-test.md`.

**Goal:** a **5-minute subtitled sample** by Saturday night.
**Where:** on your **Mac (M2)**, in a *local* Claude Code session, with everything stored on your **external SSD** (your laptop has only ~12 GB free).
**Your role:** Claude Code installs and codes. You make decisions and **review the translation**. Your review is the product.

### Ground rules
- **Your own church is not involved.** Don't use their sermons for samples, and don't ask them for anything.
- **Don't download from YouTube.** YouTube's terms forbid downloading without permission from YouTube and the rights holders. Get audio from places that *offer* downloads (a church's website, an Apple Podcasts/Spotify RSS feed with MP3s), or from files a church sends you. Paying clients will simply send you their file.
- **Samples stay private.** Show a church only *its own* sermon, never publicly. Delete working audio when you're done.
- **Never commit audio/video to GitHub.** `work/` is git-ignored.

---

## Step 0: Pick a practice sermon (~15 min)
1. Search for **Mandarin church sermon podcasts** or church websites with downloadable sermon MP3s. Search terms: `華人教會 講道 podcast`, `Chinese church sermon podcast Mandarin`, `台灣基督長老教會 講道 mp3`. NJ/NY churches are a bonus, since they become outreach targets.
2. Pick one that (a) offers a **download button or podcast MP3**, (b) has clear audio, and (c) ideally also has a YouTube channel *without* English subtitles. That makes it a future customer.
3. Note the link and a **5-minute stretch** to practice on (e.g. 12:30–17:30). Choose one with a Bible quote in it.

*(Tonight is fine to stop here. Or keep going to Step 1 if you have energy.)*

---

## Step 1: Set up on the SSD (~45–60 min)
1. Plug in the SSD. Open **Terminal** (⌘ + Space → type "Terminal").
2. Find the SSD's name:
   ```bash
   ls /Volumes
   ```
3. Go there and download the project (replace `MySSD`; keep the quotes if the name has spaces):
   ```bash
   cd "/Volumes/MySSD"
   git clone https://github.com/arksouyang/money-builder.git
   cd money-builder
   ```
   If git asks you to log in, run `gh auth login`, or use GitHub Desktop, whichever you use for your other apps.
4. Start Claude Code in that folder:
   ```bash
   claude
   ```
   *(Prefer the Claude desktop app? Open the **Code** tab → choose **Local** → pick the `money-builder` folder on the SSD.)*
5. Type:
   > Start session per CLAUDE.md. Then do guide Step 1: check the SSD's format with diskutil, then set up the sermon pipeline so everything big lives on the SSD: a Python virtual environment in this folder (use --copies if the SSD is exFAT), mlx-whisper for speech-to-text, and the model cache on the SSD (HF_HOME). Install only small tools on the laptop (ffmpeg). My laptop has only ~12 GB free, so tell me the size and location of every install before you run it.
6. **Your job:** approve installs that are small or going to the SSD. Say no to anything big landing on the laptop.

*Expected sizes (estimates):* ffmpeg via Homebrew ~100–300 MB on the laptop; Python environment + mlx-whisper ~1–2 GB on the SSD; Whisper model ~1.5–3 GB on the SSD.

---

## Step 2: Mandarin audio → Chinese subtitles (~1.5 h)
Type:
> Guide Step 2. Download the sermon MP3 from [link] into work/. Cut a 5-minute clip from [12:30]. Transcribe it with mlx-whisper (Mandarin, Traditional characters) to work/clip.zh.srt with timestamps. Show me the first 20 subtitles.

**Your checks:**
- Play the clip and read along. Is it mostly right?
- Note every mistake (names, Bible books, church words, e.g. "wrote 盛靈 instead of 聖靈"). These go into the glossary.

---

## Step 3: Chinese → English subtitles (~1.5 h)
Type:
> Guide Step 3. Create glossary.md: Bible book names (Chinese Union Version → English), common church terms (神, 主耶穌, 聖靈, 弟兄姊妹, 禱告, 恩典, 福音, 見證, 團契…), and these transcription fixes: [your list]. Then translate work/clip.zh.srt to English as work/clip.en.srt. Keep every timestamp, follow the glossary, keep each line under ~42 characters (max 2 lines), and use ESV wording for Bible quotes.

**Your checks (this is the product):**
- Play the audio and read the English. You interpret live every week, so you'll *hear* where it's wrong.
- Fix the English by hand. Add recurring fixes to `glossary.md` so the next sermon is faster.
- Note how long your review took. That number decides your real hourly rate.

---

## Step 4: Make the preview video (~1 h)
Type:
> Guide Step 4. Make work/sample.mp4: a simple 5-minute video with a plain dark background, the church's name at the top, the sermon audio, and the English subtitles burned in (readable, bottom center). Also write work/sample-bilingual.md: Chinese and English side by side for the same 5 minutes. Then tell me how a church uploads an .srt file to its own YouTube video.

**Your check:** watch all 5 minutes. Would an English-only second-gen kid follow the sermon? If yes, you have a product.

---

## Step 5: Sunday afternoon: offer + target list (~2–3 h, cloud or local session)
- One-page offer + pricing ($40/sermon, $140/mo for 4, est.).
- List of 15 Mandarin-speaking churches (not yours) that post sermons online without English subtitles, and whether each offers downloadable audio.
- Draft a short outreach message: "I made a free 5-minute English subtitle sample of your sermon. Want to see it?"
- **End the session with: "commit and push."**
