import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python spectral_bandwidth.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the spectral bandwidth
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)

# Plot the spectral bandwidth
plt.figure(figsize=(12, 8))
plt.semilogy(spectral_bandwidth.T, label='Spectral Bandwidth')
plt.ylabel('Hz')
plt.xticks([])
plt.xlim([0, spectral_bandwidth.shape[-1]])
plt.legend()
plt.show()
