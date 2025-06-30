from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import whisper

# Initialize Flask app
app = Flask(__name__)
print("✅ Flask app has started.")

# Load Whisper model
model = whisper.load_model("tiny")  # or "tiny" for faster download

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file in request"}), 400

    audio_file = request.files["audio"]
    filename = secure_filename(audio_file.filename)
    filepath = os.path.join("temp_audio", filename)
    os.makedirs("temp_audio", exist_ok=True)
    audio_file.save(filepath)

    try:
        print("🎧 Transcribing with Whisper...")
        result = model.transcribe(filepath)
        text = result["text"]
        print("✅ Transcription complete.")
    except Exception as e:
        print("❌ Whisper failed:", e)
        return jsonify({"text": f"⚠️ Transcription failed: {e}"}), 500

    os.remove(filepath)
    return jsonify({"text": text})

# ✅ REQUIRED block to actually run the Flask server
if __name__ == "__main__":
    app.run(debug=True)
