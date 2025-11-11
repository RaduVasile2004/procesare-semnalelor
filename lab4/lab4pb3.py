import numpy as np
import matplotlib.pyplot as plt


f_original = 5.0
A = 1.0
phi = 0.0

# f PESTE Nyquist
f_s = 12.0        # 12 > 2*5 = 10 Hz


t_continuous = np.linspace(0, 1, 1000)


t_samples = np.arange(0, 1, 1/f_s)
N_samples = len(t_samples)

print(f"Frecventa semnalului original: {f_original} Hz")
print(f"Frecventa de esantionare: {f_s} Hz")
print(f"Frecventa Nyquist: {f_s/2} Hz")
print(f"Numar de esantioane: {N_samples}")

# semn original
signal_original = A * np.cos(2 * np.pi * f_original * t_continuous + phi)

# esantioanele semn original
samples_original = A * np.cos(2 * np.pi * f_original * t_samples + phi)


# semn alternative
f_alias1 = 3.0   # Hz
f_alias2 = 13.0  # Hz

signal_alias1 = A * np.cos(2 * np.pi * f_alias1 * t_continuous + phi)
signal_alias2 = A * np.cos(2 * np.pi * f_alias2 * t_continuous + phi)

# esantioanele semn alternative
samples_alias1 = A * np.cos(2 * np.pi * f_alias1 * t_samples + phi)
samples_alias2 = A * np.cos(2 * np.pi * f_alias2 * t_samples + phi)

print(f"\nVerificare esantioane identice:")
print(f"Original vs Alias1: {np.allclose(samples_original, samples_alias1, atol=1e-10)}")
print(f"Original vs Alias2: {np.allclose(samples_original, samples_alias2, atol=1e-10)}")

plt.figure(figsize=(14, 10))

# Subplot 1: Semnalul original și eșantioanele
plt.subplot(3, 1, 1)
plt.plot(t_continuous, signal_original, 'b-', linewidth=2, label=f'Semnal original (f={f_original} Hz)')
plt.stem(t_samples, samples_original, linefmt='r-', markerfmt='ro', basefmt=' ',
         label=f'Eșantioane (f_s={f_s} Hz)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Semnalul Original și Eșantioanele (Eșantionare Corectă)')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 2: Primul semnal alternativ
plt.subplot(3, 1, 2)
plt.plot(t_continuous, signal_alias1, 'g-', linewidth=2, label=f'Semnal alternativ 1 (f={f_alias1} Hz)')
plt.stem(t_samples, samples_alias1, linefmt='r-', markerfmt='ro', basefmt=' ',
         label='Eșantioane diferite!')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Primul Semnal Alternativ - Eșantioane DIFERITE')
plt.legend()
plt.grid(True, alpha=0.3)

# Subplot 3: Al doilea semnal alternativ
plt.subplot(3, 1, 3)
plt.plot(t_continuous, signal_alias2, 'm-', linewidth=2, label=f'Semnal alternativ 2 (f={f_alias2} Hz)')
plt.stem(t_samples, samples_alias2, linefmt='r-', markerfmt='ro', basefmt=' ',
         label='Eșantioane diferite!')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.title('Al Doilea Semnal Alternativ - Eșantioane DIFERITE')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('fara_aliasing_nyquist.pdf', dpi=300, bbox_inches='tight')
plt.close()

