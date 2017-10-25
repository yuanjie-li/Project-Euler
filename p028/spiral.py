# coding=utf-8
"""

PROBLEM 028 - Number Spiral Diagnoals

Written by: Yuanjie Li
Date: Oct 25, 2017

Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

"""

def main():
    edge = 5                    # Starting with the 1-10
    output = 1 + 3 + 5 + 7 + 9  # Still need to add 13, 17, 21, 25
    index = 9                   # The last value added

    while edge < 1002:
        # Per edge, add 4 numbers, separated by edge - 1
        for i in range(4):
            index += edge - 1
            output += index
        edge += 2

    print(output)

if __name__ == "__main__":
    main()

