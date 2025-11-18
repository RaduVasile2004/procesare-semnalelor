import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


data = np.genfromtxt('Train.csv', delimiter=',')
x = data[:, 2]  # coloana cu numarul de masini
x_clean = np.nan_to_num(x, nan=0.0)

# Param semnal
N = len(x_clean)
Fs = 1

X = np.fft.fft(x_clean)

# calc modul si normalizarea
X_mod = np.abs(X) / N

# jumatate din spectru
X_mod_jumatate = X_mod[:N//2]

# v de frecv
f = Fs * np.linspace(0, N//2, N//2) / N

plt.figure(figsize=(12, 6))
plt.plot(f, X_mod_jumatate)
plt.title('Modulul Transformatei Fourier a semnalului de trafic')
plt.xlabel('Frecventa [cicluri/ora]')
plt.ylabel('Modul |X(f)| / N')
plt.grid(True)
plt.savefig('ex1d_transformata_fourier.pdf')
print("Graficul a fost salvat ca 'ex1d_transformata_fourier.pdf'")