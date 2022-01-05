def update_dictionary(a_dictionary, key, value):
    for actual_key in a_dictionary:
        if actual_key == key:
            a_dictionary[key] = value
            actual_key = key
    else:
        a_dictionary[key] = value
    return a_dictionary
