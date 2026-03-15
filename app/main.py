from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from concurrent.futures import ThreadPoolExecutor

# Services
from app.services.prompt_engineer import generate_prompt
from app.services.image_generator import generate_image
from app.services.storyboard_planner import plan_storyboard

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

MAX_PANELS = 6


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/generate")
def generate_storyboard(
    request: Request,
    text: str = Form(...),
    style: str = Form(...)
):

    # Step 1 — Generate storyboard scenes
    scenes = plan_storyboard(text)

    # Safety fallback
    if not scenes or not isinstance(scenes, list):
        scenes = [text]

    scenes = scenes[:MAX_PANELS]

    # Step 2 — Convert scenes to prompts
    prompts = []

    for scene in scenes:

        prompt = generate_prompt(scene, style)

        if not prompt:
            prompt = scene

        prompts.append(prompt)

    # Step 3 — Generate images in parallel
    def safe_generate(prompt):
        try:
            return generate_image(prompt)
        except:
            return "/static/images/fallback.png"

    with ThreadPoolExecutor() as executor:
        images = list(executor.map(safe_generate, prompts))

    # Step 4 — Build storyboard
    storyboard = []

    for i in range(min(len(scenes), len(images))):

        storyboard.append({
            "caption": scenes[i],
            "image": images[i]
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "storyboard": storyboard
        }
    )