#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda matrix : [pow(i, 2) for i in matrix], matrix))
