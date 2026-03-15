# AI Pitch Visualizer

AI Pitch Visualizer is a web application that converts **textual narratives or startup pitches into cinematic storyboard panels using AI**.

The system analyzes a narrative, extracts visual scenes, generates optimized prompts, and produces AI-generated images for each scene. The final output is displayed as a **multi-panel storyboard**, allowing users to visually explore their ideas.

This project demonstrates how **large language models and generative image models can be combined to transform stories into visual sequences**.

---

# Key Features

## Narrative to Storyboard Generation
Users input a short narrative or pitch. The system automatically converts it into a sequence of visual scenes.

## AI Scene Planning
A language model analyzes the narrative and extracts **3–5 visual scenes** representing the story progression.

## Prompt Engineering Pipeline
Each scene description is transformed into a **structured prompt optimized for diffusion-based image generation models**.

## AI Image Generation
Each prompt is sent to an image generation model that produces **storyboard-style images**.

## Multi-Panel Storyboard Viewer
Generated images are displayed as a **visual storyboard with panel navigation**.

## Cinematic Style Options
Users can choose different artistic styles:

- Cinematic
- Watercolor
- Sketch
- Anime

## Interactive Storyboard Viewing
The storyboard viewer supports:

- Previous / Next navigation
- Keyboard arrow navigation
- Automatic slideshow playback

---

# System Architecture

The system follows a **modular AI pipeline**.

```
User Narrative
      │
      ▼
Scene Planner (LLM)
      │
      ▼
Scene Descriptions
      │
      ▼
Prompt Engineering
      │
      ▼
Image Generation
      │
      ▼
Storyboard Viewer
```

Each component performs a specific role, making the system **modular and extensible**.

---

# Project Structure

```
app/
│
├── main.py
│
├── services/
│   ├── storyboard_planner.py
│   ├── prompt_engineer.py
│   ├── image_generator.py
│   └── segmenter.py
│
templates/
│   └── index.html
│
static/
│   └── images/
│
.env
requirements.txt
README.md
```

---

# Technology Stack

## Backend
**FastAPI**

A lightweight Python framework used to handle API requests and orchestrate the AI pipeline.

---

## Frontend

- HTML
- CSS
- Jinja Templates

Used for rendering the storyboard interface and user input form.

---

## AI Models

### Gemini 1.5 Flash
Used for **narrative analysis and scene extraction**.

### FLUX Image Generation
Used to **generate visual images from prompts**.

### Pollinations AI
A **fallback provider** used if the primary image generation provider fails.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-pitch-visualizer.git
cd ai-pitch-visualizer
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Mac / Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# API Configuration

Create a `.env` file in the root directory.

Example:

```
GEMINI_API_KEY=your_gemini_api_key
HUGGINGFACE_API_TOKEN=your_huggingface_token
```

---

## Gemini API

Used for **scene planning**.

Get an API key from:

https://aistudio.google.com

---

## HuggingFace Token

Used for **FLUX image generation**.

Generate a token at:

https://huggingface.co/settings/tokens

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open in your browser:

```
http://127.0.0.1:8000
```

---

# Example Input

```
A programmer drinks coffee while coding late at night.
The screen suddenly fills with red error messages.
He looks shocked staring at the laptop.
After debugging, the code finally works and he celebrates.
```

Generated storyboard panels:

1. Programmer drinking coffee while coding  
2. Laptop screen filled with error messages  
3. Programmer shocked staring at screen  
4. Programmer celebrating successful code  

Each scene is visualized using **AI-generated images**.

---

# Prompt Engineering Strategy

Image generation models are **highly sensitive to prompt structure**.

The system constructs prompts using the format:

```
character + camera shot + scene description + style + cinematic cues
```

Example prompt:

```
young programmer, close-up shot, shocked staring at laptop screen,
cinematic lighting, storyboard frame
```

### Design Principles

#### Short Prompts
Diffusion models perform better with concise prompts.

#### Visual Keywords
Comma-separated visual descriptors improve model interpretation.

#### Consistent Subject
The main character is included in prompts to maintain visual continuity.

#### Cinematic Framing
Camera shots such as:

- wide shot
- close-up
- over-the-shoulder

enhance storytelling quality.

---

# Fallback Resilience

External AI APIs can occasionally fail due to:

- rate limits
- provider downtime
- inference errors

To ensure reliability, the system implements **provider fallback logic**.

### Image Generation Strategy

```
Prompt
  │
  ▼
FLUX (Primary Provider)
  │
  ├── Success → return generated image
  │
  └── Failure
        │
        ▼
Pollinations (Fallback Provider)
        │
        ├── Success → return image
        │
        └── Failure → fallback image
```

This ensures that the storyboard generation pipeline continues to function **even if the primary provider fails**.

---

# Design Decisions

## LLM-based Scene Planning
Instead of manually splitting text into sentences, a language model extracts scenes based on **semantic understanding**.

## Modular Pipeline
Each stage of the system is separated into independent services:

- scene planning
- prompt generation
- image generation

This improves **maintainability and extensibility**.

## Parallel Image Generation
Images are generated concurrently using a thread pool to reduce overall latency.

## Lightweight Frontend
The UI is intentionally simple to keep focus on the **AI pipeline**.

---

# Limitations

## Character Consistency
Diffusion models may generate slightly different character appearances across panels.

## Scene Interpretation
Language models may occasionally generate scenes that lack strong visual cues.

## External API Dependence
Image generation relies on third-party APIs, which may have usage limits.

---

# Future Improvements

Possible extensions for the system include:

- Character identity consistency across panels
- Multi-character scene detection
- Editable scene descriptions
- Storyboard PDF export
- Animated transitions between panels
- Additional artistic styles
- Scene timeline view

---

# Conclusion

AI Pitch Visualizer demonstrates how **language models and generative image models can be integrated to transform textual ideas into visual narratives**.

By combining scene planning, prompt engineering, and image generation, the system provides an automated pipeline for **turning stories into visual storyboards**, opening possibilities for creative storytelling, product visualization, and concept design.