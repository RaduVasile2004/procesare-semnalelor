import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets

X = datasets.face(gray=True)
Y = np.fft.fft2(X)

pixel_noise = 50
noise = np.random.randint(-pixel_noise, pixel_noise+1, size=X.shape)
X_noisy = X + noise
X_noisy = np.clip(X_noisy, 0, 255)

Y_noisy = np.fft.fft2(X_noisy)
signal_power = np.mean(X**2)
noise_power = np.mean((X_noisy - X)**2)
snr_initial = 10 * np.log10(signal_power / noise_power)

rows, cols = X.shape
crow, ccol = rows//2, cols//2
radius = 250

Y_filtered = Y_noisy.copy()
for i in range(rows):
    for j in range(cols):
        if (i-crow)**2 + (j-ccol)**2 > radius**2:
            Y_filtered[i, j] = 0

X_filtered = np.real(np.fft.ifft2(Y_filtered))

filtered_noise_power = np.mean((X_filtered - X)**2)
snr_final = 10 * np.log10(signal_power / filtered_noise_power)

plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.imshow(X, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(X_noisy, cmap='gray')
plt.title(f'Noisy\nSNR: {snr_initial:.2f} dB')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(X_filtered, cmap='gray')
plt.title(f'Filtered\nSNR: {snr_final:.2f} dB')
plt.axis('off')

plt.subplot(2, 3, 4)
freq_db = 20 * np.log10(np.abs(np.fft.fftshift(Y)) + 1e-10)
plt.imshow(freq_db, cmap='hot')
plt.title('Original Spectrum')
plt.colorbar()
plt.axis('off')

plt.subplot(2, 3, 5)
freq_db_noisy = 20 * np.log10(np.abs(np.fft.fftshift(Y_noisy)) + 1e-10)
plt.imshow(freq_db_noisy, cmap='hot')
plt.title('Noisy Spectrum')
plt.colorbar()
plt.axis('off')

plt.subplot(2, 3, 6)
freq_db_filtered = 20 * np.log10(np.abs(np.fft.fftshift(Y_filtered)) + 1e-10)
plt.imshow(freq_db_filtered, cmap='hot')
plt.title('Filtered Spectrum')
plt.colorbar()
plt.axis('off')

plt.tight_layout()
plt.savefig('denoising_results.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"SNR initial: {snr_initial:.2f} dB")
print(f"SNR final: {snr_final:.2f} dB")
print(f"Improvement: {snr_final - snr_initial:.2f} dB")