#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for y in range(x):
            item = my_list[y]
            print("{}".format(item), end="")
        print()
        return y+1
    except:
        print()
        return y
