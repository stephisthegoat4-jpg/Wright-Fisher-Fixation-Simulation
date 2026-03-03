import numpy as np
import matplotlib.pyplot as plt


def theoretical_fixation_probability(N, s, initial_frequency):
    if s == 0:
        return initial_frequency
    else:
        numerator = 1 - np.exp(-2 * s * 2 * N * initial_frequency)
        denominator = 1 - np.exp(-2 * s * 2 * N)
        return numerator / denominator

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


def main():

    initial_frequency = float(input("Initial allele frequency (initial_frequency): "))
    generations = int(input("Number of generations: "))
    s = float(input("Selection coefficient (s): "))

    replicates = 500
    N_values = [25, 50, 100, 200, 400]

    Ns_values = []
    simulation_values = []
    theory_values = []

    for N in N_values:

        sim_fix, mean_time = estimate_fixation(
            N, s, initial_frequency, generations, replicates
        )

        theory_fix = theoretical_fixation_probability(N, s, initial_frequency)

        Ns_values.append(N * s)
        simulation_values.append(sim_fix)
        theory_values.append(theory_fix)

        print("N = {N}")
        print(f"  Fixation Probability (Simulation): {sim_fix}")
        print(f"  Fixation Probability (Theory): {theory_fix}")
        print(f"  Mean Fixation Time: {mean_time}")

    plt.figure()
    plt.plot(Ns_values, simulation_values, 'o-', label="Simulation")
    plt.plot(Ns_values, theory_values, 's--', label="Theory")
    plt.xlabel("Ns")
    plt.ylabel("Fixation Probability")
    plt.title("Fixation Probability vs Ns")
    plt.legend()
    plt.show()

    plt.figure()
    N = N_values[-1]

    for _ in range(5):
        freqs, _, _ = simulate_trajectory(
            N, s, initial_frequency, generations
        )
        plt.plot(freqs)

    plt.xlabel("Generation")
    plt.ylabel("Allele Frequency")
    plt.title(f"Sample Trajectories (N={N})")
    plt.show()


if __name__ == "__main__":
    main()
