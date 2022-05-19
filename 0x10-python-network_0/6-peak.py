#!/usr/bin/python3
'''Module to find a peak'''


def find_peak(list_of_integers):
    '''Peak function for a integers list'''
    if list_of_integers:
        return sorted(list_of_integers)[-1]
    return None
