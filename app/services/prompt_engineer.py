import random

STYLE_MAP = {

    "cinematic": "cinematic lighting, film still, dramatic atmosphere",

    "watercolor": "watercolor painting, soft brush strokes, pastel colors",

    "sketch": "pencil storyboard sketch, black and white line art",

    "anime": "anime style illustration, vibrant colors, japanese animation aesthetic"
}


DEFAULT_CHARACTER = "main character"

SHOT_TYPES = [
    "wide shot",
    "medium shot",
    "close-up shot",
    "over the shoulder shot"
]


STORYBOARD_SUFFIX = "storyboard frame, cinematic composition"


def generate_prompt(scene_text: str, style: str):

    style_prompt = STYLE_MAP.get(style.lower(), "")

    shot = random.choice(SHOT_TYPES)

    prompt = f"{scene_text}, {shot}, {style_prompt}, {STORYBOARD_SUFFIX}"
    return prompt