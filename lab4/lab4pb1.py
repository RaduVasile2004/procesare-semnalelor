import numpy as np
import matplotlib.pyplot as plt
import time


# DFT
def dft_manual(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    F = np.exp(-2j * np.pi * k * n / N) / np.sqrt(N)
    return np.dot(F, x) * np.sqrt(N)


# FFT (Cooley-Tukey)
def fft_manual(x):
    N = len(x)
    x = x.astype(complex)

    # N put 2
    if N & (N - 1) != 0:
        raise ValueError("dimensiunea trebuie sa fie putere a lui 2")

    # reordonare biti
    j = 0
    for i in range(1, N):
        bit = N >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            x[i], x[j] = x[j], x[i]

    # FFT
    L = 2
    while L <= N:
        angle = -2j * np.pi / L
        wlen = np.exp(angle)

        for i in range(0, N, L):
            w = 1.0
            for j in range(0, L // 2):
                u = x[i + j]
                v = x[i + j + L // 2] * w
                x[i + j] = u + v
                x[i + j + L // 2] = u - v
                w *= wlen

        L <<= 1

    return x



dimensiuni = [128, 256, 512, 1024, 2048, 4096, 8192]

timp_dft = []
timp_fft_manual = []
timp_numpy_fft = []

print("Masurarea timpilor de executie...")

for N in dimensiuni:
    print(f"Test pentru N = {N}")

    # semnal aleator
    x = np.random.random(N) + 1j * np.random.random(N)

    # DFT
    start_time = time.time()
    result_dft = dft_manual(x)
    end_time = time.time()
    timp_dft.append(end_time - start_time)
    print(f"  DFT manual: {timp_dft[-1]:.6f} s")

    # FFT
    try:
        start_time = time.time()
        result_fft = fft_manual(x.copy())
        end_time = time.time()
        timp_fft_manual.append(end_time - start_time)
        print(f"  FFT manual: {timp_fft_manual[-1]:.6f} s")
    except Exception as e:
        timp_fft_manual.append(np.nan)
        print(f"  FFT manual: Eroare - {e}")

    # numpy.fft.fft 100 iteratii pentru precizie
    num_iterations = 100
    start_time = time.time()
    for _ in range(num_iterations):
        result_numpy = np.fft.fft(x)
    end_time = time.time()
    timp_numpy_fft.append((end_time - start_time) / num_iterations)
    print(f"  numpy.fft.fft: {timp_numpy_fft[-1]:.6f} s")

plt.figure(figsize=(12, 8))

# DFT
plt.plot(dimensiuni, timp_dft, 'ro-', linewidth=2, markersize=8, label='DFT Manual')

# FFT
fft_valid_indices = [i for i, t in enumerate(timp_fft_manual) if not np.isnan(t)]
if fft_valid_indices:
    plt.plot([dimensiuni[i] for i in fft_valid_indices],
             [timp_fft_manual[i] for i in fft_valid_indices],
             'go-', linewidth=2, markersize=8, label='FFT Manual')

# numpy.fft.fft
plt.plot(dimensiuni, timp_numpy_fft, 'bo-', linewidth=2, markersize=8, label='numpy.fft.fft')

plt.xlabel('Dimensiunea vectorului (N)')
plt.ylabel('Timp de executie (secunde)')
plt.title('Compararea timpilor de executie: DFT vs FFT vs numpy.fft.fft')
plt.legend()
plt.grid(True, alpha=0.3)

# log Oy
plt.yscale('log')

plt.tight_layout()
plt.savefig('comparatie_timp_executie.pdf', dpi=300, bbox_inches='tight')
plt.close()
