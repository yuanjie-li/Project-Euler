# coding=utf-8
"""

PROBLEM 042 - Coded triangle numbers

Written by: Yuanjie Li
Date: June 26, 2018

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?

"""
import sys
sys.path.append('../utils')
import utils
import csv
import math

def main():
    text = []
    count = 0
    with open('../p042/p042_words.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            text += row
    for word in text:
        num = 0
        for letter in word.lower():
            num += ord(letter) - 96

        # Solve quadratic n^2 + n - num = 0
        plusx = (-1 + math.sqrt(math.pow(1,2) + 4 * 2 * num)) / 2
        minusx = (-1 - math.sqrt(math.pow(1,2) + 4 * 2 * num)) / 2

        if int(plusx) != plusx and int(minusx) != minusx:
            continue
        if int(plusx) == plusx:
            count += 1
        elif int(minusx) == minusx and minusx > 0:
            count += 1
    print("Count: %s" %count)



if __name__ == "__main__":
    main()

