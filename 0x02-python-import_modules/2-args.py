#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    num = length - 1
    if num == 0:
        print("{} arguments:".format(num))
    elif num == 1:
        print("{} argument:".format(num))
        print("{}: {}".format(num, sys.argv[num]))
    else:
        print("{} arguments:".format(num))
        for x in range(1, length):
            print("{}: {}".format(x, sys.argv[x]))
