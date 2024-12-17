# coding=utf-8
"""

PROBLEM 014 - Largest Collatz Sequence

Written by: Yuanjie Li
Date: Oct 16, 2017

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
def main():
    num = 13 # Start with 13, since it was in the example.
    best = 0

    # Iterate through, I suppose. Odds only.
    for i in xrange(15, 999999, 2):
        count = 0
        cur_num = i
        while cur_num != 1:
            if cur_num % 2 == 1:
                cur_num = 3 * cur_num + 1
                count += 1
            else:
                cur_num /= 2

        if count > best:
            best = count
            num = i

    print(num)

if __name__ == "__main__":
    main()

