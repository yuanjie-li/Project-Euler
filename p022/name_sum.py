# coding=utf-8
import csv
"""

PROBLEM 022 - Name Scores

Written by: Yuanjie Li
Date: Oct 24, 2017

Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

def main():

    namePath = "p022_names.txt"
    names = []
    output = 0

    # CSV read
    with open(namePath) as f:
        reader = csv.reader(f)
        for row in reader:
            for name in row:
                names.append(name)

    # Python sort
    names = sorted(names)

    # Expression to go from ascii to int :
    # ord('A') - 0x40

    for i in xrange(len(names)):
        output += (i+1) * sum([ord(x) - 0x40 for x in names[i]])
    print(output)

if __name__ == "__main__":
    main()

