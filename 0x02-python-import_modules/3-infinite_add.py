#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    sum = 0
    if num - 1 == 0:
        sum = + 0
    elif num - 1 == 1:
        sum = + int(sys.argv[1])
    else:

        total = 0
        for x in range(1, num):
            total = total + int(sys.argv[x])

        sum = + total
    print(sum)
