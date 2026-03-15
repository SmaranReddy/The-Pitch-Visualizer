# AI Pitch Visualizer

AI Pitch Visualizer is a web application that converts **textual narratives or startup pitches into cinematic storyboard panels using AI**.

The system analyzes a narrative, extracts visual scenes, generates optimized prompts, and produces AI-generated images for each scene. The final output is displayed as a **multi-panel storyboard**, allowing users to visually explore their ideas.

This project demonstrates how **large language models and generative image models can be combined to transform stories into visual sequences**.

---

# Repository

GitHub Repository:

https://github.com/SmaranReddy/The-Pitch-Visualizer

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

## Export Storyboard
The application includes a **Download as PDF** feature that allows users to export the generated storyboard as a single PDF document.

The PDF contains:

- All storyboard panels
- Scene captions
- Ordered narrative visualization

This makes the tool useful for:

- Startup pitch presentations
- Storyboarding for films or animations
- Visual storytelling documentation

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

FastAPI

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
Used as a **fallback image provider** if the primary provider fails.

---

# Installation

## 1 Clone the Repository

```bash
git clone https://github.com/SmaranReddy/The-Pitch-Visualizer.git
cd The-Pitch-Visualizer
```

---

## 2 Create Virtual Environment

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

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```
GEMINI_API_KEY=''
HUGGINGFACE_API_TOKEN=''
POLLINATION_API=''
```

### Gemini API Key
Used for **scene planning and narrative analysis**.

Get an API key from:

https://aistudio.google.com

---

### HuggingFace API Token
Used for **FLUX image generation**.

Create a token at:

https://huggingface.co/settings/tokens

---

### Pollinations API
Used as a **fallback image generation provider** if the primary FLUX provider fails.

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open the application in your browser:

```
http://127.0.0.1:8000
```

---

# Example Input

```
A massive spaceship slowly descends onto a distant alien planet.
Astronauts step out wearing futuristic suits and explore the glowing landscape.
Strange floating creatures drift through the air around them.
Suddenly a colossal alien structure rises from beneath the planet’s surface.
```

### Generated Storyboard Panels

The system converts the narrative into scenes such as:

1. Massive spaceship descending onto an alien planet  
2. Astronauts exploring the glowing alien landscape  
3. Strange floating creatures drifting through the air  
4. A colossal alien structure emerging from the planet surface  

Each scene is visualized as an **AI-generated storyboard panel**, forming a visual narrative of the story.

---

# Prompt Engineering Strategy

Image generation models are **highly sensitive to prompt structure**.

The system constructs prompts using the format:

```
character + camera shot + scene description + style + cinematic cues
```

Example prompt:

```
young astronaut, wide shot, exploring glowing alien landscape,
cinematic lighting, storyboard frame
```

### Design Principles

**Short Prompts**

Diffusion models perform better with concise prompts.

**Visual Keywords**

Comma-separated visual descriptors improve model interpretation.

**Consistent Subject**

The main character is included in prompts to maintain visual continuity.

**Cinematic Framing**

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

This ensures that storyboard generation continues **even if the primary provider fails**.

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

### Character Consistency
Diffusion models may generate slightly different character appearances across panels.

### Scene Interpretation
Language models may occasionally generate scenes that lack strong visual cues.

### External API Dependence
Image generation relies on third-party APIs, which may have usage limits.

---

# Future Improvements

Possible extensions for the system include:

- Character identity consistency across panels
- Multi-character scene detection
- Editable scene descriptions
- Storyboard PDF export improvements
- Animated transitions between panels
- Additional artistic styles
- Scene timeline view

---

# Conclusion

AI Pitch Visualizer demonstrates how **language models and generative image models can be integrated to transform textual ideas into visual narratives**.

By combining scene planning, prompt engineering, and image generation, the system provides an automated pipeline for **turning stories into visual storyboards**, opening possibilities for creative storytelling, product visualization, and concept design.