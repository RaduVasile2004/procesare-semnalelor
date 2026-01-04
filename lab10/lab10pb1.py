import numpy as np
import matplotlib.pyplot as plt

N = 1000
t = np.arange(N)

a, b, c = 0.0001, 0.02, 10
trend = a * t**2 + b * t + c

f1, f2 = 0.05, 0.1
A1, A2 = 5, 3
phi = np.pi / 4
season = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t + phi)

sigma = 1.0
noise = np.random.normal(0, sigma, N)

y = trend + season + noise

fig, axs = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

axs[0].plot(t, trend, label='Trend (grad 2)', color='orange')
axs[0].legend()
axs[0].set_ylabel('Trend')

axs[1].plot(t, season, label='Season (2 frecvente)', color='green')
axs[1].legend()
axs[1].set_ylabel('Season')

axs[2].plot(t, noise, label='Zgomot alb', color='red', alpha=0.7)
axs[2].legend()
axs[2].set_ylabel('Noise')

axs[3].plot(t, y, label='Serie finala', color='blue')
axs[3].legend()
axs[3].set_ylabel('Serie finala')
axs[3].set_xlabel('Time (t)')

plt.suptitle('Serie de timp cu Trend, Season si Zgomot')
plt.tight_layout()
plt.savefig('lab10pb1.png')
plt.close(fig)