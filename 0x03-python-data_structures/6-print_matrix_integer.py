#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for x in range(len(lists)):
            if x == (len(lists) - 1):
                print("{:d}".format(lists[x]), end="")
            else:
                print("{:d} ".format(lists[x]), end="")
        print()
