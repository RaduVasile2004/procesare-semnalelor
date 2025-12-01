import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

N1, N2 = 256, 256
n1 = np.arange(N1)
n2 = np.arange(N2)
n1_grid, n2_grid = np.meshgrid(n1, n2, indexing='ij')

#1
k1, k2 = 20, 30
x1 = np.sin(2 * np.pi * k1 * n1_grid / N1 + 3 * np.pi * k2 * n2_grid / N2)
Y1 = np.fft.fft2(x1)
freq_db1 = 20 * np.log10(np.abs(np.fft.fftshift(Y1)) + 1e-10)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(x1, cmap='gray')
plt.title('Semnal 1')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(freq_db1, cmap='hot', vmin=0, vmax=80)
plt.title('Spectrul 1')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('semnal_1.png', dpi=150, bbox_inches='tight')
plt.close()

#2
k3, k4 = 15, 10
x2 = np.sin(4 * np.pi * k3 * n1_grid / N1) + np.cos(6 * np.pi * k4 * n2_grid / N2)
Y2 = np.fft.fft2(x2)
freq_db2 = 20 * np.log10(np.abs(np.fft.fftshift(Y2)) + 1e-10)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(x2, cmap='gray')
plt.title('Semnal 2')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(freq_db2, cmap='hot', vmin=0, vmax=80)
plt.title('Spectrul 2')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('semnal_2.png', dpi=150, bbox_inches='tight')
plt.close()

#3
Y3 = np.zeros((256, 256), dtype=complex)
Y3[0, 5] = 1
Y3[0, 251] = 1
x3 = np.fft.ifft2(Y3)
x3_real = np.real(x3)
freq_db3 = 20 * np.log10(np.abs(np.fft.fftshift(Y3)) + 1e-10)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(x3_real, cmap='gray')
plt.title('Semnal 3')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(freq_db3, cmap='hot')
plt.title('Spectrul 3')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('semnal_3.png', dpi=150, bbox_inches='tight')
plt.close()

#4
Y4 = np.zeros((256, 256), dtype=complex)
Y4[5, 0] = 1
Y4[251, 0] = 1
x4 = np.fft.ifft2(Y4)
x4_real = np.real(x4)
freq_db4 = 20 * np.log10(np.abs(np.fft.fftshift(Y4)) + 1e-10)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(x4_real, cmap='gray')
plt.title('Semnal 4')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(freq_db4, cmap='hot')
plt.title('Spectrul 4')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('semnal_4.png', dpi=150, bbox_inches='tight')
plt.close()

#5
Y5 = np.zeros((256, 256), dtype=complex)
Y5[5, 5] = 1
Y5[251, 251] = 1
x5 = np.fft.ifft2(Y5)
x5_real = np.real(x5)
freq_db5 = 20 * np.log10(np.abs(np.fft.fftshift(Y5)) + 1e-10)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.imshow(x5_real, cmap='gray')
plt.title('Semnal 5')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(freq_db5, cmap='hot')
plt.title('Spectrul 5')
plt.colorbar()
plt.axis('off')
plt.tight_layout()
plt.savefig('semnal_5.png', dpi=150, bbox_inches='tight')
plt.close()