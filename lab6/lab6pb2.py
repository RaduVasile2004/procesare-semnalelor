import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 100
x_original = np.random.randn(N)

x = x_original.copy()
convolutions_random = [x_original]

plt.figure(figsize=(12, 10))

for i in range(3):
    x = np.convolve(x, x, mode='full')
    convolutions_random.append(x)

for i, signal in enumerate(convolutions_random):
    plt.subplot(4, 1, i+1)
    plt.plot(signal)
    if i == 0:
        plt.title('Semnalul Aleator Original')
    else:
        plt.title(f'Dupa {i} convolutii')
    plt.grid(True)

plt.tight_layout()
plt.savefig('exercitiul2_random.png')
plt.close()

x_rect = np.zeros(N)
x_rect[40:60] = 1

x = x_rect.copy()
convolutions_rect = [x_rect]

plt.figure(figsize=(12, 10))

for i in range(3):
    x = np.convolve(x, x, mode='full')
    convolutions_rect.append(x)

for i, signal in enumerate(convolutions_rect):
    plt.subplot(4, 1, i+1)
    plt.plot(signal)
    if i == 0:
        plt.title('Semnalul Bloc Rectangular Original')
    else:
        plt.title(f'Dupa {i} convolutii')
    plt.grid(True)

plt.tight_layout()
plt.savefig('exercitiul2_rectangular.png')
plt.close()