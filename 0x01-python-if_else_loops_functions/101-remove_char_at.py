#!/usr/bin/python3
def remove_char_at(str, n):
    if (n > 0) and (n <= len(str)):
        prefix = str[:n]
        suffix = str[(n + 1):]
        return (prefix + suffix)
    return (str)
