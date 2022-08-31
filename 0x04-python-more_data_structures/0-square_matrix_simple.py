#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = []
    for i in matrix:
        temp.append([j**2 for j in i])
    return temp
