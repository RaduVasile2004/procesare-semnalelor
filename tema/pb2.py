import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn

try:
    from scipy.datasets import face
except ImportError:
    from scipy.misc import face

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

def rgb2ycbcr(im):
    xform = np.array([[.299, .587, .114], [-.1687, -.3313, .5], [.5, -.4187, -.0813]])
    ycbcr = im.dot(xform.T)
    ycbcr[:, :, [1, 2]] += 128
    return ycbcr

def ycbcr2rgb(im):
    xform = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
    rgb = im.astype(float)
    rgb[:, :, [1, 2]] -= 128
    rgb = rgb.dot(xform.T)
    return np.clip(rgb, 0, 255)

def jpeg_color(image_rgb, Q_matrix):
    image_ycbcr = rgb2ycbcr(image_rgb)
    Y, Cb, Cr = image_ycbcr[:, :, 0], image_ycbcr[:, :, 1], image_ycbcr[:, :, 2]
    Y_rec = jpeg_compress_decompress_block(Y, Q_matrix)
    Cb_rec = jpeg_compress_decompress_block(Cb, Q_matrix)
    Cr_rec = jpeg_compress_decompress_block(Cr, Q_matrix)
    return ycbcr2rgb(np.dstack((Y_rec, Cb_rec, Cr_rec)))

img_color = face()
res_color = jpeg_color(img_color, Q_JPEG)

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(img_color)
plt.title('Original Color')
plt.axis('off')

plt.subplot(122)
plt.imshow(res_color.astype(np.uint8))
plt.title('JPEG Color Reconstruit')
plt.axis('off')

plt.savefig('grafic_task2.png', bbox_inches='tight')
print('Graficul complet a fost salvat in: grafic_task2.png')

plt.show()