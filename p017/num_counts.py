# coding=utf-8
"""

PROBLEM 017 - Number Letter Counts

Written by: Yuanjie Li
Date: Oct 17, 2017

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""
def main():

    # There are some patterns, but it's easier to hardcode.
    ones = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
    teens = {11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}
    tens = {1:3, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    hundred = 7

    output = 11 # includes 'one thousand'
    for i in xrange(1,1000):
        # hundred
        h = (i % 1000) // 100
        # tens
        t = (i % 100)

        if ones.has_key(h):
            output += ones[h] # The number preceeding
            output += hundred # The word
            if t != 0:
                output += 3   # 'and', when needed

        if teens.has_key(t):
            output += teens[t] # English 11-19 is wonky
        else:
            if tens.has_key(t//10):
                output += tens[t//10]  # The other 20-99

            if ones.has_key(t%10):    # And any ones
                output += ones[t%10]

    print(output)

if __name__ == "__main__":
    main()

