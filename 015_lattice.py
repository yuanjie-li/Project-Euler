# coding=utf-8
import numpy as np
"""

PROBLEM 015 - Lattice Paths

Written by: Yuanjie Li
Date: Oct 17, 2017

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""
def main(size):

    # num sides + 1, since they're vertices, not edges
    numArr = np.zeros((size+1, size+1))

    # The number of paths to any one square is equal to the sum of the paths
    # to the two adjacent squares.  The top and left edges can be initialized
    # to 1, since there is ever only one way there.
    for i in range(size+1):
        numArr[i][0] = 1
        numArr[0][i] = 1

    # But once you get here, it makes sense to use memory to store this,
    # speeding it up from O(2^n)? to O(n^2).  k
    for i in xrange(1, size+1):
        for j in xrange(1,size+1):
            numArr[i][j] = numArr[i-1][j] + numArr[i][j-1]

    print(int(numArr[size][size]))

if __name__ == "__main__":
    main(20)

