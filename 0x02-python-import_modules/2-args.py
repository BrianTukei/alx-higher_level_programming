#!/usr/binb/python3

if_name_=="_main_":
    """rint the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}:{}".formate(i + 1, sys.argv[i + 1]))


