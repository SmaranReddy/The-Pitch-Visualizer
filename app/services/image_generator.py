import requests
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def generate_image(prompt: str):

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Image generation failed: {response.text}")

    # create unique file name
    filename = f"static/images/{uuid.uuid4()}.png"

    # save binary image
    with open(filename, "wb") as f:
        f.write(response.content)

    return filename