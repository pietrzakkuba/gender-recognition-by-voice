import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import decimate
from glob import glob
from random import seed, choice


def signal_data(sample):
    w, signal = read(sample)
    if(len(signal.shape) != 1):
        signal = [sig[0] for sig in signal]
    return w, signal


def cut_data(x, y, w = 1, n = 1):
    return int((x / w) * n), int((y / w) * n)


def cut(list, x, y):
    return list[int(x * 0.001 * len(list)):int(y * 0.001 * len(list))]


def get_samples_paths(samples):
    return glob(samples + '/*')


def right_answers(samples):
    answers = list()
    for sample in samples:
        answers.append(sample[-5])
    return answers


def solve(samples, male = 120, female = 220):
    answers = list()
    for sample in samples:
        fundamental_frequency = get_fundemental_frequency(sample)
        print(fundamental_frequency)
        if fundamental_frequency < (male + female) / 2:
            answers.append('M')
        else:
            answers.append('K')        
    return answers


def get_fundemental_frequency(sample):
    try:
        w, signal = signal_data(sample)
        n = len(signal)
        frequency = [i * float(w / n) for i in range(n)]

        signal = np.fft.fft(signal)
        signal = abs(signal) / (n * 0.5)

        a, b = cut_data(0, 1000, w, n)
        signal=signal[a:b]
        frequency=frequency[a:b]

        final_signal=signal
        for x in range(2, 5):
            decimated_signal=decimate(signal, x)
            right_sized_signal=list(decimated_signal) + [0 for zero in range(len(final_signal) - len(decimated_signal))]
            final_signal=final_signal * np.array(right_sized_signal)

        final_signal = cut(final_signal, 65, 350)
        frequency = cut(frequency, 65, 350)

        result=frequency[np.argmax(final_signal)]
        return result
    except:
        seed(25)
        return choice((120.0, 220.0))


def main():
    samples = get_samples_paths('samples')
    answers = right_answers(samples)
    solved_answers = solve(samples)
    print(solved_answers)
    k = 0
    for i in range(len(answers)):
        if answers[i] == solved_answers[i]:
            k += 1
    print(100 * k / len(answers))

if __name__ == '__main__':
    main()
