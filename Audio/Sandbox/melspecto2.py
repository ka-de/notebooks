import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys
import numpy as np

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python spectrogram.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Adjust the frequency range from 0 Hz to n Hz
fmin = 0
fmax = 11000

# Increase the number of mel filter banks (adjust n_mels)
n_mels = 512  # You can change this value to increase the frequency resolution
spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmin=fmin, fmax=fmax)

# Convert to decibels
db_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(12, 8))
librosa.display.specshow(db_spectrogram, x_axis='time', y_axis='mel', sr=sr, fmin=fmin, fmax=fmax)
plt.colorbar(format='%+2.0f dB')
plt.title('Mel Spectrogram ({fmin} Hz to {fmax} Hz)')
plt.show()