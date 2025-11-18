import numpy as np

data = np.genfromtxt('Train.csv', delimiter=',')
x = data[:, 2]
x_clean = np.nan_to_num(x, nan=0.0)

componenta_continua = np.mean(x_clean)

if abs(componenta_continua) > 1e-6:
    print("Semnalul PREZINTA componenta continua")
    x_fara_dc = x_clean - componenta_continua
else:
    print("Semnalul NU prezinta componenta continua")
    x_fara_dc = x_clean

print(f"Valoarea componentei continue: {componenta_continua:.2f}")