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

import sys
sys.path.insert(0, '../utils')
import utils

def main():
    output = 0

    for i in range(1, 10000):
        divs = utils.getDivs(i)
        divSum = sum(divs[:-1])
        if divSum == i:
            # Ignore cases where it sums to itself
            pass
        elif i == sum(utils.getDivs(divSum)[:-1]):
            # Only i is added, because its counterpart will be calculated
            # again later on.
            output += i

    print(output)

if __name__ == "__main__":
    main()

