# coding=utf-8
"""

PROBLEM 040 - Champernowne's constant

Written by: Yuanjie Li
Date: June 26, 2018

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""
import sys
sys.path.append('../utils')
import utils
import math

def main():
    champsnum = ""
    for i in range(1,1000001):
        champsnum += str(i)
        if len(champsnum) > 1000000:
            break

    output = 1
    for i in range(6):
        output *= int(champsnum[int(math.pow(10,i) - 1)])

    print(output)

if __name__ == "__main__":
    main()

