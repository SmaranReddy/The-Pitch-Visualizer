import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

STYLE_SUFFIX = """
modern digital illustration, cinematic lighting,
professional storyboard style, consistent characters,
clean composition, high detail
"""


def generate_prompt(scene_text: str, style: str):

    system_prompt = f"""
Convert the following sentence into a detailed visual prompt
for an AI image generator.

Sentence:
{scene_text}

Describe:
- environment
- characters
- actions
- cinematic details

Visual style:
{style}

Return only the prompt.
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": system_prompt}
                ]
            }
        ]
    }

    response = requests.post(API_URL, json=payload)

    result = response.json()

    if "candidates" not in result:
        return f"{scene_text}, {style}"

    return result["candidates"][0]["content"]["parts"][0]["text"]