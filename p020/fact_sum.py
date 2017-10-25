# coding=utf-8
"""

PROBLEM 020 - Factorial Digit Sum

Written by: Yuanjie Li
Date: Oct 23, 2017

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
def main():
    # Python is cheating.
    fact = 100
    for x in xrange(2,100):
        fact *= x

    print(sum([int(x) for x in str(fact)]))

if __name__ == "__main__":
    main()

