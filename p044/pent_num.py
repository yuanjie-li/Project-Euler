# coding=utf-8
"""

PROBLEM 044 - Pentagon Numbers

Written by: Yuanjie Li
Date: June 27, 2018

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten
pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value
of D?

"""
import sys
sys.path.append('../utils')
import utils
import math

# Returns the pentagon number for n
def getPen(n):
    return n * (3 * n - 1) / 2

# Returns True if n is a pen num
def isPen(pen):
    # pen = n(3n-1) / 2
    pen *= 2
    # 3n^2 - n - 2pen = 0
    a = 3
    b = -1
    c = -1 * pen
    d = (b**2) - (4*a*c)
    posx = (-b-math.sqrt(d))/(2*a)
    negx = (-b+math.sqrt(d))/(2*a)

    if posx == int(posx) and posx > 0:
        return True
    if negx == int(negx) and negx > 0:
        return True

    return False

def main():
    bestD = 10000000
    for j in range(8,9999999):
        for k in range(j+1, 10000000):
            penj = getPen(j)
            penk = getPen(k)

            diff = (penk-penj)
            if diff > bestD:
                break
            if isPen(diff):
                summ = penj + penk
                if isPen(summ) and diff < bestD:
                    bestD = penk - penj

    print("The smallest difference is: %s" % bestD)

if __name__ == "__main__":
    main()

