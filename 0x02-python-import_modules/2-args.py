#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum1 = len(sys.argv) -1
    if sum1 < 1:
        print("0 arguments.")
    elif sum1 == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(sum1))
    for i in range(sum1):
            print("{} : {}".format(i + 1,sys.argv[i + 1]))


