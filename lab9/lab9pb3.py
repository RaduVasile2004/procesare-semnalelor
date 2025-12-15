import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

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

# erori
q = 5  # orizont

e = np.zeros_like(y)
for i in range(len(y)):
    start = max(0, i - q + 1)
    window_mean = np.mean(y[start:i+1])
    e[i] = y[i] - window_mean

model = ARIMA(y, order=(0, 0, q))
result = model.fit()

mu = result.params[0]
theta = result.params[1:]

print(f"MA({q}) Model Parameters:")
print(f"mu (constant): {mu:.6f}")
for i in range(q):
    print(f"theta{i+1}: {theta[i]:.6f}")

y_hat = np.zeros_like(y)
for i in range(len(y)):
    if i == 0:
        y_hat[i] = mu
    else:
        ma_sum = mu
        for lag in range(1, min(q, i) + 1):
            ma_sum += theta[lag-1] * e[i - lag]
        y_hat[i] = ma_sum


fig, axes = plt.subplots(2, 1, figsize=(12, 8))


axes[0].plot(t, y, label='Original series', color='blue', alpha=0.7, linewidth=1)
axes[0].plot(t, y_hat, label=f'MA({q}) model', color='red', alpha=0.8, linewidth=1.5)
axes[0].set_ylabel('Value')
axes[0].legend()
axes[0].set_title(f'MA({q}) Model - Original vs Predicted')

axes[1].plot(t, e, label=f'Errors e[i] (deviation from mean, q={q})', color='green', alpha=0.7)
axes[1].axhline(y=0, color='black', linestyle='--', linewidth=0.5)
axes[1].set_xlabel('Time (t)')
axes[1].set_ylabel('Error')
axes[1].legend()
axes[1].set_title('Errors used in MA model')

plt.tight_layout()
plt.savefig('lab9pb3.png', dpi=300)

print(f"\nMA({q}) Model Fit:")
print(f"MSE: {np.mean((y - y_hat)**2):.6f}")
print(f"Mean of errors e[i]: {np.mean(e):.6f}")
print(f"Std of errors e[i]: {np.std(e):.6f}")