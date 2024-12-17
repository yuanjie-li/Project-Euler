# coding=utf-8
"""

PROBLEM 047 - Distinct Prime Factors

Written by: Yuanjie Li
Date: June 28, 2018

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?

"""
import sys
sys.path.append('../utils')
import utils
import math

def main():
    print("Generating prime array ...")
    primeArr = utils.getPrimeArr(10000)
    print("Done.")

    i = 10000
    while True:
        if i > primeArr[-1]:
            print("Updating prime array to %s." %(i*10))
            primeArr = utils.updatePrimeArr(i*10, primeArr)
            print("Done.")

        facs = utils.getPrimeFactors(i,primeArr)
        if len(list(set(facs))) == 4:
            # Try to find next 3
            found = True
            for j in range(i+1, i+4):
                facs = utils.getPrimeFactors(j,primeArr)
                if len(list(set(facs))) != 4:
                    found = False
                    break
            if found:
                print("The first 4 consecutive integer is: %s" %i)
                break
        i += 1


if __name__ == "__main__":
    main()

