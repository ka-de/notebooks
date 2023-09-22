import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python zero_crossing_rate.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the zero crossing rate
zero_crossings = librosa.feature.zero_crossing_rate(y)

# Plot the zero crossing rate
plt.figure(figsize=(12, 8))
plt.semilogy(zero_crossings.T, label='Zero Crossing Rate')
plt.ylabel('Zero Crossing Rate')
plt.xticks([])
plt.xlim([0, zero_crossings.shape[-1]])
plt.legend()
plt.show()
