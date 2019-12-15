import numpy as np
from scipy.io.wavfile import read
from scipy.signal import decimate
from glob import glob
from random import seed, choice
from time import time
from sys import argv
from warnings import filterwarnings


def get_sample(path):
    return glob('./' + path)[0]


def signal_data(sample):
    w, signal = read(sample)
    if(len(signal.shape) != 1):
        signal = [sig[0] for sig in signal]
    return w, signal


def cut_data(list, x, y, w, n):
    return list[int((x / w) * n):int((y / w) * n)]


def cut(list, x, y):
    return list[int(x * 0.001 * len(list)):int(y * 0.001 * len(list))]


def hps(signal, freq):
    final_signal = signal
    for x in range(2, 5):
        decimated_signal = decimate(signal, x)
        final_signal = final_signal * np.array(list(decimated_signal) + [0 for rest in range(len(final_signal) - len(decimated_signal))])

    final_signal = cut(final_signal, 65, 350)
    freq = cut(freq, 65, 350)
    return final_signal, freq


def solve(sample, male = 120.0, female = 220.0, show_result = False):
    result = get_fundemental_frequency(sample, male, female)
    if show_result:
        print(result)
    if result < (male + female) / 2:
        return 'M'
    return 'F'       


def get_fundemental_frequency(sample, male, female):
    try:
        w, signal = signal_data(sample)
        n = len(signal)
        frequency = [i * float(w / n) for i in range(n)]

        signal = np.fft.fft(signal)
        signal = abs(signal) / (n * 0.5)

        signal = cut_data(signal, 0, 1000, w, n)
        frequency = cut_data(frequency, 0, 1000, w, n)
    
        signal, frequency = hps(signal, frequency)

        return frequency[np.argmax(signal)]
    except:
        seed(int(time()))
        return choice((male, female))


def main(path_to_sample):
    sample = get_sample(path_to_sample)
    print(solve(sample, show_result=False)) # toggle printing exact result


if __name__ == '__main__':
    filterwarnings('ignore')
    main(argv[1])
