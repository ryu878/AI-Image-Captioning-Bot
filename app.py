import gradio as gr
from caption import generate_caption

def handle_upload(image, mode):
    if image is None:
        return "Please upload an image."
    return generate_caption(image, mode)

gr.Interface(
    fn=handle_upload,
    inputs=[
        gr.Image(type="pil", label="Upload your image"),
        gr.Radio(["default", "funny", "detailed"], label="Caption Style", value="default")
    ],
    outputs=gr.Textbox(label="AI-Generated Caption"),
    title="🖼️ AI Image Captioning Bot",
    description="Upload an image and get a smart caption powered by BLIP."
).launch()
