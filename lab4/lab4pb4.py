"""

Rezolvare:
semnal trece-banda cu frecvente intre 40Hz si 200Hz.
frecventa minima de esantionare este data de:
fs_min = 2 * B
B este latimea de banda.

Latimea de banda B = f_max - f_min = 200Hz - 40Hz = 160Hz.
Frecventa minima de esantionare fs_min = 2 * 160Hz = 320Hz.

Verificare: fs_min = 320Hz > 2 * B = 320Hz, conditie indeplinita.
Aceasta frecventa garanteaza ca toate componentele de frecventa intre 40Hz si 200Hz
vor fi pastrate in semnalul discretizat fara pierderi datorate aliasing-ului.

Raspuns final: Frecventa minima de esantionare este 320 Hz.
"""