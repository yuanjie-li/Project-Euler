# Utilities file for stuff like:
#   Finding Primes up to n
#   Getting all factors of n

import numpy as np
import random
import math

# Get all primes up to n, inclusive
def getPrimeArr(n):

    # Sieve of Eratosthenes
    numArr =[2,3]
    for num in range(5, n+1, 2):
        numArr.append(num)
    print("Sieve generated.")
    # Ticker
    sieveSize = len(numArr)
    print("Sieve size :"),
    print(sieveSize)

    # Generate the non-primes
    index = 1
    num = numArr[index]
    while num != numArr[-1]:

        # Ticker
        if len(numArr) < sieveSize // 2:
            sieveSize = len(numArr)
            print("Sieve has been reduced by half to"),
            print(sieveSize)

        for j in range(num**2, n+1, num * 2):
            if j in numArr:
                numArr.remove(j)
        index += 1
        num = numArr[index]

    print(len(numArr)),
    print("primes generated.")
    return numArr

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

    output = sorted(list(set(output)))
    return output

# Return a list of permutations of a list
def permute(arr):
    # Recursive?  Recursive.
    # Base case
    if len(arr) <= 1:
        return [arr]

    perms = []
    for elem in arr:
        reducedArr = list(arr)
        reducedArr.remove(elem)

        for perm in permute(reducedArr):
            perms.append([str(elem)] + perm)

    return perms

# Get all prime factors.
def getPrimeFactors(n, primeArr=None):
    # Takes prime array to reduce compute.
    if primeArr is None:
        primeArr = getPrimeArr(n)

    if n in primeArr:
        return [n]

    index = 0
    output = []
    while primeArr[index] <= n:
        if n % primeArr[index] == 0:
            output.append(primeArr[index])
            n /= primeArr[index]
        else:
            index += 1
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

    primefacs = getPrimeFactors(20)
    print("Primes factors of 20 : "),
    print(primefacs)

