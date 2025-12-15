import numpy as np
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import warnings
warnings.filterwarnings('ignore')

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

max_horizon = 20
e = np.zeros_like(y)
for i in range(len(y)):
    start = max(0, i - max_horizon + 1)
    window_mean = np.mean(y[start:i+1])
    e[i] = y[i] - window_mean


model = auto_arima(y,
                   start_p=0, max_p=8,
                   start_q=0, max_q=8,
                   d=0,  # no differencing
                   seasonal=False,
                   trace=False,
                   error_action='ignore',
                   suppress_warnings=True)

optimal_p = model.order[0]
optimal_q = model.order[2]

print(f"\nOptimal parameters found: p={optimal_p}, q={optimal_q}")
print(f"Model AIC: {model.aic():.2f}")

y_hat = model.fittedvalues()
residuals = y - y_hat

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(t, y, label='Original', color='blue', alpha=0.7, linewidth=1)
axes[0].plot(t, y_hat, label=f'ARMA({optimal_p},{optimal_q})', color='red', alpha=0.8)
axes[0].set_ylabel('Value')
axes[0].legend()
axes[0].set_title(f'ARMA({optimal_p},{optimal_q}) Model')

axes[1].plot(t, e, label=f'Errors e[i] (horizon={max_horizon})', color='green', alpha=0.7)
axes[1].axhline(y=0, color='black', linestyle='--', linewidth=0.5)
axes[1].set_xlabel('Time (t)')
axes[1].set_ylabel('Error')
axes[1].legend()

plt.tight_layout()
plt.savefig('lab9pb4.png', dpi=300)

print(f"\nModel performance:")
print(f"MSE: {np.mean(residuals**2):.6f}")
print(f"Mean error e[i]: {np.mean(e):.6f}")
print(f"Std error e[i]: {np.std(e):.6f}")