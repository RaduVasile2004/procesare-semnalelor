import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True)
Y = np.fft.fft2(X)
target_snr_db = 20
magnitude = np.abs(Y)

sorted_magnitude = np.sort(magnitude.flatten())[::-1]
cumulative_energy = np.cumsum(sorted_magnitude**2)
total_energy = cumulative_energy[-1]
target_snr_linear = 10**(target_snr_db / 10)
threshold_energy = total_energy * (1 - 1/target_snr_linear)
threshold_index = np.argmax(cumulative_energy > threshold_energy)
freq_cutoff = sorted_magnitude[threshold_index]

Y_compressed = Y.copy()
Y_compressed[magnitude < freq_cutoff] = 0
X_compressed = np.real(np.fft.ifft2(Y_compressed))
noise = X - X_compressed
snr_real = 10 * np.log10(np.mean(X**2) / np.mean(noise**2))

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(X, cmap='gray')
plt.title('Original')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(X_compressed, cmap='gray')
plt.title(f'Compressed\nSNR: {snr_real:.2f} dB')
plt.axis('off')
plt.subplot(1, 3, 3)
freq_db_compressed = 20 * np.log10(np.abs(np.fft.fftshift(Y_compressed)) + 1e-10)
plt.imshow(freq_db_compressed, cmap='hot')
plt.title('Compressed Spectrum')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('compresie_imagine.png', dpi=150, bbox_inches='tight')
plt.close()