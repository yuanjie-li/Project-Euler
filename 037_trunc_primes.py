# coding=utf-8
"""

PROBLEM 037 - Truncatable Primes

Written by: Yuanjie Li
Date: Mar 20, 2018

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left
    3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
import sys
sys.path.append('../utils')
import utils

def main():
    primeArr = utils.getPrimeArr(100)
    print primeArr
    count = 0
    output = 0

    index = 4
    upper = 100
    while count < 11:
        cur_prime = primeArr[index]
        left = leftTrunc(cur_prime, primeArr)
        if left:
            right = rightTrunc(cur_prime, primeArr)
            if right:
                print "Found:", cur_prime
                count += 1
                output += cur_prime
        index += 1
        while index == len(primeArr):
            upper += 1000
            primeArr = utils.updatePrimeArr(upper, primeArr)
            print "Updating prime array ...", len(primeArr)

    print "Output:",output

def leftTrunc(prime, arr):
    strprime = str(prime)
    for i in range(1,len(strprime)):
        trunc = int(strprime[i:])
        if trunc not in arr:
            return False
    return True

def rightTrunc(prime, arr):
    strprime = str(prime)
    for i in range(1,len(strprime)):
        trunc = int(strprime[:-i])
        if trunc not in arr:
            return False
    return True

if __name__ == "__main__":
    main()

