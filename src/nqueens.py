import math


def fit(individual, **kwargs):
    """
    Length of sequence should be n^2; The i'th element is 1 if there's a queen in the i%n column of the i//n row.
    0 if there isn't.
    :param individual: Something
    :param kwargs: Something
    :return: Something
    """

    def get_row(sequence, n, i):
        return sequence[i*n : n*(i+1)]

    def make_matrix(sequence):
        n = int(math.sqrt(len(sequence)))
        matrix = list()
        for i in range(n):
            matrix.append(get_row(sequence, n, i))
        return matrix

    def check_vertical(board, i, j):
        hits = 0
        n = len(board)
        for ii in range(i + 1, n):
            if board[ii][j] == "1":  # check directly vertical
                hits += 1
            diff = ii - i
            if j - diff >= 0 and board[ii][j - diff] == "1":  # check left-bottom diagonal
                hits += 1
            if j + diff < n and board[ii][j + diff] == "1":  # check right-bottom diagonal
                hits += 1
        return hits

    def check_horizontal(board, i, j):
        hits = 0
        n = len(board)
        for y in range(j + 1, n):
            if board[i][y] == "1":
                hits += 1
        return hits

    # Length of sequence should be n^2; The i'th element is 1 if there's a queen in the i%n column of the i//n row.
    # 0 if there isn't.
    sequence = individual.sequence
    n = int(math.sqrt(len(sequence)))

    if sequence.count("1") != n:
        return -math.sqrt(n)

    board = make_matrix(sequence)

    hits = 0  # pairs of queens that attack each other
    for i in range(n):
        for j in range(n):
            if board[i][j] == "1":
                hits += check_horizontal(board, i, j) + check_vertical(board, i, j)
    return -hits


def avg_fitness(population, fit_func):
    s = 0
    for individual in population:
        s += fit_func(individual)
    return s/len(population)
