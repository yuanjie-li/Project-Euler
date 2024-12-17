# coding=utf-8
"""

PROBLEM 039 -Integer right triangles

Written by: Yuanjie Li
Date: June 26, 2018

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
import sys
sys.path.append('../utils')
import utils
import math

def main():
    max_sols = 0
    best_p = 0

    for p in range(12,1001):
        cur_sols = 0

        # For legs a and b...
        for a in range(1,p // 2):
            for b in range(a,p // 2):
                # Calculate c
                c = math.sqrt(math.pow(a,2) + math.pow(b,2))
                if (a + b + c) > p:
                    break
                if (a + b + c) == p:
                    cur_sols += 1

        if cur_sols > max_sols:
            max_sols = cur_sols
            best_p = p

    print("Most solutions: " + str(max_sols))
    print("Best perimeter: " + str(best_p))

if __name__ == "__main__":
    main()

