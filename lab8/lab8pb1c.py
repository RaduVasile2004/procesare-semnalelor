import numpy as np
import matplotlib.pyplot as plt

N = 1000
t = np.arange(N)

a, b, c = 0.0001, 0.02, 10
trend = a * t**2 + b * t + c

f1, f2 = 0.05, 0.1
A1, A2 = 5, 3
phi = np.pi / 4
season = A1 * np.sin(2 * np.pi * f1 * t) + A2 * np.sin(2 * np.pi * f2 * t + phi)

sigma = 1.0
np.random.seed(42)
noise = np.random.normal(0, sigma, N)

y = trend + season + noise

p = 10

X = np.zeros((N - p, p))
for i in range(p):
    X[:, i] = y[i:N - p + i]

Y = y[p:]

theta = np.linalg.lstsq(X, Y, rcond=None)[0]

predictions = np.zeros(N)
predictions[:p] = y[:p]
for i in range(p, N):
    predictions[i] = np.dot(theta, y[i - p:i])

plt.figure(figsize=(14, 6))
plt.plot(t, y, label='Original', color='blue', alpha=0.7)
plt.plot(t, predictions, label='Predictii AR(10)', color='red', linestyle='--')
plt.title('Model AR(p) - Predictii')
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('lab8pb1c.png')
plt.close()

print("Parametri AR(10):", theta)
print("MAE:", np.mean(np.abs(y - predictions)))