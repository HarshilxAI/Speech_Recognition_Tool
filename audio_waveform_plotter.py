import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_waveform(file_path):
    sample_rate, data = wavfile.read(file_path)

    duration = len(data) / sample_rate
    time = [i / sample_rate for i in range(len(data))]

    plt.figure(figsize=(12, 4))
    plt.plot(time, data)
    plt.title("Audio Waveform")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    wav_file = "E:/AI Internship/TASKS/Speech_Recog_Tool/temp_audio/your_audio.wav"
  # 🔄 Replace with your file
    plot_waveform(wav_file)
