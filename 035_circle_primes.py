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
    primeArr = utils.getPrimeArr(99)
    primeIndex = 0
    print("Primes generated.")

    count = 0

    # Calculate all 3 digit primes:
    for i in range(1,6):
        # Iterate through and check permutations.
        for num in primeArr[primeIndex:]:
            # This line takes long time.
            num_perms = rotate(str(num))
            # Then check all of the perms
            if len(list(set(primeArr[primeIndex:]) & set(num_perms))) == \
                    len(num_perms):
                count += 1
        print "Completed:", 100 * 10 ** (i-1)
        # Update the primeArr to all 4 digit numbers
        primeIndex = len(primeArr)-1 # Skip these
        if 100 * 10 ** i > 1000000:
            break
        primeArr = utils.updatePrimeArr(100 * 10 ** i, primeArr)
        print "Prime array updated."
    print(count)

def rotate(s):
    output = []
    for i in range(1,len(s)):
        output.append(int(s[i:] + s[:i]))
    return output

if __name__ == "__main__":
    main()

