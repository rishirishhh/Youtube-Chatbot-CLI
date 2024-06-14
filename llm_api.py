import os
import openai
from dotenv import load_dotenv
from openai.error import RateLimitError
import time

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def summarize_text(text: str, retries: int = 3, delay: int = 5) -> str:
    for attempt in range(retries):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Summarize the following text:\n\n{text}",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except RateLimitError:
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                return "Error: You have exceeded your API rate limit. Please try again later or check your API plan."

def answer_question(text: str, question: str, retries: int = 3, delay: int = 5) -> str:
    for attempt in range(retries):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Based on the following text, answer the question:\n\nText: {text}\n\nQuestion: {question}",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except RateLimitError:
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                return "Error: You have exceeded your API rate limit. Please try again later or check your API plan."
