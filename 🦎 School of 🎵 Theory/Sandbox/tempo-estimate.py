import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python tempo_estimation.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Estimate the tempo
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

# Create a tempo curve
tempogram = librosa.feature.tempogram(y=y, sr=sr)

# Plot the tempo curve
plt.figure(figsize=(12, 8))
librosa.display.specshow(tempogram, x_axis='time')
plt.colorbar()
plt.title(f'Tempo Estimation: {tempo:.2f} BPM')
plt.show()
