# coding=utf-8
"""

PROBLEM 036 - Double-base Palindromes

Written by: Yuanjie Li
Date: Mar 20, 2018

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""
import sys
sys.path.append('../utils')
import utils

def main():
    count = 1 # 0 and 1 counts

    for i in range(2,1000000):
        palin = checkPalin(i)
        bpalin = checkBase2(i)

        if palin and bpalin:
            count += i
    print(count)

def checkPalin(i):
    stri = str(i)
    for i in range(0, len(stri) // 2):
        if stri[i] != stri[-(1+i)]:
            return False
    return True

def checkBase2(i):
    # Get string without '0b' header
    b2 = bin(i)[2:]
    for i in range(0, len(b2) // 2):
        if b2[i] != b2[-(1+i)]:
            return False
    return True

if __name__ == "__main__":
    main()

