import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
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

p = 5

ar_model = ARIMA(y, order=(p, 0, 0))
ar_result = ar_model.fit()

ar_coeff = ar_result.params
print(f"AR({p}) Model Parameters:")
print(f"Constant: {ar_coeff[0]:.6f}")
for i in range(1, len(ar_coeff)):
    if i <= p:
        print(f"phi{i}: {ar_coeff[i]:.6f}")

y_hat = ar_result.fittedvalues
residuals = y - y_hat

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(t, y, label='Original', color='blue', alpha=0.7, linewidth=1)
axes[0].plot(t, y_hat, label=f'AR({p})', color='red', alpha=0.8, linewidth=1.5)
axes[0].set_ylabel('Value')
axes[0].legend()
axes[0].set_title(f'AR({p}) Model')

axes[1].plot(t, residuals, label='Residuals', color='purple', alpha=0.7)
axes[1].axhline(y=0, color='black', linestyle='--', linewidth=0.5)
axes[1].set_xlabel('Time (t)')
axes[1].set_ylabel('Residual')
axes[1].legend()
axes[1].set_title('Model Residuals')

plt.tight_layout()
plt.savefig('lab10pb2.png', dpi=300)

print(f"\nAR({p}) Model Statistics:")
print(f"MSE: {np.mean(residuals**2):.6f}")