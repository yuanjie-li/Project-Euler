# coding=utf-8
"""

PROBLEM 024 - Lexicographic Permutations

Written by: Yuanjie Li
Date: Oct 25, 2017

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
5, 6, 7, 8 and 9?

"""
import sys
sys.path.append('../utils')
import utils

def main():
    num = ["0","1","2","3","4","5","6","7","8","9"]
    print("Generating permutations.  Please wait ...")
    perms = utils.permute(num)
    print("Permutations generated.  There are "),
    print(len(perms)),
    print(" permutations.")
    perms = sorted([''.join(x) for x in perms]) # Convert back to string

    print(perms[999999])

if __name__ == "__main__":
    main()

