import librosa
import sys
import matplotlib.pyplot as plt  # Import matplotlib

# Check if an audio file path is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python delta_feature.py <audio_file_path>")
    sys.exit(1)

# Get the audio file path from the command-line argument
audio_file = sys.argv[1]

# Load the audio file
y, sr = librosa.load(audio_file)

# Compute a feature matrix (e.g., MFCCs)
feature_matrix = librosa.feature.mfcc(y=y, sr=sr)

# Compute the delta feature matrix
delta_matrix = librosa.feature.delta(feature_matrix)

# Plot the delta feature matrix
plt.figure(figsize=(12, 8))
librosa.display.specshow(delta_matrix, x_axis='time')
plt.colorbar()
plt.title('Delta Feature Matrix')
plt.show()