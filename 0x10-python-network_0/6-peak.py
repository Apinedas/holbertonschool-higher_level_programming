#!/usr/bin/python3
'''Module to find a peak'''
def find_peak(list_of_integers):
    if list_of_integers:
        sorted_list = sorted(list_of_integers)
        return sorted_list[-1]
    return None
