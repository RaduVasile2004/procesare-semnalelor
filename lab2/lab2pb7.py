import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului original
fs_original = 1000
f_semnal = 50
A = 1
duration = 0.1

# semnal original
t_original = np.linspace(0, duration, int(fs_original * duration))
semnal_original = A * np.sin(2 * np.pi * f_semnal * t_original)

print(f"Parametrii initiali:")
print(f"  - Frecventa de esantionare: {fs_original} Hz")
print(f"  - Frecventa semnalului: {f_semnal} Hz")
print(f"  - Numar de esantioane original: {len(semnal_original)}")

# (a) Decimare incepand cu primul element (pastrand al 4-lea element)
factor_decimare = 4
fs_decimat_a = fs_original // factor_decimare

# (index 0)
indici_decimare_a = range(0, len(semnal_original), factor_decimare)
t_decimat_a = t_original[indici_decimare_a]
semnal_decimat_a = semnal_original[indici_decimare_a]

print(f"\n(a) Decimare incepand cu primul element:")
print(f"  - Factor de decimare: {factor_decimare}")
print(f"  - Frecventa de esantionare dupa decimare: {fs_decimat_a} Hz")
print(f"  - Numar de esantioane dupa decimare: {len(semnal_decimat_a)}")

# (b) Decimare incepand cu al doilea element
indici_decimare_b = range(1, len(semnal_original), factor_decimare)
t_decimat_b = t_original[indici_decimare_b]
semnal_decimat_b = semnal_original[indici_decimare_b]

print(f"\n(b) Decimare incepand cu al doilea element:")
print(f"  - Factor de decimare: {factor_decimare}")
print(f"  - Frecventa de esantionare dupa decimare: {fs_decimat_a} Hz")
print(f"  - Numar de esantioane dupa decimare: {len(semnal_decimat_b)}")

plt.figure(figsize=(14, 10))

# Semnalul original
plt.subplot(3, 1, 1)
plt.plot(t_original, semnal_original, 'b-', linewidth=2, label='Semnal original')
plt.title(f'Semnal Original - fs = {fs_original} Hz, f = {f_semnal} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

#Decimare incepand cu primul element
plt.subplot(3, 1, 2)
plt.plot(t_original, semnal_original, 'b-', linewidth=1, alpha=0.5, label='Original')
plt.plot(t_decimat_a, semnal_decimat_a, 'ro-', linewidth=2, markersize=6, label='Decimat (incepand cu primul)')
plt.title(f'(a) Decimare incepand cu primul element - fs = {fs_decimat_a} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

# Decimare incepand cu al doilea element
plt.subplot(3, 1, 3)
plt.plot(t_original, semnal_original, 'b-', linewidth=1, alpha=0.5, label='Original')
plt.plot(t_decimat_b, semnal_decimat_b, 'go-', linewidth=2, markersize=6, label='Decimat (incepand cu al doilea)')
plt.title(f'(b) Decimare incepand cu al doilea element - fs = {fs_decimat_a} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('exercitiul7_decimare.png', dpi=150, bbox_inches='tight')

print("\n" + "="*70)
print("ANALIZA SI OBSERVATII:")
print("="*70)

#(a)
print(f"\n(a) Decimare incepand cu primul element:")
print(f"  - Esantioane pastrate: {len(semnal_decimat_a)}")
print(f"  - Valori esantioane: {np.round(semnal_decimat_a[:8], 4)}")
faza_a = np.angle(np.exp(1j * 2 * np.pi * f_semnal * t_decimat_a))
print(f"  - Faze relative: {np.round(faza_a[:8] / (2*np.pi), 4)} (in perioade)")

# (b)
print(f"\n(b) Decimare incepand cu al doilea element:")
print(f"  - Esantioane pastrate: {len(semnal_decimat_b)}")
print(f"  - Valori esantioane: {np.round(semnal_decimat_b[:8], 4)}")
faza_b = np.angle(np.exp(1j * 2 * np.pi * f_semnal * t_decimat_b))
print(f"  - Faze relative: {np.round(faza_b[:8] / (2*np.pi), 4)} (in perioade)")

# Comparatie
print(f"\nCOMPARATIE INTRE CELE DOUA DECIMARI:")
print(f"  - Ambele au aceeasi frecventa de esantionare: {fs_decimat_a} Hz")
print(f"  - Ambele pastreaza acelasi numar de esantioane: {len(semnal_decimat_a)}")
print(f"  - Diferenta: faza relativa a esantioanelor")


print("\n" + "="*70)
print("CONCLUZII FINALE:")
print("1. Decimarea reduce frecventa de esantionare de la 1000 Hz la 250 Hz")
print("2. Ambele decimari pastreaza acelasi numar de esantioane")
print("3. Diferenta consta in faza de esantionare:")
print("   - (a) Esantioneaza la momente precise ale perioadei")
print("   - (b) Esantioneaza cu o deplasare de faza (1/4 din perioada de esantionare)")
print("4. Ambele semnale decimate respecta teorema Nyquist")