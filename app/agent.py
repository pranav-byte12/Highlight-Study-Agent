# Highlight - AI Study Agent
# Built with Google ADK 2.0 for the Kaggle 5-Day AI Agents Course
# This agent transforms study notes into personalized interactive quizzes

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini

# Security tool: validates input before the agent processes it
# Blocks prompt injection attacks and ensures input is genuine study notes
def validate_notes(text: str) -> str:
    """Validates that input is genuine study notes, not a prompt injection attempt.
    Args:
        text: The input text to validate
    Returns:
        'valid' if notes are genuine, 'invalid' if suspicious
    """
    # List of common prompt injection patterns to detect
    injection_patterns = [
        "ignore previous", "ignore all", "bypass", "forget your instructions",
        "you are now", "act as", "jailbreak", "override"
    ]
    
    text_lower = text.lower()
    
    # Check for injection patterns
    for pattern in injection_patterns:
        if pattern in text_lower:
            return "invalid"
    
    # Reject input that is too short to be real study notes
    if len(text.strip()) < 50:
        return "invalid"
    
    return "valid"

# Main ADK agent definition
# Uses Gemini 3.1 Flash Lite
root_agent = Agent(
    name="Highlight",
    model=Gemini(model="gemini-3.1-flash-lite"),
    # Agent instruction defines the study workflow behavior
    instruction="""You are Highlight, an AI Study Agent.

When a student gives you their study notes:
1. First call validate_notes to check the input is genuine
2. If invalid, politely refuse and ask for real study notes
3. If valid, summarize the key topics in 3-5 bullet points
4. Generate exactly 5 practice questions based on the notes
5. Ask one question at a time and wait for the answer
6. Tell them if they were right or wrong and explain why
7. Track their score throughout (e.g. Score: 2/3)
8. At the end give their final score and recommend which topics to review

Always be encouraging and supportive!""",
    # validate_notes is registered as a tool the agent can call
    tools=[validate_notes],
)

# ADK App wraps the agent for the playground and deployment
app = App(
    root_agent=root_agent,
    name="app",
)
