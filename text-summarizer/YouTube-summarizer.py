from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    pattern = r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(url):
    video_id = get_video_id(url)
    if not video_id:
        print("Invalid YouTube URL.")
        return

    try:
        transcript = YouTubeTranscriptApi.list_transcripts(video_id)
        # Try to get English transcript if available, else first one
        try:
            t = transcript.find_transcript(['en', 'en-US', 'auto'])
        except:
            t = next(iter(transcript))
        full_text = " ".join([entry['text'] for entry in t.fetch()])
        print("\n--- Transcript ---\n")
        print(full_text)
    except Exception as e:
        print(f"Error fetching transcript: {e}")

if __name__ == "__main__":
    # youtube_url = input("Enter YouTube URL: ").strip()
    youtube_url = "https://www.youtube.com/watch?v=jaYN-iwgw2g&list=PLhr0Ua8H1x-K7UMXXeSfjULEIBCE1FVd1&index=1&pp=iAQB"
    get_transcript(youtube_url)
