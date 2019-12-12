# from numpy import *
# from ipywidgets import *
# import math as mt
# import scipy.io.wavfile

import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy import size
import numpy as np
from pylab import copy
from scipy.signal import decimate

w, signal = read('./test/066_K.wav')
signal = [s[0] for s in signal] 

fig = plt.figure(figsize=(15, 6), dpi=80)

t = size(signal) / int(w)
time = [i * t / len(signal) for i in range(len(signal))]

# ax.plot(time, signal) #input


n = len(signal)
n_arange = np.arange(len(signal))


signal1 = np.fft.fft(signal)
signal1 = abs(signal1) / (0.5 * n)
freq = [v * float(w / n) for v in n_arange]
freq2 = freq[:int(len(freq) / 2)]
signal2 = signal1[:int(len(signal1) / 2)]
ax = fig.add_subplot(121)
ax.plot(freq2[:int(len(freq2)/50)], signal2[:int(len(freq2)/50)]) # /50 - skrócenie zakresu częstotliwości do narysowania


    #nie wiem czy tu nie trzeba zrobic:
    #(usuniecie podwojenia
    #wyswietl signal
# ax = fig.add_subplot(132)
# stem(freq, ffty, '-*')

# signal2 = signal2 * np.kaiser(len(signal2), 5) #dobierz te parametry
hps = copy(signal2)
for i in np.arange(2,6):
    d = decimate(signal2, int(i))
    hps[:len(d)] *= d
ax = fig.add_subplot(122)
ax.plot(freq2[:int(len(freq2)/50)], hps[:int(len(freq2)/50)])
plt.show()
print(freq[np.argmax(hps)])
# #hps[0:freq[70]] = 0
# hps=hps[int((70/44200)*ind)]
# ax = fig.add_subplot(133)
# stem(freq, hps)
# stem(freq2, ffty2, '-*')
# our_result = freq[np.argmax(hps)]
# print(our_result)
# if our_result > 180:
#     print('M')
# else:
#     print('K')