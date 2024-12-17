# coding=utf-8
"""

PROBLEM 030 - Digit Fifth Powers

Written by: Yuanjie Li
Date: Oct 25, 2017

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

def fifthSum(number):
    output = 0
    for digit in number:
        output += int(digit) ** 5
    return output

def main():
    output = 0

    # What is the stopping condition?  Possibilities:
    #   Num of digits < num in sum  --DOESN'T WORK--
    #   Hard code a large number    --1,000,000 works--
    #   Can it be improved?
    number = "2"

    lastNum = "2" # Just to see where the stop condition is

    while 1:
        fifSum = fifthSum(number)

        # Stop
        if int(number) > 1000000:
            print("Stopping at :"),
            print(number)
            break

        if int(number) == fifSum:
            output += fifSum
            lastNum = number

        number = str(int(number) + 1)

    print("The last number found was :"),
    print(lastNum)

    print("Sum :"),
    print(output)

if __name__ == "__main__":
    main()

