import numpy as np

def simulate_trajectory(N, s, initial_frequency, generations):
    A = int(initial_frequency * 2 * N)
    freqs = []

    for gen in range(generations):
        freqs.append(A / (2 * N))

        if A == 0 or A == 2 * N:
            return freqs, gen, A 

        frequency = A / (2 * N)
        selection_frequency = (frequency * (1 + s)) / (
            frequency * (1 + s) + (1 - frequency)
        )

        A = np.random.binomial(2 * N, selection_frequency)

    return freqs, generations, A

def estimate_fixation(N, s, initial_frequency, generations, replicates):
    fixation_count = 0
    fixation_times = []

    for _ in range(replicates):
        _, time, final_state = simulate_trajectory(N, s, initial_frequency, generations)

        if final_state == 2 * N:
            fixation_count += 1
            fixation_times.append(time)

    fixation_probability = fixation_count / replicates
    mean_fix_time = np.mean(fixation_times) if fixation_times else None

    return fixation_probability, mean_fix_time
:
    main()
