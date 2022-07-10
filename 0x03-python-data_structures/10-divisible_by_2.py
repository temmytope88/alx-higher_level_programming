#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_value = []
    for x in my_list:
        if x % 2 == 0:
            my_value.append(True)
        else:
            my_value.append(False)
    return my_value
