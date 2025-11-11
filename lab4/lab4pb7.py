"""
Rezolvare:

P_semnal_dB = 90dB
SNR_dB = 80dB

SNR_dB = 10 * log10(P_semnal / P_zgomot)

Din formula rezulta:
80 = 10 * log10(P_semnal / P_zgomot)
8 = log10(P_semnal / P_zgomot)
10^8 = P_semnal / P_zgomot
P_zgomot = P_semnal / 10^8

puterea zgomotului in dB:
P_zgomot_dB = 10 * log10(P_zgomot)
P_zgomot_dB = 10 * log10(P_semnal / 10^8)
P_zgomot_dB = 10 * log10(P_semnal) - 10 * log10(10^8)
P_zgomot_dB = P_semnal_dB - 80
P_zgomot_dB = 90dB - 80dB = 10dB

Verificare:
Diferenta dintre puterea semnalului si puterea zgomotului este 90dB - 10dB = 80dB,
ceea ce corespunde cu SNR_dB = 80dB.

Raspuns final: Puterea zgomotului este 10 dB.
"""