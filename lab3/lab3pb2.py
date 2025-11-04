import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection

# param
fs = 30  # frec esantionare
f = 3  # frecv semnal
N = 200  # nr esantioane
t = np.arange(N) / fs
x = np.cos(2 * np.pi * f * t)  # sinus
n = np.arange(N)

# semnal si infasurarea pe cercul unitate
omega_wrap = 1  # frecventa de infasurare
y = x * np.exp(-2j * np.pi * omega_wrap * t)

k = 100  # index punct rosu

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# semnal sinus
ax1.plot(t, x, 'b-', linewidth=1)
ax1.plot(t[k], x[k], 'ro', markersize=8)
ax1.axvline(t[k], color='r', linestyle='--', alpha=0.7)
ax1.set_xlabel('Timp [s]')
ax1.set_ylabel('Amplitudine')
ax1.set_title(f'Semnal sinusoidal, f = {f} Hz')
ax1.grid(True)

# cerc unitate
circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--')
ax2.add_patch(circle)
ax2.plot(y.real, y.imag, 'b-', alpha=0.7, linewidth=1)
ax2.plot([0, y[k].real], [0, y[k].imag], 'r-', linewidth=2)
ax2.plot(y[k].real, y[k].imag, 'ro', markersize=8)
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlabel('Real')
ax2.set_ylabel('Imag')
ax2.set_title(f'Infasurare pe cercul unitate (ω = {omega_wrap} Hz)')
ax2.set_aspect('equal')
ax2.grid(True)

plt.tight_layout()
plt.savefig('figura1.pdf')
#part2
# influenta frecventei de infasurare
omega_values = [1, 2, f, 7]  # frecvente de infasurare

fig2, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

for idx, omega in enumerate(omega_values):
    z = x * np.exp(-2j * np.pi * omega * t)
    dist = np.abs(z)

    points = np.array([z.real, z.imag]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    norm = plt.Normalize(dist.min(), dist.max())
    lc = LineCollection(segments, cmap=cm.viridis, norm=norm, alpha=0.8)
    lc.set_array(dist)
    lc.set_linewidth(2)

    axs[idx].add_collection(lc)

    circle = plt.Circle((0, 0), 1, fill=False, color='gray', linestyle='--', linewidth=1)
    axs[idx].add_patch(circle)
    axs[idx].set_xlim(-1.5, 1.5)
    axs[idx].set_ylim(-1.5, 1.5)
    axs[idx].set_xlabel('Real')
    axs[idx].set_ylabel('Imag')
    axs[idx].set_title(f'ω = {omega} Hz')
    axs[idx].set_aspect('equal')
    axs[idx].grid(True)

    step = N // 10
    for i in range(0, N, step):
        axs[idx].plot(z.real[i], z.imag[i], 'o', markersize=4,
                      color=cm.viridis(norm(dist[i])), alpha=0.8)

plt.tight_layout()
plt.savefig('figura2.pdf')

