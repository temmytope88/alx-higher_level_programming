#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for i in range(len(arr)):
        if arr[i][0:2] != "__":
            print("{}".format(arr[i]))
