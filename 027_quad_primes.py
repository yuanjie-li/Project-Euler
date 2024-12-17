# coding=utf-8
"""

PROBLEM 027 - Quadratic Primes

Written by: Yuanjie Li
Date: Oct 25, 2017

Euler discovered the remarkable quadratic formula:

    n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41n=40,
40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,
41^2+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes
for the consecutive values 0≤n≤79. The product of the coefficients, −79 and
1601, is −126479.

Considering quadratics of the form:

        n^2+an+b, where |a|<1000 and |b|≤1000

        where |n| the modulus/absolute value of n
        e.g. |11|=11 and |−4|=4

Find the product of the coefficients, aa and bb, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
import sys
sys.path.append('../utils')
import utils
import math

def quad(n, a, b):
    return n**2 + a * n + b

def main():
    limit = 100000
    a = -999
    b = -1000
    best = 0
    prod = a * b

    # Get a prime array of 10,000 primes
    print("Generating prime array...")
    primeArr = utils.getPrimeArr(limit)
    print("Done.")

    # Reduce access time of prime array
    isPrime = [False] * limit
    for prime in primeArr:
        isPrime[prime] = True

    # Iterate
    print("Beginning iterations...")
    while a < 1000:
        b = -1000
        while b <= 1000:
            # Only care about cases where b is prime, since 0^2 + a * 0 + b
            # must be prime.
            if isPrime[int(math.fabs(b))]:
                n = 0
                count = 0

                while isPrime[int(math.fabs(quad(n,a,b)))]:
                    count += 1
                    n += 1

                if count > best:
                    best = count
                    prod = a * b
            b += 1
        a += 1

    print(prod)

if __name__ == "__main__":
    main()

