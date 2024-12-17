# coding=utf-8
import csv
"""

PROBLEM 067 - Maximum Path Sum II

Written by: Yuanjie Li
Date: Oct 22, 2017



By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

    [Below]

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 299
altogether! If you could check one trillion (1012) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)


"""

def main():

    triPath = "p067_triangle.txt"
    triangle = []

    # CSV read added here
    with open(triPath) as f:
        reader = csv.reader(f)
        for row in reader:
            row = [int(x) for x in row[0].split(" ")]
            triangle.append(row)

    # No recursion this time. Trade RAM to reduce operation time.
    sumLayer = triangle[-1]

    # Calculate bottom up
    for j in xrange(1,len(triangle)):

        nextLayer = triangle[-(j+1)]

        # Only save the larger of the two children
        sumLayer = [max(sumLayer[x], sumLayer[x+1]) \
                    for x in xrange(len(sumLayer)-1)]

        # What's in a name? Sum 'er up.
        sumLayer = [nextLayer[x] + sumLayer[x] \
                    for x in xrange(len(sumLayer))]

    print(sumLayer[0])

if __name__ == "__main__":
    main()

