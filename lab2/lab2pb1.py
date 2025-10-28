import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


# Parametrii semnalului
A = 2.0
f = 5.0
phi = np.pi/4
t_start = 0
t_end = 1
num_points = 1000

t = np.linspace(t_start, t_end, num_points)

# Semnal sinusoidal (sin)
x_sin = A * np.sin(2 * np.pi * f * t + phi)

# Semnal cosinusoidal identic
x_cos = A * np.cos(2 * np.pi * f * t + phi - np.pi/2)

diferenta_maxima = np.max(np.abs(x_sin - x_cos))
print(f"Diferenta maxima intre semnale: {diferenta_maxima}")

# Afisare grafica
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

ax1.plot(t, x_sin, 'b-', linewidth=2, label='sinus')
ax1.set_title('Semnal sinusoidal - SIN')
ax1.set_xlabel('Timp [s]')
ax1.set_ylabel('Amplitudine')
ax1.grid(True)
ax1.legend()

ax2.plot(t, x_cos, 'r-', linewidth=2, label='cosinus')
ax2.set_title('Semnal cosinusoidal - COS')
ax2.set_xlabel('Timp [s]')
ax2.set_ylabel('Amplitudine')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()