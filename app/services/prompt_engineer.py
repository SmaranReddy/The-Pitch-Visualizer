import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"


STYLE_MAP = {

    "cinematic": """
cinematic wide shot, dramatic lighting, film still,
35mm lens, depth of field, high dynamic range,
professional cinematography
""",

    "watercolor": """
watercolor painting, soft brush strokes,
hand painted illustration, pastel colors,
artistic watercolor texture
""",

    "sketch": """
storyboard pencil sketch, black and white drawing,
rough hand drawn lines, concept storyboard art
""",

    "anime": """
anime style illustration, vibrant colors,
sharp clean lines, japanese animation aesthetic
"""
}


def generate_prompt(scene_text: str, style: str):

    style_prompt = STYLE_MAP.get(style.lower(), "")

    system_prompt = f"""
You are generating prompts for an AI image generator used to create storyboard scenes.

Rules:
- Stay faithful to the sentence.
- Do NOT invent unrelated characters, locations, or objects.
- Convert the sentence into a clear visual scene.
- Preserve the meaning and context of the sentence.

Sentence:
{scene_text}

Describe visually:
- the environment
- the people or subjects involved
- the main action happening
- camera angle
- lighting

Style:
{style_prompt}

Return ONLY the final visual prompt.
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
        return f"{scene_text}, {style_prompt}"

    prompt = result["candidates"][0]["content"]["parts"][0]["text"]

    grounding_suffix = """
clear subject focus, coherent scene, visually grounded environment
"""

    return f"{prompt}, {grounding_suffix}"