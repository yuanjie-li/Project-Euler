# coding=utf-8
"""

PROBLEM 019 - Counting Sundays

Written by: Yuanjie Li
Date: Oct 26, 2017

You are given the following information, but you may prefer to do some
research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.

    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""

def main():
    year = 1901
    count = 0       # number of sundays found
    day = 2         #: 0-6 value for the first of the year
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30,\
             10:31, 11:30, 12:31}

    for i in xrange(year, 2001):

        leap = False
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 4 == 0:
            leap = True

        for month in months:
            if day == 0:
                count += 1

            # Update for next month
            if leap and month == 2:
                day += ((months[month] + 1) % 7)
            else:
                day += (months[month] % 7)
            day = day % 7

    print(count)

if __name__ == "__main__":
    main()

