import os
import uuid
import requests
import urllib.parse
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

IMAGE_DIR = "static/images"
os.makedirs(IMAGE_DIR, exist_ok=True)

client = InferenceClient(
    provider="nscale",
    api_key=HF_TOKEN
)


def save_pil_image(image):

    filename = f"{IMAGE_DIR}/{uuid.uuid4()}.png"

    image.save(filename)

    return filename


def save_image_bytes(image_bytes):

    filename = f"{IMAGE_DIR}/{uuid.uuid4()}.png"

    with open(filename, "wb") as f:
        f.write(image_bytes)

    return filename


def generate_with_hf_flux(prompt):

    print("HF FLUX generating:", prompt[:80])

    image = client.text_to_image(
        prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    return save_pil_image(image)


def generate_with_pollinations(prompt):

    print("Pollinations fallback:", prompt[:80])

    encoded_prompt = urllib.parse.quote(prompt)

    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=768&seed=random"

    response = requests.get(url, timeout=120)

    if response.status_code != 200:
        raise Exception("Pollinations generation failed")

    return save_image_bytes(response.content)


def generate_image(prompt):

    try:

        return generate_with_hf_flux(prompt)

    except Exception as e:

        print("HF FLUX failed:", e)

        try:

            return generate_with_pollinations(prompt)

        except Exception as e:

            print("Pollinations failed:", e)

            raise Exception("All image providers failed")