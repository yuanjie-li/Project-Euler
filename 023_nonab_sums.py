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
    upper = 28123 # Upper bound as defined above
    abNums = []   # Array of abundant numbers

    for i in xrange(2, upper):
        divs = utils.getDivs(i)
        if sum(divs[:-1]) > i:
            abNums.append(i)
    print(str(len(abNums)) + " abundant numbers found.")

    # Generate a list of all abnum sums. It's gonna be large.
    abSums = [False] * (upper + 1) # 0 indexed
    for i in xrange(len(abNums)):
        # Early stop
        if abNums[i] > upper / 2:
            break
        for j in xrange(i, len(abNums)):
            num = abNums[i] + abNums[j]
            # Early stop
            if num > upper:
                break
            abSums[num] = True

    print(sum(abSums)),
    print("sums generated.")

    for i, abSum in enumerate(abSums):
        if not abSum:
            output += i

    print(output)

if __name__ == "__main__":
    main()

