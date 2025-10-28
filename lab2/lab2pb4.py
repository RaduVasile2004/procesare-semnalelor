import numpy as np
import matplotlib.pyplot as plt

# Parametrii comuni
fs = 1000  # Frecventa de esantionare [Hz]
t_start = 0
t_end = 2  # 2 secunde
t = np.linspace(t_start, t_end, int(fs * (t_end - t_start)))

# Semnal 1: Sinusoidal
print("Generare semnal sinusoidal")
f1 = 2  # Frecvența [Hz]
A1 = 1  # Amplitudine
phi1 = 0  # Faza
semnal_sinus = A1 * np.sin(2 * np.pi * f1 * t + phi1)

# Semnal 2: Sawtooth
print("Generare semnal sawtooth")
f2 = 1  # Frecventa fundamentala [Hz]
A2 = 0.8  # Amplitudine
semnal_sawtooth = A2 * (2 * (t * f2 - np.floor(0.5 + t * f2)))

# Suma semnalelor
print("Calculare suma")
suma_semnalelor = semnal_sinus + semnal_sawtooth

# Afisare grafica
plt.figure(figsize=(12, 10))

# Subplot 1: Semnal sinusoidal
plt.subplot(3, 1, 1)
plt.plot(t, semnal_sinus, 'b-', linewidth=2)
plt.title('Semnal Sinusoidal')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-2, 2)

# Subplot 2: Semnal sawtooth
plt.subplot(3, 1, 2)
plt.plot(t, semnal_sawtooth, 'r-', linewidth=2)
plt.title('Semnal Sawtooth')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-2, 2)

# Subplot 3: Suma semnalelor
plt.subplot(3, 1, 3)
plt.plot(t, suma_semnalelor, 'g-', linewidth=2)
plt.title('Suma Semnalelor')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.ylim(-2, 2)

plt.tight_layout()
plt.savefig('exercitiul4_semnale.png', dpi=150, bbox_inches='tight')

#
# # Afișare informații despre semnale
# print("\n" + "="*60)
# print("INFORMAȚII DESPRE SEMNALE:")
# print(f"Semnal sinusoidal:")
# print(f"  - Amplitudine: {A1}")
# print(f"  - Frecvență: {f1} Hz")
# print(f"  - Perioadă: {1/f1:.2f} s")
#
# print(f"\nSemnal sawtooth:")
# print(f"  - Amplitudine: {A2}")
# print(f"  - Frecvență: {f2} Hz")
# print(f"  - Perioadă: {1/f2:.2f} s")
#
# print(f"\nSuma semnalelor:")
# print(f"  - Amplitudine maximă: {np.max(suma_semnalelor):.3f}")
# print(f"  - Amplitudine minimă: {np.min(suma_semnalelor):.3f}")
# print(f"  - Valoare medie: {np.mean(suma_semnalelor):.3f}")
#
# # Afișare câteva valori pentru demonstrație
# print("\n" + "="*60)
# print("EXEMPLU DE VALORI:")
# print("t[s]   | Sinus    | Sawtooth | Suma     ")
# print("-" * 45)
# momente_afisare = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
# for moment in momente_afisare:
#     idx = np.argmin(np.abs(t - moment))
#     print(f"{t[idx]:.3f} | {semnal_sinus[idx]:>8.3f} | {semnal_sawtooth[idx]:>9.3f} | {suma_semnalelor[idx]:>8.3f}")
#
# print("\n✓ Semnalele au fost generate și adunate cu succes!")
# print("✓ Rezultatele au fost salvate în fișierul PNG")