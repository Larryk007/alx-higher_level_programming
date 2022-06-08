#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            value += int(arg)
    print(value)
