from pydub import AudioSegment
import os

def get_audio_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path)
        duration_sec = len(audio) / 1000  # milliseconds to seconds
        print(f"File: {os.path.basename(file_path)}")
        print(f"Duration: {duration_sec:.2f} seconds ({duration_sec / 60:.2f} minutes)")
    except Exception as e:
        print("Error processing audio file:", e)

# Example usage
if __name__ == "__main__":
    audio_file = "temp_audio/sample.wav"  # Change to your desired path
    get_audio_duration(audio_file)
