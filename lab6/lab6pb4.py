import numpy as np

n = 20
x = np.random.rand(n)
d = 3
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

result1 = np.fft.ifft(X * Y)
result2 = np.fft.ifft(Y / X)

d_recovered1 = np.argmax(np.real(result1))
d_recovered2 = np.argmax(np.real(result2))

print("Deplasare originala d:", d)
print("Deplasare recuperata cu inmultire:", d_recovered1)
print("Deplasare recuperata cu impartire:", d_recovered2)