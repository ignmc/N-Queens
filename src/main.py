from src.genetic_algorithm import GA
from src.nqueens import fit as nqueens_fit

MUTATION_PROB = 0.05
POPULATION_SIZE = 100
SEQUENCE_SIZE = 25  # length of the sequences
VOCABULARY = ['0', '1']  # possible values for a sequence
GENERATIONS = 2000
TOURNAMENT_SIZE = 10


if __name__ == "__main__":

    # def fit(individual, **kwargs):
    #     c = 0
    #     for a, b in zip(individual.sequence, kwargs['target']):
    #         if a == b:
    #             c += 1
    #     return c

    population_fit = []
    first_solution_gen = None

    ga = GA(POPULATION_SIZE, SEQUENCE_SIZE, VOCABULARY, nqueens_fit, MUTATION_PROB)
    ga.get_initial_population()
    population_fit.append(ga.avg_fitness())

    for generation in range(GENERATIONS):
        ga.build_mating_pool(TOURNAMENT_SIZE)
        ga.reproduction()
        population_fit.append(ga.avg_fitness())
        if first_solution_gen is None and ga.has_solution():
            first_solution_gen = generation

    print(population_fit, first_solution_gen)
