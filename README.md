# YouTube Chatbot CLI

## Overview

This project is a command-line interface (CLI) chatbot for YouTube that allows users to search for videos, summarize video content, and answer questions about videos using ChatGPT-3.5 Turbolibrary.

## Features

- **Search YouTube Videos**: Find videos based on user queries.
- **Summarize Videos**: Summarize the content of a YouTube video.
- **Answer Questions**: Answer questions about the content of a YouTube video.

## Requirements

- Python 3.6+
- Pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/rishirishhh/Youtube-Chatbot-CLI.git
   cd Youtube-Chatbot-CLI
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the root directory and add your YouTube API key:

   ```env
   YOUTUBE_API_KEY=your_youtube_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Commands

#### Search for Videos

Search for YouTube videos based on a query.

```bash
python main.py search --query "Machine Learning"
```

#### Summarize a Video

Summarize the content of a YouTube video by its ID.

```bash
python main.py summarize --video_id VIDEO_ID
```

Example:

```bash
python main.py summarize --video_id 5sLYAQS9sWQ
```

#### Ask a Question about a Video

Answer questions about the content of a YouTube video by its ID.

```bash
python main.py ask --video_id VIDEO_ID --question "What is supervised learning?"
```

Example:

```bash
python main.py ask --video_id 5sLYAQS9sWQ --question "What is supervised learning?"
```

## Example Output

### Search

```bash
python main.py search --query "Machine Learning"
```

Output:

```
1. Introduction to Machine Learning (abcd1234)
2. Machine Learning Basics (efgh5678)
3. Advanced Machine Learning Techniques (ijkl9101)
```

### Summarize

```bash
python main.py summarize --video_id 5sLYAQS9sWQ
```

Output:

```
Summary: This is a brief summary of the video content...
```

### Ask a Question

```bash
python main.py ask --video_id 5sLYAQS9sWQ --question "What is supervised learning?"
```

Output:

```
Answer: Supervised learning is a type of machine learning where...
```




