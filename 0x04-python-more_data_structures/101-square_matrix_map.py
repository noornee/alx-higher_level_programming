#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        root = map(lambda n: n ** 2, matrix[i])
        new_matrix.append(list(root))
    return new_matrix
