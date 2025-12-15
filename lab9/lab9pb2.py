import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from scipy.signal import find_peaks
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

#exp simpla
def exp_smooth(series, alpha):
    result = np.zeros_like(series, dtype=float)
    result[0] = series[0]
    for i in range(1, len(series)):
        result[i] = alpha * series[i] + (1 - alpha) * result[i-1]
    return result

alpha_fix = 0.3
smoothed_fix = exp_smooth(y, alpha_fix)

#alp optim
alphas = np.linspace(0.01, 0.99, 50)
mse_list = []
for a in alphas:
    smoothed = exp_smooth(y, a)
    mse = np.mean((y - smoothed)**2)
    mse_list.append(mse)

alpha_opt = alphas[np.argmin(mse_list)]
smoothed_opt = exp_smooth(y, alpha_opt)

print(f"Alpha fixed: {alpha_fix}")
print(f"Alpha optimal: {alpha_opt:.3f}")

#exp dubla
def holt_smooth(series, alpha, beta):
    n = len(series)
    l = np.zeros(n)
    b = np.zeros(n)
    l[0] = series[0]
    b[0] = series[1] - series[0]
    for i in range(1, n):
        l[i] = alpha * series[i] + (1 - alpha) * (l[i-1] + b[i-1])
        b[i] = beta * (l[i] - l[i-1]) + (1 - beta) * b[i-1]
    return l, b

# alpha beta optim
best_mse = float('inf')
best_ab = (0.3, 0.1)
for a in np.linspace(0.1, 0.9, 9):
    for b in np.linspace(0.05, 0.5, 10):
        l_smooth, b_smooth = holt_smooth(y, a, b)
        mse = np.mean((y - l_smooth)**2)
        if mse < best_mse:
            best_mse = mse
            best_ab = (a, b)

alpha_holt, beta_holt = best_ab
l_opt, b_opt = holt_smooth(y, alpha_holt, beta_holt)

print(f"Holt optimal: alpha={alpha_holt:.3f}, beta={beta_holt:.3f}")

# 4. exp tripla
peaks, _ = find_peaks(season, distance=10)
if len(peaks) > 1:
    m_est = int(np.mean(np.diff(peaks)))
else:
    m_est = int(1 / f1)

m_est = max(4, m_est)

model_hw = ExponentialSmoothing(
    y,
    seasonal_periods=m_est,
    trend='add',
    seasonal='add',
    use_boxcox=False
)
fit_hw = model_hw.fit(optimized=True)
smoothed_hw = fit_hw.fittedvalues

print(f"Holt-Winters: m={m_est}, alpha={fit_hw.params['smoothing_level']:.3f}, "
      f"beta={fit_hw.params['smoothing_trend']:.3f}, "
      f"gamma={fit_hw.params['smoothing_seasonal']:.3f}")

fig, axes = plt.subplots(5, 1, figsize=(14, 12), sharex=True)

axes[0].plot(t, y, label='Original', color='blue', alpha=0.7)
axes[0].set_ylabel('Original')
axes[0].legend()

axes[1].plot(t, smoothed_fix, label=f'Exp Smooth alpha={alpha_fix}', color='orange')
axes[1].set_ylabel('Exp Smooth (fixed)')
axes[1].legend()

axes[2].plot(t, smoothed_opt, label=f'Exp Smooth alpha={alpha_opt:.3f} (optimal)', color='red')
axes[2].set_ylabel('Exp Smooth (optimal)')
axes[2].legend()

axes[3].plot(t, l_opt, label=f'Holt alpha={alpha_holt:.3f}, beta={beta_holt:.3f}', color='green')
axes[3].set_ylabel('Holt (double)')
axes[3].legend()

axes[4].plot(t, smoothed_hw, label='Holt-Winters (triple)', color='purple')
axes[4].set_ylabel('Holt-Winters')
axes[4].legend()
axes[4].set_xlabel('Time (t)')

plt.suptitle('Exercise 2 - Exponential Smoothing: Simple, Double, Triple')
plt.tight_layout()
plt.savefig('lab9pb2.png', dpi=300)

plt.close(fig)