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

def autocorr(y, lag_max=200):
    y_mean = np.mean(y)
    y_var = np.var(y)
    n = len(y)
    corr = [1.0]
    for lag in range(1, lag_max + 1):
        numerator = np.sum((y[:-lag] - y_mean) * (y[lag:] - y_mean))
        denominator = (n - lag) * y_var
        corr.append(numerator / denominator)
    return np.array(corr)

lag_max = 200
acf = autocorr(y, lag_max)
lags = np.arange(lag_max + 1)

plt.figure(figsize=(12, 5))
plt.stem(lags, acf, linefmt='blue', markerfmt='bo', basefmt=" ")
plt.axhline(y=0, color='black', linewidth=0.5)
plt.title('Autocorelatie - Serie de timp')
plt.xlabel('Lag (k)')
plt.ylabel('Autocorelatie R(k)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('lab8pb1b.png')
plt.close()

print("First 10 ACF values:", acf[:10])