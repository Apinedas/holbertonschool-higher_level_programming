#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    sum = 0
    i = 1
    argc = len(sys.argv)

    while (i < argc):
        sum += int(sys.argv[i])
        i += 1
    
    print("{:d}".format(sum))
