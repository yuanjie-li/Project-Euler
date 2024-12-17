# coding=utf-8
"""

PROBLEM 016 - Power Digit Sum

Written by: Yuanjie Li
Date: Oct 17, 2017

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

def main():

    # Types in pyton is cheating.  But it works.
    num = str(2**1000)
    output = 0

    for i in num:
        output += int(i)

    print(output)

if __name__ == "__main__":
    main()

