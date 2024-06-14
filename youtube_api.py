import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3'

def search_videos(query: str, max_results: int = 5) -> list:
    url = f"{YOUTUBE_API_URL}/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results,
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('items', [])

def get_video_details(video_id: str) -> dict:
    url = f"{YOUTUBE_API_URL}/videos"
    params = {
        'part': 'snippet,contentDetails,statistics',
        'id': video_id,
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('items', [])[0]
