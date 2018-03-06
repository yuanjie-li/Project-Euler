# coding=utf-8
"""

PROBLEM 035 - Circular Primes

Written by: Yuanjie Li
Date: Oct 26, 2017

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

"""
import sys
sys.path.append('../utils')
import utils

def main():

    print("Generating primes ...")
    # This line takes a LONG time ...
    primeArr = utils.getPrimeArr(999999)
    print("Primes generated.")

    count = 0

    # Iterate through and check permutations.
    for num in primeArr:
        # This line takes long time.
        num_perms = utils.permute([x for x in str(num)])
        # Then check all of the perms
        for perm in num_perms:
            perm = int(''.join(perm))
            if perm not in primeArr:
                break
        else:
            count += 1
    print(count)

if __name__ == "__main__":
    main()

