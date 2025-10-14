import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

# a
fs_a = 1600
t_a = np.arange(1600) / fs_a
freq_a = 400
signal_a = np.sin(2 * np.pi * freq_a * t_a)

plt.figure(figsize=(10, 6))

mask_a = t_a <= 0.01
plt.plot(t_a[mask_a], signal_a[mask_a], 'b-', linewidth=1.5)
plt.title('Sinusoidal 400 Hz, 1600 samples')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.savefig('2a_sinus_400hz.pdf', dpi=300, bbox_inches='tight')


# b
duration_b = 3
fs_b = 8000
t_b = np.arange(0, duration_b, 1/fs_b)
freq_b = 800
signal_b = np.sin(2 * np.pi * freq_b * t_b)

plt.figure(figsize=(10, 6))

mask_b = t_b <= 0.005
plt.plot(t_b[mask_b], signal_b[mask_b], 'r-', linewidth=1.5)
plt.title('Sinusoidal 800 Hz, 3 seconds')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.savefig('2b_sinus_800hz.pdf', dpi=300, bbox_inches='tight')


# c
duration_c = 0.02
fs_c = 10000
t_c = np.arange(0, duration_c, 1/fs_c)
freq_c = 240
signal_c = 2 * (t_c * freq_c - np.floor(0.5 + t_c * freq_c))

plt.figure(figsize=(10, 6))
plt.plot(t_c, signal_c, 'g-', linewidth=1)
plt.title('Sawtooth 240 Hz')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.savefig('2c_sawtooth_240hz.pdf', dpi=300, bbox_inches='tight')


# d
duration_d = 0.02
fs_d = 10000
t_d = np.arange(0, duration_d, 1/fs_d)
freq_d = 300
signal_d = np.sign(np.sin(2 * np.pi * freq_d * t_d))

plt.figure(figsize=(10, 6))
plt.plot(t_d, signal_d, 'm-', linewidth=1)
plt.title('Square 300 Hz')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.tight_layout()
plt.savefig('2d_square_300hz.pdf', dpi=300, bbox_inches='tight')


# e
signal_e = np.random.rand(128, 128)

plt.figure(figsize=(8, 8))
plt.imshow(signal_e, cmap='viridis')
plt.title('Random 2D signal 128x128')
plt.colorbar()
plt.tight_layout()
plt.savefig('2e_2d_random.pdf', dpi=300, bbox_inches='tight')


# f
x, y = np.meshgrid(np.linspace(0, 1, 128), np.linspace(0, 1, 128))
signal_f = np.zeros((128, 128))
center_x, center_y = 64, 64
for i in range(128):
    for j in range(128):
        distance = np.sqrt((i - center_x)**2 + (j - center_y)**2)
        signal_f[i, j] = 1 - distance / 90

plt.figure(figsize=(8, 8))
plt.imshow(signal_f, cmap='plasma')
plt.title('Radial gradient 128x128')
plt.colorbar()
plt.tight_layout()
plt.savefig('2f_2d_gradient.pdf', dpi=300, bbox_inches='tight')


