import numpy as np
import matplotlib
matplotlib.use('Agg')  # Backend care nu da eroare
import matplotlib.pyplot as plt

data = np.genfromtxt('Train.csv', delimiter=',')
x = data[:, 2]
x_clean = np.nan_to_num(x, nan=0.0)

start_sample = 1000

zile_afisare = 30
esantioane_afisare = zile_afisare * 24

x_luna = x_clean[start_sample:start_sample + esantioane_afisare]
t_ore = np.arange(len(x_luna))

plt.figure(figsize=(15, 6))
plt.plot(t_ore, x_luna, linewidth=1)
plt.title(f'Traficul pe o perioada de {zile_afisare} zile (incepand de la esantionul {start_sample})')
plt.xlabel('Ore de la inceputul perioadei')
plt.ylabel('Numar de masini')
plt.grid(True, alpha=0.3)

for i in range(0, len(t_ore), 24):
    if i < len(t_ore):
        ziua_saptamanii = (i // 24) % 7
        zile = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
        culoare = 'red' if ziua_saptamanii in [5, 6] else 'blue'  # Weekend vs lucratoare
        plt.axvline(x=i, color=culoare, linestyle='--', alpha=0.7)
        plt.text(i, plt.ylim()[1] * 0.95, zile[ziua_saptamanii],
                ha='center', va='top', fontweight='bold', color=culoare)

plt.xticks(np.arange(0, len(t_ore)+1, 24))
plt.tight_layout()
plt.savefig('ex1g_trafic_o_luna.pdf', dpi=300, bbox_inches='tight')
