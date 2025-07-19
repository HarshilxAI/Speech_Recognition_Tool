from pydub import AudioSegment
import os

def convert_mp3_to_wav(mp3_path, output_folder):
    if not mp3_path.endswith(".mp3"):
        print("Only .mp3 files are supported.")
        return

    audio = AudioSegment.from_mp3(mp3_path)
    base_filename = os.path.splitext(os.path.basename(mp3_path))[0]
    wav_path = os.path.join(output_folder, f"{base_filename}.wav")
    
    audio.export(wav_path, format="wav")
    print(f"Conversion successful! Saved to {wav_path}")

# Example usage
if __name__ == "__main__":
    mp3_file = "sample_audio.mp3"  
    output_dir = "."              
    convert_mp3_to_wav(mp3_file, output_dir)
