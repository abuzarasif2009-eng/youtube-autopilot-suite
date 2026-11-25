# 🚀 YouTube Autopilot Suite (AI Agent Skill)

An end-to-end AI agent skill for YouTube research, SEO, and fully automated uploading (Shorts & Long Videos). This works with OpenCode, Hermes, or any AI agent that can read Markdown and run Python scripts.

## ✨ Features
- **Auto Upload:** Directly uploads videos via YouTube Data API v3.
- **Shorts Support:** Auto-detects and adds `#Shorts` to titles/tags.
- **Advanced Settings:** Full control over privacy, category, tags, and scheduling.
- **Modular Skills:** Includes 11 sub-skills for research, scripting, SEO, and packaging, managed by `youtube-autopilot`.

## ⚠️ Security Notice
This repository **does NOT** contain any API keys or secrets. The `.gitignore` is configured to prevent `client_secrets.json` and `token.json` from ever being uploaded. You must generate your own keys.

---

## 🛠️ Step-by-Step Setup Guide

### Step 1: Google Cloud Console Setup (One-time)
1. Go to [Google Cloud Console](https://console.cloud.google.com/) and login with the Gmail account linked to your YouTube channel.
2. Create a **New Project** (e.g., `My YouTube Uploader`).
3. Go to **APIs & Services > Library**, search for `YouTube Data API v3` and click **Enable**.
4. Go to **APIs & Services > OAuth consent screen**:
   - Choose **External** and click Create.
   - Fill App Name and Emails. Save and Continue.
   - In Scopes, add `.../auth/youtube.upload`. Save and Continue.
   - In **Test Users**, add your own Gmail address. Save and Continue.
5. Go to **APIs & Services > Credentials**:
   - Click **+ CREATE CREDENTIALS > OAuth client ID**.
   - Application type: **Desktop app**. Name it anything. Click Create.
   - Click **Download JSON**.
6. Rename the downloaded file to exactly **`client_secrets.json`** and place it in the root folder of this project.

### Step 2: Local Installation
1. Clone this repository:
   `git clone https://github.com/abuzarasif2009-eng/youtube-autopilot-suite.git`
2. Go to the folder:
   `cd youtube-autopilot-suite`
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it:
   - Windows: `.\venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
   `pip install -r requirements.txt`

### Step 3: Using with AI Agents
- **For OpenCode:** Move the `.opencode/skills` folder to your OpenCode skills directory. The agent will automatically pick up `youtube-autopilot`.
- **For Hermes/Other Agents:** Copy the folders inside `.opencode/skills/` (like `youtube-publish`, `youtube-autopilot`) into your agent's custom skills directory (e.g., `~/.hermes/skills/`).

### Step 4: First Run (Authentication)
Before asking your agent to upload, run this manually in your terminal to authorize Google:
`python upload_video.py --file "test.mp4" --title "Test" --privacy private`
(A browser will open. Login and allow access. This creates `token.json` so you never have to login again).

---

## 🤖 How to use the Agent
Once setup, just tell your agent:
> *"Run autopilot and make a video on GTA 6 hidden details, then upload it as a Short."*

The agent will use `yt-viral` for research, `yt-script` for writing, `yt-seo` for tags, and finally `youtube-publish` to upload it directly to your channel!
