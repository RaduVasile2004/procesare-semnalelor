import numpy as np
import matplotlib.pyplot as plt

N = 8
n = np.arange(N)
k = n.reshape((N, 1))

F = np.exp(-2j * np.pi * k * n / N) / np.sqrt(N)

print("Matricea Fourier F (8x8):")
print(F)

# parte reala si imaginara pentru fiecare linie
fig, axs = plt.subplots(N, 2, figsize=(12, 16))

for i in range(N):
    # reala
    axs[i, 0].stem(n, F[i, :].real, basefmt=" ")
    axs[i, 0].set_ylabel(f'Linia {i}')
    axs[i, 0].set_ylim(-0.5, 0.5)
    axs[i, 0].grid(True, alpha=0.3)
    if i == N - 1:
        axs[i, 0].set_xlabel('n')
    if i == 0:
        axs[i, 0].set_title('Partea Reala')

    # imaginara
    axs[i, 1].stem(n, F[i, :].imag, basefmt=" ")
    axs[i, 1].set_ylim(-0.5, 0.5)
    axs[i, 1].grid(True, alpha=0.3)
    if i == N - 1:
        axs[i, 1].set_xlabel('n')
    if i == 0:
        axs[i, 1].set_title('Partea Imaginara')

plt.tight_layout()

plt.savefig('matricea_fourier_subploturi.pdf')
plt.close()

# unitaritate
F_conj_transpus = F.conj().T  # F^H
FHF = F_conj_transpus @ F  # F^H * F

print("\nMatricea F^H * F:")
print(FHF)

# FHF este proportionala cu matr identitate
identity = np.eye(N)
tolerance = 1e-10

# numpy.allclose
is_unitary_allclose = np.allclose(FHF, identity, atol=tolerance)
print(f"\nVerificare cu np.allclose: Matricea este unitara? {is_unitary_allclose}")

# norm
difference_norm = np.linalg.norm(FHF - identity)
print(f"Norma diferentei dintre F^H*F si I: {difference_norm}")
print(f"Verificare cu norma: Matricea este unitara? {difference_norm < tolerance}")

# factor de proportionalitate ar trebui sa fie 1
print(f"\nElementele diagonale ale F^H*F: {np.diag(FHF)}")

# toate elementele de pe diagonala sunt 1, iar celelalte sunt 0
diagonal_ok = np.allclose(np.diag(FHF), np.ones(N), atol=tolerance)
off_diagonal_ok = np.allclose(FHF - np.diag(np.diag(FHF)), np.zeros((N, N)), atol=tolerance)

print(f"Elementele diagonale sunt 1: {diagonal_ok}")
print(f"Elementele off-diagonale sunt 0: {off_diagonal_ok}")
print(f"Matricea este unitara: {diagonal_ok and off_diagonal_ok}")

# matrice F^H * F
plt.figure(figsize=(10, 8))
plt.imshow(np.abs(FHF), cmap='hot', interpolation='nearest')
plt.colorbar(label='Magnitudine')
plt.title('Matricea F$^H$F')
plt.xlabel('n')
plt.ylabel('k')

# valorile pe imagine
for i in range(N):
    for j in range(N):
        plt.text(j, i, f'{FHF[i, j].real:.2f}',
                 ha='center', va='center', color='white', fontsize=8)

plt.savefig('verificare_unitaritate.pdf')
plt.close()
