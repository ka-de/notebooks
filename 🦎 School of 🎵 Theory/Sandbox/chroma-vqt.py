import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python chroma_vqt.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Specify the intervals parameter as 'equal'
intervals = 'equal'

# Compute the Variable-Q Chromagram
chromagram = librosa.feature.chroma_vqt(y=y, sr=sr, intervals=intervals)

# Plot the Variable-Q Chromagram
plt.figure(figsize=(12, 8))
librosa.display.specshow(chromagram, x_axis='time')
plt.colorbar()
plt.title('Variable-Q Chromagram')
plt.show()
