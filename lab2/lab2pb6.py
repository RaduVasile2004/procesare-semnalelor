import numpy as np
import matplotlib.pyplot as plt


fs = 1000


t_end = 2 * (1/(fs/4))  # 2 perioade pentru fs/4
t = np.linspace(0, t_end, int(fs * t_end))

print(f"\nTimp de simulare: {t_end:.3f} s")
print(f"Număr de eșantioane: {len(t)}")

# Semnalele cerute

# (a) f = fs/2
f_a = fs / 2
semnal_a = np.sin(2 * np.pi * f_a * t)
print(f"(a) f = fs/2 = {f_a} Hz")

# (b) f = fs/4
f_b = fs / 4
semnal_b = np.sin(2 * np.pi * f_b * t)
print(f"(b) f = fs/4 = {f_b} Hz")

# (c) f = 0 Hz
f_c = 0
semnal_c = np.sin(2 * np.pi * f_c * t)
print(f"(c) f = 0 Hz")

plt.figure(figsize=(12, 10))

# (a): f = fs/2
plt.subplot(3, 1, 1)
plt.plot(t, semnal_a, 'b-', linewidth=2, marker='o', markersize=3)
plt.title(f'(a) Semnal sinusoidal - f = fs/2 = {f_a} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-1.2, 1.2)

# (b): f = fs/4
plt.subplot(3, 1, 2)
plt.plot(t, semnal_b, 'r-', linewidth=2, marker='s', markersize=3)
plt.title(f'(b) Semnal sinusoidal - f = fs/4 = {f_b} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-1.2, 1.2)

# (c): f = 0 Hz
plt.subplot(3, 1, 3)
plt.plot(t, semnal_c, 'g-', linewidth=2)
plt.title(f'(c) Semnal sinusoidal - f = 0 Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-1.2, 1.2)

plt.tight_layout()
plt.savefig('exercitiul6_semnale.png', dpi=150, bbox_inches='tight')

# Analiza detaliată a semnalelor
print("\n" + "="*70)
print("ANALIZA SI OBSERVATII:")
print("="*70)

# (a) f = fs/2
print(f"\n(a) f = fs/2 = {f_a} Hz:")
print(f"  - Perioada teoretica: T = 1/f = {1/f_a:.6f} s")
print(f"  - Esantioane per perioada: fs/f = {fs/f_a:.1f}")
print(f"  - Valori unice ale semnalului: {len(np.unique(np.round(semnal_a[:20], 8)))} in primele 20 esantioane")
print("  → OBSERVATIE: Semnalul alterneaza intre -1 si 1 (cel mai rapid semnal posibil la aceasta fs)")

# (b) f = fs/4
print(f"\n(b) f = fs/4 = {f_b} Hz:")
print(f"  - Perioada teoretica: T = 1/f = {1/f_b:.6f} s")
print(f"  - Esantioane per perioada: fs/f = {fs/f_b:.1f}")
print(f"  - Secventa valorilor in prima perioada: {np.round(semnal_b[:int(fs/f_b)], 4)}")
print("  → OBSERVATIE: Semnalul are 4 esantioane per perioada (sinus complet esantionat)")

# (c) f = 0 Hz
print(f"\n(c) f = 0 Hz:")
print(f"  - Valoare constanta a semnalului: {semnal_c[0]}")
print(f"  - Toate esantioanele sunt identice: {np.all(semnal_c == semnal_c[0])}")
print("  → OBSERVATIE: Semnal constant (valoare 0) - nu exista oscilatie")
