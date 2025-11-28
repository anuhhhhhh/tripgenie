import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

client = OpenAI()

def generate_ai_itinerary(
    destination: str,
    origin: str,
    days: int,
    style: str,
    budget: float,
    activities=None,
) -> str:
    """
    Generate a detailed, natural-language itinerary using OpenAI.
    """
    if activities:
        activities_text = ", ".join(activities)
    else:
        activities_text = "local attractions"

    prompt = f"""
You are a professional travel planner.

Plan a detailed {days}-day trip for a traveler going from {origin} to {destination}.
Trip style: {style}
Total budget: ${budget:,.0f}

Include:
- Morning, afternoon, and evening activities
- Destination-specific details
- Good pacing, no unrealistic scheduling
- Use these activity themes: {activities_text}
- Keep the language warm, fun, and helpful

Return the itinerary in this format:

Day 1: ...
Day 2: ...
Day 3: ...
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are an expert travel planner."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )

    return response.choices[0].message.content.strip()
