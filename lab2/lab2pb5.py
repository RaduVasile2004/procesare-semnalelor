import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt



# Parametrii comuni
fs = 44100
duration = 2

# frecventa joasa (200 Hz)
t1 = np.arange(0, duration, 1/fs)
freq1 = 200
signal1 = np.sin(2 * np.pi * freq1 * t1)

# frecventa inalta (800 Hz)
t2 = np.arange(0, duration, 1/fs)
freq2 = 800
signal2 = np.sin(2 * np.pi * freq2 * t2)

# Concatenare semnale
combined_signal = np.concatenate([signal1, signal2])
total_duration = 2 * duration  # 4 secunde total

print("Generare si redare semnale...")
print(f"Semnal 1: {freq1} Hz pentru {duration} secunde")
print(f"Semnal 2: {freq2} Hz pentru {duration} secunde")
print(f"Semnal combinat: {total_duration} secunde total")


print("\nRedare semnal combinat")
print("Ascultati: primul semnal (200 Hz) urmat de al doilea semnal (800 Hz)")
sd.play(combined_signal, fs)
sd.wait()


plt.figure(figsize=(12, 8))

# semnal 1
plt.subplot(3, 1, 1)
plt.plot(t1[:2000], signal1[:2000], 'b-', linewidth=1.5)
plt.title(f'Semnal 1: Sinusoidal {freq1} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# semnal 2
plt.subplot(3, 1, 2)
plt.plot(t2[:2000], signal2[:2000], 'r-', linewidth=1.5)
plt.title(f'Semnal 2: Sinusoidal {freq2} Hz')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)

# Grafic semnal combinat (primele si ultimele parti)
plt.subplot(3, 1, 3)
t_combined = np.arange(len(combined_signal[:4000])) / fs
plt.plot(t_combined, combined_signal[:4000], 'g-', linewidth=1.5)
plt.axvline(x=duration, color='k', linestyle='--', alpha=0.7, label='Tranzitie')
plt.title('Semnal combinat - primele 4 secunde (tranzitie la 2 secunde)')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('semnal_combinat.pdf', dpi=300, bbox_inches='tight')
print("\nGrafic salvat ca 'semnal_combinat.pdf'")

# Observatii
print("\n" + "="*50)
print("OBSERVATII:")
print("="*50)
print("1. SE AUDE CLAR TRANZITIA: Primul semnal (200 Hz) are un sunet mai grav,")
print("   iar al doilea semnal (800 Hz) are un sunet mai ascutit.")
print("2. FORMA DE UNDA ESTE ACEEASI: Ambele sunt semnale sinusoidale,")
print("   dar cu frecvente diferite.")
print("3. DURATA: Fiecare semnal dureaza 2 secunde, totalul fiind 4 secunde.")
print("4. FRECVENTA AFECTEAZA INALTIMEA SUNETULUI: Cu cât frecventa este mai mare,")
print("   cu atat sunetul este mai inalt (mai 'ascutit').")
print("5. TRANZITIA ESTE INSTANTANEE: Nu exista pauza intre semnale,")
print("   trecerea de la unul la altul este imediata.")

#redare separata pentru comparatie
print("\n" + "="*50)
print("COMPARATIE SEMNALE SEPARATE:")
print("="*50)

print("Redare semnal 1 (200 Hz)")
sd.play(signal1, fs)
sd.wait()

print("Redare semnal 2 (800 Hz)")
sd.play(signal2, fs)
sd.wait()
