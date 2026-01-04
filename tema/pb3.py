import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn

try:
    from scipy.datasets import ascent
except ImportError:
    from scipy.misc import ascent

Q_JPEG = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

def jpeg_compress_decompress_block(image, Q_matrix):
    h, w = image.shape
    h_pad = (8 - h % 8) % 8
    w_pad = (8 - w % 8) % 8
    image_padded = np.pad(image, ((0, h_pad), (0, w_pad)), mode='edge')
    h_new, w_new = image_padded.shape
    image_jpeg = np.zeros_like(image_padded)
    for i in range(0, h_new, 8):
        for j in range(0, w_new, 8):
            block = image_padded[i:i + 8, j:j + 8]
            freq_block = dctn(block, norm='ortho')
            quant_block = np.round(freq_block / Q_matrix)
            dequant_block = quant_block * Q_matrix
            rec_block = idctn(dequant_block, norm='ortho')
            image_jpeg[i:i + 8, j:j + 8] = rec_block
    result = image_jpeg[:h, :w]
    return np.clip(result, 0, 255)

def mse(img1, img2):
    return np.mean((img1 - img2) ** 2)

def find_jpeg_quality_by_mse(image, target_mse):
    low = 0.1
    high = 100.0
    best_scale = 1.0
    best_img = image.copy()

    for _ in range(15):
        mid = (low + high) / 2
        Q_scaled = Q_JPEG * mid
        res = jpeg_compress_decompress_block(image, Q_scaled)
        err = mse(image, res)
        if err <= target_mse:
            best_scale = mid
            best_img = res
            low = mid
        else:
            high = mid
    return best_img, best_scale, mse(image, best_img)

X = ascent()
target_mse = 50.0

final_img, scale, final_mse = find_jpeg_quality_by_mse(X, target_mse)

plt.figure(figsize=(8, 8))
plt.imshow(final_img, cmap='gray')
plt.title(f'Optimizare MSE\nTarget: {target_mse}, Realizat: {final_mse:.2f}\nFactor Scalare Q: {scale:.2f}')
plt.axis('off')

plt.savefig('grafic_task3.png', bbox_inches='tight')
print('Graficul complet a fost salvat in: grafic_task3.png')

plt.show()