# 🗣️ SpeakEasy - A Speech to Text Transcription Tool

## 🎯 Description

**SpeakEasy** is a simple and intuitive web-based tool that allows users to convert audio files into readable text using a speech recognition system. Built using Python, Flask, and OpenAI's Whisper model, this tool processes short audio clips and outputs high-quality transcriptions – all offline.

---

## 📸 Demo

> _Add a screenshot or GIF of your app UI + transcription in action here._

---

## 🧠 Features

- 🎤 Upload `.mp3` or `.wav` audio files  
- ⚡ Fast & accurate offline transcription using Whisper  
- 🌑 Clean dark-themed user interface  
- 🔘 Transcribe button changes based on process state  
- 🧹 Clear button to reset uploaded file and transcription  
- 💻 Runs fully offline (no internet needed after setup)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python (Flask)  
- **Model**: OpenAI Whisper (offline)  
- **Hosting**: Locally (Railway / Render / Replit optional)

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/speech-recognition-tool.git
cd speech-recognition-tool

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open in browser
http://127.0.0.1:5000/

##📦 Requirements
flask
openai-whisper
torch
werkzeug
