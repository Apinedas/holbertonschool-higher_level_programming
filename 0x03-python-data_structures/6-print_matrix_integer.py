#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        while i < (len(row) - 1):
            print("{:d}".format(row[i]), end=" ")
            i += 1
        if row:
            print("{:d}".format(row[i]))
        else:
            print()
