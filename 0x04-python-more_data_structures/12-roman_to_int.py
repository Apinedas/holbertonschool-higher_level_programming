#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        roman_numbers = list('IVXLCDM')
        roman_values = [1, 5, 10, 50, 100, 500, 1000]
        roman_conversion = dict(zip(roman_numbers, roman_values))
        total_value = 0
        i = 0
        while (i < len(roman_string)):
            actual_roman = roman_string[i]
            if i + 1 < len(roman_string):
                next_roman = roman_string[i + 1]
            else:
                next_roman = None
            actual_value = roman_conversion[actual_roman]
            if next_roman and roman_conversion[next_roman] > actual_value:
                actual_value = actual_value * -1
            total_value += actual_value
            i += 1
        return total_value
    else:
        return (0)
