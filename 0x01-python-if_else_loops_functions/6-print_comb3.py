#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if (i != j) and (i < j) and (i != 8):
            print("{:d}{:d}".format(i, j), end=", ")
print("{:d}{:d}".format(8, 9))
