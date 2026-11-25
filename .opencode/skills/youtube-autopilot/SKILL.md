---
name: youtube-autopilot
description: End-to-end YouTube automation. Takes a topic, researches it, writes a script, generates SEO, finds clips, and publishes. Use when user says "make a video on X" or "run autopilot".
version: 1.0.0
---

# YouTube Autopilot (Orchestrator)

Ye skill ek manager hai. Jab user ek topic de, toh turant kaam shuru karo aur neeche diye gaye steps ko ek-ek karke follow karo.

## Step 1: Research & Idea (yt-viral, yt-script)
- `yt-viral` skill load karo aur us topic par kya chal raha hai, wo research karo.
- `yt-script` skill load karo aur research ke base par ek script likho.

## Step 2: SEO & Packaging (yt-package, yt-seo)
- `yt-package` skill load karo aur title + thumbnail pairing tayar karo.
- `yt-seo` skill load karo aur description + tags generate karo.

## Step 3: Publish (youtube-publish)
- `youtube-publish` skill load karo.
- User se `upload_video.py` ke liye zaroori MCQ poochho (Privacy, Category, Short/Long).
- Clipping aur editing ke baad, jab final video file ready ho, toh `upload_video.py` script run karo aur video upload kar do.

## Important Rule
- Ek step poora hone ke baad hi agle step par jao. 
- Agar user ne sirf publish karne ko bola hai (jaise "ye clip upload kar do"), toh seedha Step 3 par jao aur `youtube-publish` skill use karo.
