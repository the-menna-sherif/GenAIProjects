import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(youtube_url: str) -> str:
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?&]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL")


def get_transcript_from_url(youtube_url: str) -> str:
    video_id = extract_video_id(youtube_url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    # 👇 LEGACY OBJECT ACCESS
    return " ".join(item.text for item in transcript)


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print(get_transcript_from_url(url))
