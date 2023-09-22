import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python fourier_tempogram.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the onset envelope (you can replace this with your own onset detection method)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)

# Compute the Fourier Tempogram
tempogram = librosa.feature.fourier_tempogram(onset_envelope=onset_env, sr=sr)

# Plot the Fourier Tempogram
plt.figure(figsize=(12, 8))
librosa.display.specshow(tempogram, x_axis='time', y_axis='tempo')
plt.colorbar()
plt.title('Fourier Tempogram')
plt.show()
