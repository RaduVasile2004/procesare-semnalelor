import numpy as np

# eliminarea componentei continue
data = np.genfromtxt('Train.csv', delimiter=',')
x = data[:, 2]
x_clean = np.nan_to_num(x, nan=0.0)
componenta_continua = np.mean(x_clean)
x_fara_dc = x_clean - componenta_continua


N = len(x_fara_dc)
Fs = 1

# trans fourier semn fara comp cont
X = np.fft.fft(x_fara_dc)
X_mod = np.abs(X) / N
X_mod_jumatate = X_mod[:N // 2]
f = Fs * np.linspace(0, N // 2, N // 2) / N

#cele 4 val max
indices_sortati = np.argsort(X_mod_jumatate)[::-1]

print("Primele 4 frecvente principale (excluzand componenta continua):\n")

for i in range(4):
    idx = indices_sortati[i]
    frecventa = f[idx]
    amplitudine = X_mod_jumatate[idx]

    perioada_ore = 1 / frecventa if frecventa > 0 else float('inf')
    perioada_zile = perioada_ore / 24

    print(f"Rank {i + 1}:")
    print(f"  Frecventa: {frecventa:.6f} cicluri/ora")
    print(f"  Amplitudine: {amplitudine:.4f}")
    print(f"  Perioada: {perioada_ore:.1f} ore ({perioada_zile:.2f} zile)")

    if abs(perioada_ore - 24) < 2:
        fenomen = "Ciclu zilnic (trafic zi/noapte)"
    elif abs(perioada_ore - 168) < 10:  # 7 zile × 24 ore
        fenomen = "Ciclu saptamanal (lucratoare/weekend)"
    elif abs(perioada_ore - 12) < 2:
        fenomen = "Ciclu semizilnic (ore de varf dimineata/seara)"
    elif perioada_zile > 50:
        fenomen = "Ciclu sezonier/anual"
    elif perioada_ore < 10:
        fenomen = "Ciclu orar/pe termen scurt"
    else:
        fenomen = "Componenta periodica"

    print(f"  Fenomen asociat: {fenomen}")
    print()