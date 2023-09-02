import librosa
import numpy as np
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python audio_reconstruction.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the magnitude spectrogram
S = np.abs(librosa.stft(y))

# Invert using Griffin-Lim
y_inv = librosa.griffinlim(S)

# Invert without estimating phase
y_istft = librosa.istft(S)

# Plot the original, Griffin-Lim reconstruction, and istft reconstruction
fig, ax = plt.subplots(nrows=3, sharex=True, sharey=True)

librosa.display.waveshow(y, sr=sr, color='b', ax=ax[0])
ax[0].set(title='Original', xlabel=None)
ax[0].label_outer()

librosa.display.waveshow(y_inv, sr=sr, color='g', ax=ax[1])
ax[1].set(title='Griffin-Lim reconstruction', xlabel=None)
ax[1].label_outer()

librosa.display.waveshow(y_istft, sr=sr, color='r', ax=ax[2])
ax[2].set_title('Magnitude-only istft reconstruction')

# Show the plot
plt.show()
