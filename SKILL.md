---
name: youtube-publish
description: Use when a clip is ready and the user says "publish", "upload", "YouTube par daalo", or "short upload karo". Asks MCQ questions in chat for privacy, category, video type (short/long), title, tags, thumbnail, and schedule, then runs upload_video.py with full advanced settings.
version: 1.0.0
platforms: [windows, macos, linux]
metadata:
  tags: [youtube, publish, upload, shorts, clipping]
  category: content
---

# YouTube Publish Skill

## Overview
Ye skill ready clip ko YouTube Data API v3 se publish karti hai. Full advanced settings supported hain: privacy, category, made-for-kids, tags, language, license, schedule, recording date, custom thumbnail, aur Shorts/Long video ka logic.

## When to Use
- User bole: "publish karo", "upload karo", "YouTube par daalo", "short upload karo"
- Clipping skill clip ready kar chuki ho.

## Important Rules
- NEVER try to read or open `client_secrets.json` or `token.json`.
- Always ask MCQs one by one. Do not ask all at once.

## Step 1 — MCQ poochho (ek waqt par sirf ek question)

### Q1. Video Type
"Ye video Shorts hai ya Long video?"
A) Short (60 sec se kam / Vertical)
B) Long video

### Q2. Privacy
"Video ki privacy kya rakhu?"
A) Public
B) Unlisted
C) Private
D) Schedule (private + future date/time)

### Q3. Category
"Category kya hai?"
A) Gaming (20)
B) Entertainment (24)
C) People & Blogs (22)
D) Education (27)
E) Science & Technology (28)

### Q4. Title
"Maine ye title suggest kiya hai: `<clip_title>`. Ye rakhu ya aap khud likhoge?"
A) Ye rakho
B) Main khud likhta hoon

### Q5. Tags
"Maine ye tags suggest kiye hain: `<tags>`. Ye rakhu ya aap khud doge?"
A) Ye rakho
B) Main khud likhta hoon

### Q6. Thumbnail
"Thumbnail ka kya karna hai?"
A) Auto-generated
B) Main file path dunga

## Step 2 — Script chalao

Jab saare answers mil jayein, to skill folder mein ye command chalao:

.\venv\Scripts\python.exe upload_video.py --file "CLIP_PATH" --title "FINAL_TITLE" --description "DESCRIPTION" --tags "tag1,tag2,tag3" --category "20" --privacy "public" --language "hi"

**Logic for arguments:**
- Agar Q1 mein `A) Short` chuna hai, toh command ke end mein `--is-short` flag lagao. Agar `B) Long` chuna hai, toh `--is-short` mat lagao.
- Agar Q2 mein `A) Public` chuna hai, toh `--privacy public` bhejo.
- Agar Q2 mein `D) Schedule` chuna hai, toh user se date/time poochho, `--privacy private` aur `--publish-at "YYYY-MM-DDTHH:MM:SSZ"` dono bhejo.
- Category ID ke liye Q3 ka number use karo (Gaming ke liye 20).
- Agar Q6 mein `B` chuna hai, toh `--thumbnail "path"` bhejo.

## Step 3 — Confirm karo

Script ke output se `video_id` aur link lo, aur user ko bolo:
"✅ Video publish ho gayi — https://youtu.be/<video_id>"
Agar schedule tha: "Video private hai aur <date> ko public hogi."
