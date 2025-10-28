import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')

# a
t = np.arange(0, 0.03 + 0.0005, 0.0005)

plt.figure(figsize=(10, 4))
plt.plot(t, np.zeros_like(t), 'bo-', markersize=3, linewidth=0.5)
plt.title('Axa reala de timp [0 : 0.0005 : 0.03]')
plt.xlabel('Timp [s]')
plt.ylabel('Puncte de esantionare')
plt.grid(True)
plt.yticks([])
plt.tight_layout()
plt.savefig('1a_axa_timp.pdf')


# b
x_t = np.cos(520 * np.pi * t + np.pi/3)
y_t = np.cos(280 * np.pi * t - np.pi/3)
z_t = np.cos(120 * np.pi * t + np.pi/3)

plt.figure(figsize=(12, 10))

# x(t)
plt.subplot(3, 1, 1)
plt.plot(t, x_t, 'b-', linewidth=1.5)
plt.title('Semnalul x(t) = cos(520πt + π/3)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# y(t)
plt.subplot(3, 1, 2)
plt.plot(t, y_t, 'r-', linewidth=1.5)
plt.title('Semnalul y(t) = cos(280πt - π/3)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# z(t)
plt.subplot(3, 1, 3)
plt.plot(t, z_t, 'g-', linewidth=1.5)
plt.title('Semnalul z(t) = cos(120πt + π/3)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.savefig('1b_semnale_continue.pdf')


# c
fs = 200  # frecventa
Ts = 1/fs  # perioada

# axa timp
n = np.arange(0, 0.03 + Ts, Ts)

# semnale esantionate
x_n = np.cos(520 * np.pi * n + np.pi/3)
y_n = np.cos(280 * np.pi * n - np.pi/3)
z_n = np.cos(120 * np.pi * n + np.pi/3)

plt.figure(figsize=(12, 10))

# x[n]
plt.subplot(3, 1, 1)
plt.stem(n, x_n, 'b', markerfmt='bo', linefmt='b-', basefmt=' ')
plt.plot(t, x_t, 'b--', alpha=0.3)  # semnal continuu pt comparatie
plt.title('Semnalul esantionat x[n] (fs = 200 Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# y[n]
plt.subplot(3, 1, 2)
plt.stem(n, y_n, 'r', markerfmt='ro', linefmt='r-', basefmt=' ')
plt.plot(t, y_t, 'r--', alpha=0.3)
plt.title('Semnalul esantionat y[n] (fs = 200 Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# z[n]
plt.subplot(3, 1, 3)
plt.stem(n, z_n, 'g', markerfmt='go', linefmt='g-', basefmt=' ')
plt.plot(t, z_t, 'g--', alpha=0.3)
plt.title('Semnalul esantionat z[n] (fs = 200 Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

plt.tight_layout()
plt.savefig('1c_semnale_esantionate.pdf')

