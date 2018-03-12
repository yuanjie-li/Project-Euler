# coding=utf-8
"""

PROBLEM 034 - Digit Factorials

Written by: Yuanjie Li
Date: March 12, 2018

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
import math

def main():
    output = 0
    # Make list to hold the factorials calculated.
    facarr = [1,1,2,6]
    for i in range(4,10):
        facarr.append(getFactorial(i))

    num = 10
    while True: # TODO: Stopping condition
        numsum = 0
        strnum = str(num)
        for digit in strnum:
            numsum += facarr[int(digit)]
            if numsum > num:
                break

        if num == numsum:
            print(num)
            output += num
        num += 1
        if num > 1000000:
            break

    print "OUTPUT:", output


def getFactorial(n):
    output = 1
    for i in range(2,n+1):
        output *= i
    return output

if __name__ == "__main__":
    main()

