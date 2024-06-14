import click
from youtube_api import search_videos, get_video_details
from llm_api import summarize_text, answer_question

@click.group()
def cli():
    pass

@cli.command()
@click.option('--query', prompt='Search query', help='Search for YouTube videos.')
def search(query):
    videos = search_videos(query)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['snippet']['title']} ({video['id']['videoId']})")

@cli.command()
@click.option('--video_id', prompt='Video ID', help='Summarize a YouTube video.')
def summarize(video_id):
    video_details = get_video_details(video_id)
    description = video_details['snippet']['description']
    summary = summarize_text(description)
    print(f"Summary: {summary}")

@cli.command()
@click.option('--video_id', prompt='Video ID', help='Answer questions about a YouTube video.')
@click.option('--question', prompt='Your question', help='Ask a question about the video content.')
def ask(video_id, question):
    video_details = get_video_details(video_id)
    description = video_details['snippet']['description']
    answer = answer_question(description, question)
    print(f"Answer: {answer}")

if __name__ == '__main__':
    cli()
