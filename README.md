# AI Image Captioning Bot

### Tech: Python, BLIP2 or GPT-4V, Gradio, Hugging Face
### Description: Upload any image and get a detailed, human-like caption. Add optional meme/Instagram-style generation.

```
📦 AI-Image-Captioning-Bot/
├── app.py                # Main Gradio app
├── caption.py            # Caption generation logic
├── requirements.txt      # Dependencies
└── README.md             # This file
```

### 🔧 Features
- 🔍 BLIP-2 transformer-based image captioning

- ⚡ Fast local inference via HuggingFace

- 🖥️ Web UI powered by Gradio

- 🧠 Optionally generate fun/meme-style or professional captions

### 🧠 Models Used
- Salesforce/BLIP2

- transformers

- gradio

You can easily switch to other Hugging Face models if needed.

### 📦 Installation
### 1. Clone the repo and cd into it
```
git clone https://github.com/ryu878/AI-Image-Captioning-Bot.git
cd AI-Image-Captioning-Bot
```
### 2. Set up and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Run the app
```
python app.py
```
### 5. ToDo
- Add Docker support

- Add batch captioning for multiple images

- Use GitHub Actions to auto-deploy the app (e.g., to Hugging Face Spaces or Fly.io)

## Contacts
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf
