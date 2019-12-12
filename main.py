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
# freq2 = freq[0:int(len(freq) / 2)]
# signal2 = signal[0:int(len(signal) / 2)]
    #nie wiem czy tu nie trzeba zrobic:
    #(usuniecie podwojenia
    #wyswietl signal
# ax = fig.add_subplot(132)
# stem(freq, ffty, '-*')

signal1 = signal1 * np.kaiser(len(signal1), 100) #dobierz te parametry

hps = copy(signal1)
for i in np.arange(2,6):
    d = decimate(signal, int(i))
    hps[:len(d)] *= d
ax = fig.add_subplot(111)
ax.plot(freq, hps)
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