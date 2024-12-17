# coding=utf-8
"""

PROBLEM 043 - Sub-string divisibility

Written by: Yuanjie Li
Date: June 26, 2018

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""
import sys
sys.path.append('../utils')
import utils
import math

def main():
    print("Getting permutes ...")
    all_pans = utils.permute([0,1,2,3,4,5,6,7,8,9])
    print("Done.")
    output = 0
    primeArr = [2,3,5,7,11,13,17]

    for pan in all_pans:
        for i in range(1,8):
            subpan = pan[i:i+3]
            joined = ""
            for ch in subpan:
                joined += str(ch)
            joined = int(joined)

            if joined % primeArr[i-1] != 0:
                break
            elif i == 7:
                joined = ""
                for ch in pan:
                    joined += str(ch)
                output += int(joined)
    print(output)

if __name__ == "__main__":
    main()

