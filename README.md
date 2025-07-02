# AI Image Captioning Bot

📦 ai-image-captioning-bot/

├── app.py                # Main Gradio app

├── caption.py            # Caption generation logic

├── requirements.txt      # Dependencies

└── README.md             # This file

### 🧠 Models Used
- Salesforce/BLIP2

- transformers

- gradio

You can easily switch to other Hugging Face models if needed.

### 📦 Installation
### 1. Clone the repo and cd into it
```
git clone https://github.com/yourusername/ai-image-captioning-bot.git
cd ai-image-captioning-bot
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
