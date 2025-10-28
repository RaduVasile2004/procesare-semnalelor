import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

# (a) 400 Hz cu 1600 de esantioane
fs_a = 1600
t_a = np.arange(1600) / fs_a
freq_a = 400
signal_a = np.sin(2 * np.pi * freq_a * t_a)

# (b) 800 Hz care dureaza 3 secunde
duration_b = 3
fs_b = 8000
t_b = np.arange(0, duration_b, 1/fs_b)
freq_b = 800
signal_b = np.sin(2 * np.pi * freq_b * t_b)

# (c) sawtooth 240 Hz
duration_c = 2
fs_c = 8000
t_c = np.arange(0, duration_c, 1/fs_c)
freq_c = 240
signal_c = 2 * (t_c * freq_c - np.floor(0.5 + t_c * freq_c))

# (d) square 300 Hz
duration_d = 2
fs_d = 8000
t_d = np.arange(0, duration_d, 1/fs_d)
freq_d = 300
signal_d = np.sign(np.sin(2 * np.pi * freq_d * t_d))

print("Ascultarea semnalelor generate")

# sinusoidal 400 Hz
print("\n1. Semnal sinusoidal 400 Hz (1 secunda)")
sd.play(signal_a, fs_a)
sd.wait()

# sinusoidal 800 Hz
print("2. Semnal sinusoidal 800 Hz (3 secunde)")
sd.play(signal_b, fs_b)
sd.wait()

# sawtooth 240 Hz
print("3. Semnal sawtooth 240 Hz (2 secunde)")
sd.play(signal_c, fs_c)
sd.wait()

#square 300 Hz
print("4. Semnal square 300 Hz (2 secunde)")
sd.play(signal_d, fs_d)
sd.wait()

# normalizare semnal
signal_d_normalized = signal_d / np.max(np.abs(signal_d))

# fisier WAV
wavfile.write('square_300hz.wav', fs_d, (signal_d_normalized * 32767).astype(np.int16))


# Verificare incarcare fisier WAV
fs_loaded, signal_loaded = wavfile.read('square_300hz.wav')

print(f"Frecventa de esantionare incarcata: {fs_loaded} Hz")
print(f"Dimensiune semnal incarcat: {signal_loaded.shape}")
print(f"Tip date semnal incarcat: {signal_loaded.dtype}")

# Reproducere semnal incarcat
print("Redare semnal incarcat din fisier...")
sd.play(signal_loaded, fs_loaded)
sd.wait()

# Verificare vizuala a semnalului salvat si incarcat
plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t_d[:1000], signal_d_normalized[:1000], 'm-', linewidth=1.5)
plt.title('Semnal square 300 Hz original (primele 1000 esantioane)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
# Convertire in float pentru plot
signal_loaded_float = signal_loaded.astype(np.float32) / 32767.0
t_loaded = np.arange(len(signal_loaded_float[:1000])) / fs_loaded
plt.plot(t_loaded, signal_loaded_float[:1000], 'c-', linewidth=1.5)
plt.title('Semnal square 300 Hz incarcat din fisier WAV (primele 1000 esantioane)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.savefig('verificare_wav.pdf', dpi=300, bbox_inches='tight')
print("\nGrafic de verificare salvat ca 'verificare_wav.pdf'")
