import librosa
import librosa.display
import numpy as np
import pandas as pd
import os

def extract_audio_features(audio_path):
    print(f"🔍 Extracting features from: {audio_path}")
    
    y, sr = librosa.load(audio_path)
    
    duration = librosa.get_duration(y=y, sr=sr)
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=y).T, axis=0)
    rmse = np.mean(librosa.feature.rms(y=y).T, axis=0)
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr).T, axis=0)
    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr).T, axis=0)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs, axis=1)
    
    feature_dict = {
        "filename": os.path.basename(audio_path),
        "duration": duration,
        "sample_rate": sr,
        "zero_crossing_rate": zcr,
        "rms_energy": rmse,
        "spectral_centroid": spectral_centroid,
        "spectral_rolloff": spectral_rolloff
    }

    for i, mfcc in enumerate(mfccs_mean, start=1):
        feature_dict[f"mfcc_{i}"] = mfcc

    return feature_dict

# ===== MAIN FUNCTION =====
if __name__ == "__main__":
    audio_file = "sample.wav"  # Replace with your .wav file name

    if not os.path.exists(audio_file):
        print("❌ Audio file not found. Please check the path and filename.")
    else:
        features = extract_audio_features(audio_file)

        df = pd.DataFrame([features])
        df.to_csv("audio_features_output.csv", index=False)
        print("✅ Audio features extracted and saved to 'audio_features_output.csv'")
