#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_weight = 0
    total_score = 0
    for tuple in my_list:
        total_weight += tuple[1]
        total_score += tuple[0] * tuple[1]
    return total_score / total_weight
