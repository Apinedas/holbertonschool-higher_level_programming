#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string = new_string  + char
        i += 1
    return new_string
