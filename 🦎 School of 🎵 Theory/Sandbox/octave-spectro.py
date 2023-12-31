import librosa
import librosa.display
import matplotlib.pyplot as plt
import sys

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python octave_spectrogram.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute the Short-Time Fourier Transform (STFT)
D = librosa.stft(y)

# Convert the magnitude spectrogram to dB scale
db_spec = librosa.amplitude_to_db(abs(D))

# Plot the octave-based spectrogram
plt.figure(figsize=(12, 8))
librosa.display.specshow(db_spec, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Octave-based Spectrogram')
plt.show()
