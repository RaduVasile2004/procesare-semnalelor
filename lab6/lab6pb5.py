import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def fereastra_dreptunghiulara(N):
    return np.ones(N)

def fereastra_hanning(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.arange(N) / (N - 1)))

t = np.linspace(0, 0.02, 200)
f = 100
A = 1
phi = 0
sinusoida = A * np.sin(2 * np.pi * f * t + phi)

Nw = 200
w_rect = fereastra_dreptunghiulara(Nw)
w_hanning = fereastra_hanning(Nw)

sinusoida_rect = sinusoida * w_rect
sinusoida_hanning = sinusoida * w_hanning

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, sinusoida)
plt.title('Sinusoida Originala')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, sinusoida_rect)
plt.title('Sinusoida cu Fereastra Dreptunghiulara')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, sinusoida_hanning)
plt.title('Sinusoida cu Fereastra Hanning')
plt.grid(True)

plt.tight_layout()
plt.savefig('exercitiul5.png')
plt.close()