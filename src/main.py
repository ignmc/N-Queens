from src.genetic_algorithm import GA
from src.nqueens import fit as nqueens_fit

MUTATION_PROB = 0.05
POPULATION_SIZE = 100
SEQUENCE_SIZE = 16
VOCABULARY = ['0', '1']


if __name__ == "__main__":

    def fit(individual, **kwargs):
        c = 0
        for a, b in zip(individual.sequence, kwargs['target']):
            if a == b:
                c += 1
        return c


    ga = GA(POPULATION_SIZE, SEQUENCE_SIZE, VOCABULARY, nqueens_fit, MUTATION_PROB)
    ga.get_initial_population()
    for _ in range(1000):
        ga.build_mating_pool(10)
        ga.reproduction()
    print(ga.population)
