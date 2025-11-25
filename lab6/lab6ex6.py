import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, filtfilt
import matplotlib
matplotlib.use('Agg')

#a
df = pd.read_csv('Train.csv')
df['Datetime'] = pd.to_datetime(df['Datetime'], dayfirst=True)
df = df.sort_values('Datetime')
x = df['Count'].values[:72]

#b
window_sizes = [5, 9, 13, 17]
plt.figure(figsize=(12, 6))
plt.plot(x, label='Original')
for w in window_sizes:
    filtered = np.convolve(x, np.ones(w), 'valid') / w
    plt.plot(range(w-1, len(x)), filtered, label=f'w={w}')
plt.legend()
plt.grid(True)
plt.savefig('ex6b.png')
plt.close()

#c
fs = 1/3600
f_nyquist = fs / 2
f_cutoff = 1/(8*3600)
Wn = f_cutoff / f_nyquist
print(f"Frecventa taiere: {f_cutoff:.6f} Hz")
print(f"Frecventa normalizata: {Wn:.6f}")

#d
b_butter, a_butter = butter(5, Wn, btype='low')
b_cheby, a_cheby = cheby1(5, 5, Wn, btype='low')
print("Filtrele au fost proiectate")