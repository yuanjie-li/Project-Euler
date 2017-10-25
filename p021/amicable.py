# coding=utf-8
"""

PROBLEM 021 - Amicable Numbers

Written by: Yuanjie Li
Date: Oct 23, 2017



Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then
a and b are an amicable pair and each of a and b are called amicable
numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
# Helper to generate a primes arr
def isPrime(num, primeArr):
    for prime in primeArr:
        if num % prime == 0:
            return False
        elif num ** 0.5 <= prime:
            break
    return True

# Helper to sum up the factors and stuff
def sumDivs(num, primeArr):

    divArr = [num]
    output = 1

    # Get all the prime factors
    for prime in primeArr:
        if num % prime == 0 and num != prime:
            divArr.append(prime)

    return output

def main():

    primeArr = [2, 3, 5, 7, 11]
    # Make the primes arr real quick.
    for i in xrange(13,10000,2):
        if isPrime(i,primeArr):
            primeArr.append(i)
    print("Primes array generated. " + str(len(primeArr)) +
            " primes found.")

    output = 0
    pairs = [] # list of stuff to skip

    print(sumDivs(220, primeArr))
    print(sumDivs(284, primeArr))

    """
    for i in xrange(5,285):
        if i in pairs:
            pass

        divSum = sumDivs(i, primeArr)
        pair = sumDivs(divSum, primeArr)
        if pair >= 10000:
            pass
        elif divSum == pair:
            print("found a pair : " + str(divSum) + " " + str(pair))
            pairs.append(pair)
            output += divSum + pair
    """

    print(output)

if __name__ == "__main__":
    main()

