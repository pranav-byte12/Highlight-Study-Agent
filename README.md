# Highlight - AI Study Agent


## Problem
Study tools such as flashcards only allow simple memorization and do not adapt based on student performance. They neither give an explanation of why an answer is wrong nor identify the weak areas for students. It forces students to spend equal amount of time on both things that they have mastered and those that they haven't.


## Solution

Highlight is an Ai study agent which gives personalized feedback to students based on their performance. The users pastes their notes and the agent does the following:

1. Generates the key topics covered in the note
2. Creates 5 practice questions based on the note
3. Quizzes the user on one question at a time
4. Gives an explanation for the correct and incorrect answers
5. Monitors the performance during the whole session
6. Finally, highlights the weak areas of the user and suggests them to review them.

## Architecture

Developed using Google ADK 2.0 and help from an agent powered by Gemini 3.1 FlashLite


**Security Feature:** The `validate_notes` tool checks for prompt injection patterns such as ignore previous instructions, bypass, and jailbreak before the agent processes the input, protecting against manipulation of the agent's behavior.

## How to setup

1. Clone this repo
2. Create a `.env` file with your Gemini API key: GEMINI_API_KEY=your_key_here
3. Install dependencies: uv sync
4. Run the playground: uv run adk web . --host 127.0.0.1 --port 8080
5. Open http://127.0.0.1:8080/dev-ui/ and select app
6. Paste your text
