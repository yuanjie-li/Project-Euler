# coding=utf-8
"""

PROBLEM 041 - Pandigital Prime

Written by: Yuanjie Li
Date: June 26, 2018

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?

"""
import sys
sys.path.append('../utils')
import utils
import math

def main():
    best = 0
    pandig = ['1','2','3','4','5','6','7','8','9']

    print("Generating primes array ... ")
    primeArr = utils.getPrimeArr(999)
    print("Done.")
    for i in range(4,10):
        print("Updating prime array to %s..." % int(math.pow(10,i)))
        primeArr = utils.updatePrimeArr(int(math.pow(10,i)), primeArr)
        print("Updated.")

        # Subset and get all permutations of these.
        pan_check = [int(x) for x in pandig[:i]]
        all_check = utils.permute(pan_check)

        for permute in all_check:
            number = ""
            for digit in permute:
                number += str(digit)

            number = int(number)
            if number in primeArr and number > best:
                best = number
        print("The current best is: %i" % best)

    print('The best prime is: %i' % best)
    print(best)

if __name__ == "__main__":
    main()

