# coding=utf-8
"""

PROBLEM 026 - Reciprocal Cycles

Written by: Yuanjie Li
Date: Oct 26, 2017

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.

"""
# Use decimal for increased precision
from decimal import *

def main():

    output = 0 # Minimum it's 1/3
    numer = Decimal(1)
    getcontext().prec = 2000

    for num in range(3,1000,2): # only care about evens
        print("Number : "),
        print(num)
        denom = Decimal(num)
        frac = Decimal(numer / denom)

        # Convert to string, no leading 0's
        frac = str(int(str(frac).split(".")[1]))
        if len(frac) > 1:
            # Loop 1: Iterate through substrings, incase repeat starts later
            for sub in range(len(frac)):
                subfrac = frac[sub:]

                # Nest loops to find the repeats
                for i in range(len(subfrac)//2):
                    for j in xrange(0,len(subfrac)//2 * 2,2):
                        if subfrac[:i] == subfrac[i:j] and j-i > 0:
                            if j-i > output:
                                print("Repeat found : "),
                                print(numer),
                                print("/"),
                                print(denom)
                                print(subfrac[:i])
                                print(subfrac[i:j])
                                output = denom
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break

    print(output)

if __name__ == "__main__":
    main()

