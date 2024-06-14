import os
from dotenv import load_dotenv

load_dotenv()

def load_api_keys():
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')
    llm_api_key = os.getenv('OPENAI_API_KEY')
    return youtube_api_key, llm_api_key
