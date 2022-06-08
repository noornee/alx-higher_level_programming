#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    for i in range(len(matrix)):
        square = []
        for j in range(len(matrix[i])):
            square.append(matrix[i][j] ** 2)
        arr.append(square)
    return arr
