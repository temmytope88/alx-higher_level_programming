#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_add = []
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        list_add.append(0)
        list_add.append(0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        list_add.append(tuple_a[0] + tuple_b[0])
        list_add.append(0)
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        list_add.append(0 + tuple_b[0])
        list_add.append(0)
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        list_add.append(0 + tuple_b[0])
        list_add.append(0 + tuple_b[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        list_add.append(tuple_a[0] + tuple_b[0])
        list_add.append(0 + tuple_b[1])
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        list_add.append(0 + tuple_a[0])
        list_add.append(0)
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        list_add.append(0 + tuple_a[0])
        list_add.append(0 + tuple_a[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        list_add.append(tuple_a[0] + tuple_b[0])
        list_add.append(0 + tuple_a[1])
    else:
        list_add.append(tuple_a[0] + tuple_b[0])
        list_add.append(tuple_a[1] + tuple_b[1])
    return tuple(list_add)
