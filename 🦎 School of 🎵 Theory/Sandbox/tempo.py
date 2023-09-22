import librosa
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python tempo_estimation.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the onset envelope (you can replace this with your onset detection method)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Compute tempo using librosa.feature.tempo
tempo, _ = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)

# Print the estimated tempo
print(f"Estimated Tempo: {tempo[0]} BPM")
