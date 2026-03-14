import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")


def segment_text(text: str, max_scenes: int = 5):
    
    sentences = sent_tokenize(text)

    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= max_scenes:
        return sentences

    chunk_size = len(sentences) // max_scenes
    scenes = []

    for i in range(0, len(sentences), chunk_size):
        chunk = " ".join(sentences[i:i+chunk_size])
        scenes.append(chunk)

    return scenes[:max_scenes]