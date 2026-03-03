import numpy as np

def theoretical_fixation_probability(N, s, initial_frequency):
    if s == 0:
        return initial_frequency
    else:
        numerator = 1 - np.exp(-2 * s * 2 * N * initial_frequency)
        denominator = 1 - np.exp(-2 * s * 2 * N)
        return numerator / denominator
