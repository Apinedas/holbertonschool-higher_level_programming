#!/usr/bin/python3
def best_score(a_dictionary):
    best_student = None
    score = 0
    if (a_dictionary):
        for student in a_dictionary:
            if a_dictionary[student] > score:
                best_student = student
                score = a_dictionary[student]
    return best_student
