# Utilities file for stuff like:
#   Finding Primes up to n
#   Getting all factors of n

import numpy as np
import random
import math

# Get all primes up to n, inclusive
def getPrimeArr(n):
    # Sieve of Eratosthenes
    numArr = [x+1 for x in xrange(1,n)]
    notPrimes = []
    primeArr = []

    # Generate the non-primes
    for num in numArr:
        if num not in notPrimes:
            primeArr.append(num)

            for j in xrange(num*2-2, len(numArr), num):
                notPrimes.append(numArr[j])

    return primeArr

# Update a prime array up to n, inclusive
def updatePrimeArr(n, primeArr):
    for x in xrange(primeArr[-1], n+1):
        for prime in primeArr:
            if x % prime == 0:
                break
            elif prime == primeArr[-1] and\
                 x % prime != 0:
                primeArr.append(x)

    return primeArr

# Get all divisors of n (non-prime)
def getDivs(n):

    maxF = n # Maximum factor, stopping condition
    output = [1,n]

    for x in xrange(2, n // 2):
        if x + 1 == maxF:
            break
        if n % x == 0:
            output.append(x)
            output.append(n / x)

            maxF = n / x

    output = sorted(output)
    return output

if __name__ == "__main__":
    primeArr = getPrimeArr(25)
    print("Primes up to 25 : "),
    print(primeArr)

    primeArr = updatePrimeArr(50, primeArr)
    print("Primes up to 25, updated to 50 : "),
    print(primeArr)

    factors = getDivs(24)
    print("Factors of 24 : "),
    print(factors)
