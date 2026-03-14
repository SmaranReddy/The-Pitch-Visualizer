from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.services.segmenter import segment_text
from app.services.prompt_engineer import generate_prompt
from app.services.image_generator import generate_image

from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

# templates
templates = Jinja2Templates(directory="templates")

# static files (generated images)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
async def generate_storyboard(request: Request, text: str = Form(...), style: str = Form(...)):

    scenes = segment_text(text)

    # Step 1: create prompts
    prompts = [generate_prompt(scene, style) for scene in scenes]

    # Step 2: generate images in parallel
    with ThreadPoolExecutor() as executor:
        images = list(executor.map(generate_image, prompts))

    # Step 3: build storyboard
    storyboard = []

    for scene, image in zip(scenes, images):

        storyboard.append({
            "caption": scene,
            "image": image
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "storyboard": storyboard
        }
    )