# coding=utf-8
"""

PROBLEM 046 - Goldbach's Other Conjecture

Written by: Yuanjie Li
Date: June 28, 2018

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?

"""
import sys
sys.path.append('../utils')
import utils
import math

# An odd number when subtracted by a prime results in an even number that
# when divided by 2 is not a perfect square.

def main():
    primeArr = utils.getPrimeArr(1000)
    found = False
    index = 35
    while not found:
        if index > primeArr[-1]:
            utils.updatePrimeArr(index*5, primeArr)
            print("Updated prime array to: %s" %(index*5))
        if index in primeArr:
            index += 2
            continue
        # Perform the check
        failed = True
        for i in primeArr:
            if index < i:
                break
            val = math.sqrt((index - i) / 2)
            if val == int(val):
                failed = False
                break
        if failed:
            print("Failed at %s." %index)
            found = True
        index += 2

if __name__ == "__main__":
    main()

