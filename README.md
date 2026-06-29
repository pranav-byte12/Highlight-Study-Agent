# Highlight - AI Study Agent

An AI-powered study assistant built with Google ADK 2.0 that helps students learn effectively by turning their notes into interactive quizzes.

*What it does

1. **Accepts study notes** - paste any notes directly into the chat
2. **Summarizes key topics** - extracts the most important concepts
3. **Generates 5 practice questions** - based on your actual notes
4. **Interactive quiz** - asks one question at a time
5. **Tracks your score** - tells you if you're right or wrong with explanations
6. **Recommends review topics** - tells you what to study more based on your performance

*Security Features

- **Prompt injection detection** - blocks attempts to manipulate the agent
- **Input validation** - ensures the input is genuine study notes

*Tech Stack

- Google ADK 2.0
- Gemini 3.1 Flash Lite
- Google Antigravity IDE
- Python 3.12

*How to run locally

1. Clone this repo
2. Create a `.env` file with your Gemini API key: GEMINI_API_KEY=your_key_here
3. Install dependencies: uv sync
4. Run the playground: uv run adk web . --host 127.0.0.1 --port 8080
5. Open http://127.0.0.1:8080/dev-ui/ and select app
6. Paste your study notes
