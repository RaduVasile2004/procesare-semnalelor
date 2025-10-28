import numpy as np
import matplotlib.pyplot as plt


# Parametrii
A = 1.0
f = 3.0
t_start = 0
t_end = 2
num_points = 1000


t = np.linspace(t_start, t_end, num_points)


faze = [0, np.pi / 4, np.pi / 2, np.pi]
nume_faze = ['0', 'π/4', 'π/2', 'π']
culori = ['blue', 'red', 'green', 'orange']

plt.figure(figsize=(12, 6))

for i, phi in enumerate(faze):
    #sinusoidal
    x = A * np.sin(2 * np.pi * f * t + phi)

    plt.plot(t, x, linewidth=2, color=culori[i], label=f'φ = {nume_faze[i]}')

plt.title('Seminale sinusoidale cu amplitudine unitara si faze diferite')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()
plt.savefig('exercitiul2.png', dpi=150, bbox_inches='tight')


