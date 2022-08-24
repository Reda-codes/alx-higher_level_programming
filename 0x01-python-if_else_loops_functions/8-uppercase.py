#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{:c}".format( ord(i)-32 if ord(i) < 123 and ord(i) > 96 else ord(i)), end='')
    print("\n", end='')
