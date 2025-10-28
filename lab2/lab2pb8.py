import numpy as np
import matplotlib.pyplot as plt


# Definirea intervalului
alpha = np.linspace(-np.pi / 2, np.pi / 2, 1000)
sin_alpha = np.sin(alpha)

# Aproximari
# 1. Aproximarea liniara (Taylor de ordinul 1)
approx_linear = alpha

# 2. Aproximarea Pade [3/2]
approx_pade = (alpha - (7 / 60) * alpha ** 3) / (1 + alpha ** 2 / 20)

# Calculul erorilor
error_linear = np.abs(sin_alpha - approx_linear)
error_pade = np.abs(sin_alpha - approx_pade)

# Afisare grafica principala
plt.figure(figsize=(15, 12))

# functiile principale
plt.subplot(3, 2, 1)
plt.plot(alpha, sin_alpha, 'b-', linewidth=3, label='sin(α)')
plt.plot(alpha, approx_linear, 'r--', linewidth=2, label='α (aproximare liniara)')
plt.plot(alpha, approx_pade, 'g--', linewidth=2, label='Pade [3/2]')
plt.title('Comparare functii')
plt.xlabel('α [rad]')
plt.ylabel('Valoare')
plt.grid(True, alpha=0.3)
plt.legend()
plt.axis([-np.pi / 2, np.pi / 2, -1.5, 1.5])

# erori absolute
plt.subplot(3, 2, 2)
plt.plot(alpha, error_linear, 'r-', linewidth=2, label='Eroare liniara')
plt.plot(alpha, error_pade, 'g-', linewidth=2, label='Eroare Pade')
plt.title('Eroarea absoluta')
plt.xlabel('α [rad]')
plt.ylabel('|Eroare|')
plt.grid(True, alpha=0.3)
plt.legend()
plt.yscale('log')

# eroare relativa
error_rel_linear = error_linear / np.abs(sin_alpha)
error_rel_pade = error_pade / np.abs(sin_alpha)

# Evitam impartirea la zero
error_rel_linear[np.abs(sin_alpha) < 1e-10] = 0
error_rel_pade[np.abs(sin_alpha) < 1e-10] = 0

plt.subplot(3, 2, 3)
plt.plot(alpha, error_rel_linear, 'r-', linewidth=2, label='Eroare relativa liniara')
plt.plot(alpha, error_rel_pade, 'g-', linewidth=2, label='Eroare relativa Pade')
plt.title('Eroarea relativa')
plt.xlabel('α [rad]')
plt.ylabel('Eroare relativa')
plt.grid(True, alpha=0.3)
plt.legend()
plt.yscale('log')

# zoom pe regiunea cu valori mici
alpha_small = np.linspace(-0.5, 0.5, 500)
sin_alpha_small = np.sin(alpha_small)
approx_linear_small = alpha_small
approx_pade_small = (alpha_small - (7 / 60) * alpha_small ** 3) / (1 + alpha_small ** 2 / 20)

plt.subplot(3, 2, 4)
plt.plot(alpha_small, sin_alpha_small, 'b-', linewidth=3, label='sin(α)')
plt.plot(alpha_small, approx_linear_small, 'r--', linewidth=2, label='α')
plt.plot(alpha_small, approx_pade_small, 'g--', linewidth=2, label='Pade [3/2]')
plt.title('Zoom: α ∈ [-0.5, 0.5] rad')
plt.xlabel('α [rad]')
plt.ylabel('Valoare')
plt.grid(True, alpha=0.3)
plt.legend()

# eroare absoluta pe axa logaritmica completa
plt.subplot(3, 2, 5)
plt.semilogy(alpha, error_linear, 'r-', linewidth=2, label='Eroare liniara')
plt.semilogy(alpha, error_pade, 'g-', linewidth=2, label='Eroare Pade')
plt.title('Eroare absoluta (axa Y logaritmica)')
plt.xlabel('α [rad]')
plt.ylabel('|Eroare| (log)')
plt.grid(True, alpha=0.3)
plt.legend()

# comparatie performante
plt.subplot(3, 2, 6)
x_ticks = np.array([0.1, 0.2, 0.5, 1.0])
y_linear = [np.abs(np.sin(x) - x) for x in x_ticks]
y_pade = [np.abs(np.sin(x) - (x - (7 / 60) * x ** 3) / (1 + x ** 2 / 20)) for x in x_ticks]

x_pos = np.arange(len(x_ticks))
plt.bar(x_pos - 0.2, y_linear, 0.4, label='Aproximare liniara', alpha=0.7)
plt.bar(x_pos + 0.2, y_pade, 0.4, label='Aproximare Pade', alpha=0.7)
plt.xticks(x_pos, [f'{x:.1f}' for x in x_ticks])
plt.title('Eroare pentru valori specifice ale lui α')
plt.xlabel('α [rad]')
plt.ylabel('Eroare absoluta')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exercitiul8_aproximari.png', dpi=150, bbox_inches='tight')

