import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python chroma_cens.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute Chroma Energy Normalized (CENS)
chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)

# Plot the Chroma CENS
plt.figure(figsize=(12, 8))
librosa.display.specshow(chroma_cens, x_axis='time')
plt.colorbar()
plt.title('Chroma Energy Normalized (CENS)')
plt.show()
