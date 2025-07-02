from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load model & processor once at startup
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image, mode: str = "default") -> str:
    """
    Generate a caption for an image using BLIP.
    mode: can be "default", "funny", or "detailed"
    """
    inputs = processor(images=image, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(output[0], skip_special_tokens=True)

    if mode == "funny":
        return f"When you {caption.lower()} but it's Monday 😂"
    elif mode == "detailed":
        return f"This image likely shows: {caption}. It appears to capture fine details and context."
    return caption
