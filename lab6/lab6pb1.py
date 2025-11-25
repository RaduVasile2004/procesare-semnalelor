import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

B = 1
t_continuous = np.linspace(-3, 3, 1000)
x_continuous = np.sinc(B * t_continuous) ** 2

frequencies = [1, 1.5, 2, 4]

for i, fs in enumerate(frequencies):
    plt.figure(figsize=(8, 5))

    Ts = 1 / fs
    n = np.arange(-3, 3, Ts)
    n = n[(n >= -3) & (n <= 3)]
    x_sampled = np.sinc(B * n) ** 2

    t_recon = np.linspace(-3, 3, 1000)
    x_recon = np.zeros_like(t_recon)

    for idx, t_val in enumerate(t_recon):
        x_recon[idx] = np.sum(x_sampled * np.sinc((t_val - n) / Ts))

    plt.plot(t_continuous, x_continuous, 'b-', linewidth=2, label='Original')
    plt.plot(n, x_sampled, 'ro', markersize=4, label='Eșantioane')
    plt.plot(t_recon, x_recon, 'g--', linewidth=1.5, label='Reconstruit')
    plt.title(f'Fs = {fs} Hz')
    plt.grid(True)
    plt.xlim(-3, 3)
    plt.legend()
    plt.savefig(f'figura_fs_{fs}_Hz.png')
    plt.close()

B_nou = 2
t_continuous_nou = np.linspace(-3, 3, 1000)
x_continuous_nou = np.sinc(B_nou * t_continuous_nou) ** 2

for i, fs in enumerate(frequencies):
    plt.figure(figsize=(8, 5))

    Ts = 1 / fs
    n = np.arange(-3, 3, Ts)
    n = n[(n >= -3) & (n <= 3)]
    x_sampled_nou = np.sinc(B_nou * n) ** 2

    t_recon_nou = np.linspace(-3, 3, 1000)
    x_recon_nou = np.zeros_like(t_recon_nou)

    for idx, t_val in enumerate(t_recon_nou):
        x_recon_nou[idx] = np.sum(x_sampled_nou * np.sinc((t_val - n) / Ts))

    plt.plot(t_continuous_nou, x_continuous_nou, 'b-', linewidth=2, label='Original')
    plt.plot(n, x_sampled_nou, 'ro', markersize=4, label='Eșantioane')
    plt.plot(t_recon_nou, x_recon_nou, 'g--', linewidth=1.5, label='Reconstruit')
    plt.title(f'B = {B_nou}, Fs = {fs} Hz')
    plt.grid(True)
    plt.xlim(-3, 3)
    plt.legend()
    plt.savefig(f'figura_B_{B_nou}_fs_{fs}_Hz.png')
    plt.close()

print("Toate figurile au fost salvate ca fișiere PNG")