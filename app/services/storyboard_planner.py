import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"


def plan_storyboard(narrative: str):

    prompt = f"""
Convert the following narrative into 4 visual storyboard scenes.

Rules:
- Each scene must be ONE short sentence
- Max 15 words
- Only describe visible actions
- Maintain the same main character
- Return ONLY a numbered list

Example:
1. programmer drinking coffee while coding late night
2. laptop screen fills with red error messages
3. programmer shocked staring at screen
4. code runs successfully and programmer celebrates

Narrative:
{narrative}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()
    except:
        return fallback_split(narrative)

    if "candidates" not in result:
        return fallback_split(narrative)

    text = result["candidates"][0]["content"]["parts"][0]["text"]

    scenes = []

    for line in text.split("\n"):

        line = line.strip()

        match = re.match(r"^\d+[\.\)\-]\s*(.*)", line)

        if match:
            scenes.append(match.group(1).strip())

    if not scenes:
        return fallback_split(narrative)

    return scenes[:6]


def fallback_split(narrative):

    sentences = re.split(r"[.!?]", narrative)

    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences[:6]