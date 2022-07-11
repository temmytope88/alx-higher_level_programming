#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from unittest import result
    import calculator_1
    num = len(sys.argv)

    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        opr = sys.argv[2]
        if opr not in ["+", "-", "/", "*"]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if opr == "+":
                result = calculator_1.add(a, b)
                print("{} + {} = {}".format(a, b, result))
            elif opr == "-":
                result = calculator_1.sub(a, b)
                print("{} - {} = {}".format(a, b, result))
            elif opr == "/":
                result = calculator_1.div(a, b)
                print("{} / {} = {}".format(a, b, result))
            else:
                result = calculator_1.mul(a, b)
                print("{} * {} = {}".format(a, b, result))
