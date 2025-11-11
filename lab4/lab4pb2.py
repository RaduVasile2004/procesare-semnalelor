import numpy as np
import matplotlib.pyplot as plt

# semnal original
f_original = 5.0
A = 1.0           # amplitudine
phi = 0.0         # faza

# frecventa de eșantionare sub-Nyquist
f_s = 8.0         #ar trebui > 2*5 = 10Hz

# t semn continue
t_continuous = np.linspace(0, 1, 1000)

# t esantioane
t_samples = np.arange(0, 1, 1/f_s)
N_samples = len(t_samples)

print(f"Frecventa semnalului original: {f_original} Hz")
print(f"Frecventa de esantionare: {f_s} Hz")
print(f"Frecventa Nyquist: {f_s/2} Hz")
print(f"Numar de esantioane: {N_samples}")

# semn original continuu
signal_original = A * np.cos(2 * np.pi * f_original * t_continuous + phi)

# esantioane semn original
samples_original = A * np.cos(2 * np.pi * f_original * t_samples + phi)

# semn alternative care produc aceleasi esantioane
# cos(2πf₁nT) = cos(2πf₂nT) pentru f₂ = f₁ ± k·f_s

# primul semn (aliasing)
f_alias1 = f_original - f_s  # 5 - 8 = -3
signal_alias1 = A * np.cos(2 * np.pi * abs(f_alias1) * t_continuous + phi)

# al doilea semn (aliasing)
f_alias2 = f_original + f_s  # 5 + 8 = 13
signal_alias2 = A * np.cos(2 * np.pi * f_alias2 * t_continuous + phi)

print(f"\nSemnale alternative care produc aceleași esantioane:")
print(f"f_alias1 = {f_alias1} Hz (echivalent cu {abs(f_alias1)} Hz)")
print(f"f_alias2 = {f_alias2} Hz")

# verificam ca toate semnalele produc aceleasi esantioane
samples_alias1 = A * np.cos(2 * np.pi * abs(f_alias1) * t_samples + phi)
samples_alias2 = A * np.cos(2 * np.pi * f_alias2 * t_samples + phi)

print(f"\nVerificare esantioane identice:")
print(f"Toate identice: {np.allclose(samples_original, samples_alias1) and np.allclose(samples_original, samples_alias2)}")

plt.figure(figsize=(14, 10))

# Subplot 1: Semnalul original si esantioanele
plt.subplot(3, 1, 1)
plt.plot(t_continuous, signal_original, 'b-', linewidth=2, label=f'Semnal original (f={f_original} Hz)')
plt.stem(t_samples, samples_original, linefmt='r-', markerfmt='ro', basefmt=' ',
         label=f'Eșantioane (f_s={f_s} Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Semnalul Original și Eșantioanele')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: Primul semnal alternativ
plt.subplot(3, 1, 2)
plt.plot(t_continuous, signal_alias1, 'g-', linewidth=2, label=f'Semnal alternativ 1 (f={abs(f_alias1)} Hz)')
plt.stem(t_samples, samples_alias1, linefmt='r-', markerfmt='ro', basefmt=' ',
         label='Aceleași eșantioane')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Primul Semnal Alternativ care Produce Aceleași Eșantioane')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 3: Al doilea semnal alternativ
plt.subplot(3, 1, 3)
plt.plot(t_continuous, signal_alias2, 'm-', linewidth=2, label=f'Semnal alternativ 2 (f={f_alias2} Hz)')
plt.stem(t_samples, samples_alias2, linefmt='r-', markerfmt='ro', basefmt=' ',
         label='Aceleași eșantioane')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Al Doilea Semnal Alternativ care Produce Aceleași Eșantioane')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fenomen_aliasing.pdf', dpi=300, bbox_inches='tight')
plt.close()

