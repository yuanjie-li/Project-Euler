# coding=utf-8
"""

PROBLEM 023 - Non-abundant Sums

Written by: Yuanjie Li
Date: Oct 24, 2017

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.

"""

import sys
sys.path.insert(0, '../utils')
import utils

def main():

    output = 0
    abNums = [] # Array of abundant numbers

    for i in xrange(1, 28123): # Upper bound defined by problem
        divs = utils.getDivs(i)
        if sum(divs[:-1]) > i:
            abNums.append(i)

    abNums = sorted(list(set(abNums)))
    print(str(len(abNums)) + " abundant numbers found.")

    # Generate a list of all abnum sums. It's gonna be large.
    abSums = []
    for i in xrange(len(abNums)):
        if abNums[i] >= 28123:
            break
        for j in xrange(i, len(abNums)):
            if abNums[i] + abNums[j] >= 28123:
                break
            abSums.append(abNums[i] + abNums[j])

    abSums = sorted(list(set(abSums)))
    print("Sums generated.")

    for i in range(1, 28123):
        # Ticker
        if i % 1000 == 0:
            print(i)
        if i not in abSums:
            output += i

    print(output)

if __name__ == "__main__":
    main()

