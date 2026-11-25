import os
import argparse
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

import sys
import io

# Force UTF-8 encoding for Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
CLIENT_SECRETS_FILE = 'client_secrets.json'
TOKEN_FILE = 'token.json'

def get_authenticated_service():
    """Handles OAuth authentication and token caching."""
    creds = None
    # The file token.json stores the user's access and refresh tokens
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_FILE):
                print(f"Error: {CLIENT_SECRETS_FILE} nahi mili! Pehle Google Cloud se download karke is folder mein rakhein.")
                exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
            
    return build('youtube', 'v3', credentials=creds)

def upload_video(youtube, args):
    """Uploads the video to YouTube with provided metadata."""
    # Handle Shorts logic
    title = args.title
    description = args.description
    tags = args.tags.split(',') if args.tags else []
    
    if args.is_short:
        if '#Shorts' not in title and '#Shorts' not in description:
            title = f"{title} #Shorts"
        if 'Shorts' not in tags:
            tags.append('Shorts')
        print("📱 Video is set to be uploaded as a Short (#Shorts added).")

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': args.category,
            'defaultLanguage': args.language,
        },
        'status': {
            'privacyStatus': args.privacy,
            'selfDeclaredMadeForKids': args.made_for_kids,
            'license': args.license,
            'embeddable': args.embeddable,
            'publicStatsViewable': args.public_stats_viewable,
        },
        'recordingDetails': {
            'recordingDate': args.recording_date or datetime.date.today().isoformat(),
        },
    }

    # Schedule logic (only for private videos)
    if args.privacy == 'private' and args.publish_at:
        body['status']['publishAt'] = args.publish_at

    print(f"🚀 Uploading: {args.file}")
    media = MediaFileUpload(args.file, chunksize=-1, resumable=True)
    
    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploading... {int(status.progress() * 100)}%")

    video_id = response['id']
    print(f"✅ Video upload ho gayi! Video ID: {video_id}")
    print(f"🔗 Link: https://youtu.be/{video_id}")
    
    if args.thumbnail and os.path.exists(args.thumbnail):
        print(f"🖼️ Setting thumbnail: {args.thumbnail}")
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(args.thumbnail)
        ).execute()
        print("✅ Thumbnail set ho gaya!")
        
    return video_id

def main():
    parser = argparse.ArgumentParser(description='YouTube Video Uploader')
    parser.add_argument('--file', required=True, help='Video file ka path')
    parser.add_argument('--title', required=True, help='Video ka title')
    parser.add_argument('--description', default='', help='Video ka description')
    parser.add_argument('--tags', default='', help='Comma-separated tags')
    parser.add_argument('--category', default='22', help='Category ID (20=Gaming, 24=Entertainment)')
    parser.add_argument('--privacy', default='private', choices=['public', 'unlisted', 'private'])
    parser.add_argument('--made-for-kids', action='store_true', help='Bacchon ke liye hai toh flag lagao')
    parser.add_argument('--language', default='hi', help='Language code (hi, en)')
    parser.add_argument('--license', default='youtube', choices=['youtube', 'creativeCommon'])
    parser.add_argument('--embeddable', action='store_true', default=True)
    parser.add_argument('--public-stats-viewable', action='store_true', default=True)
    parser.add_argument('--publish-at', default=None, help='Schedule time (ISO 8601 e.g., 2026-12-01T10:00:00Z)')
    parser.add_argument('--recording-date', default=None, help='Recording date (YYYY-MM-DD)')
    parser.add_argument('--thumbnail', default=None, help='Thumbnail image ka path')
    parser.add_argument('--is-short', action='store_true', help='Short video hai toh flag lagao')

    args = parser.parse_args()
    
    try:
        youtube = get_authenticated_service()
        upload_video(youtube, args)
    except Exception as e:
        print(f"❌ Error aaya: {str(e)}")

if __name__ == '__main__':
    main()
