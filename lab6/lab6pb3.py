import numpy as np

N = 5
p = np.random.randint(0, 10, N+1)
q = np.random.randint(0, 10, N+1)

print("Polinom p:", p)
print("Polinom q:", q)

r_direct = np.zeros(2*N + 1)
for i in range(len(p)):
    for j in range(len(q)):
        r_direct[i+j] += p[i] * q[j]

print("Produs direct r:", r_direct)

P = np.fft.fft(p, 2*N+1)
Q = np.fft.fft(q, 2*N+1)
R = P * Q
r_fft = np.real(np.fft.ifft(R))

print("Produs FFT r:", r_fft)

print("Diferenta:", np.max(np.abs(r_direct - r_fft)))