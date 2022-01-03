#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_int = my_list[0]
        i = 0
        while i < len(my_list):
            if max_int < my_list[i]:
                max_int = my_list[i]
                i = 0
            else:
                i += 1
        return max_int
