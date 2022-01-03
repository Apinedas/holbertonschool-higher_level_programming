#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) >= 2):
        addend_1 = tuple_a
    if (len(tuple_b) >= 2):
        addend_2 = tuple_b
    if (len(tuple_a) == 1):
        addend_1 = (tuple_a[0], 0)
    if (len(tuple_a) == 0):
        addend_1 = (0, 0)
    if (len(tuple_b) == 1):
        addend_2 = (tuple_b[0], 0)
    if (len(tuple_b) == 0):
        addend_2 = (0, 0)
    addition = (addend_1[0] + addend_2[0], addend_1[1] + addend_2[1])
    return addition
