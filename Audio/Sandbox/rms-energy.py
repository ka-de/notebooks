import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python rms_energy.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute RMS energy
rms_energy = librosa.feature.rms(y=y)

# Plot the RMS energy
plt.figure(figsize=(12, 8))
plt.semilogy(rms_energy.T, label='RMS Energy')
plt.ylabel('RMS Energy')
plt.xticks([])
plt.xlim([0, rms_energy.shape[-1]])
plt.legend()
plt.show()
