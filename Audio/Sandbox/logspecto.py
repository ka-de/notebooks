import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys
import numpy as np

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python log_spectrogram.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the standard spectrogram
spectrogram = np.abs(librosa.stft(y))

# Convert to a logarithmic scale (log-spectrogram)
log_spectrogram = librosa.amplitude_to_db(spectrogram)

# Plot the log-spectrogram
plt.figure(figsize=(12, 8))
librosa.display.specshow(log_spectrogram, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Log-Spectrogram')
plt.show()
