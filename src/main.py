from src.genetic_algorithm import GA
from src.nqueens import fit as nqueens_fit

if __name__ == "__main__":

    def fit(individual, **kwargs):
        c = 0
        for a, b in zip(individual.sequence, kwargs['target']):
            if a == b:
                c += 1
        return c

    ga = GA(100, 16, ["1", "0"], nqueens_fit, 0.05)
    ga.get_initial_population()
    for _ in range(1000):
        ga.build_mating_pool(10)
        ga.reproduction()
    print(ga.population)
