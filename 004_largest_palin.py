# coding=utf-8

"""

PROBLEM 004 - Largest Palindrome Product

Written by: Yuanjie Li
Date Jan 19, 2017

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# I wanted to time this solution vs. brute force
from datetime import datetime as dt

def main():
  Start = dt.now()
  Fac1 = 999
  Fac2 = 999
  Largest = 0
  Product = 999 * 999

  # Variables for early stop
  Fac1Large = 0
  Fac2Large = 0
  for i in range(1, Fac1 - Fac1 / 10):
    Fac2 = 999
    for j in range(1, Fac2 - Fac2 / 10):
      if Fac1 < Fac2Large and Fac2 < Fac2Large:
        print "Solution: " + str(Largest)
        print "This solution took " + str(dt.now() - Start) + "."
        return
      Fac2 -= 1
      Product = Fac1 * Fac2
      if isPalin(Product) and Product > Largest:
        Largest = Product
        Fac1Large = Fac1
        Fac2Large = Fac2
    Fac1 -= 1

  """
  # Brute Foce
  print "Solution: " + str(Largest)
  print "This solution took " + str(dt.now() - Start) + "."
  """

# Helper to determine if number is palindromic
def isPalin(i):
  # Make into an array of single digits, preserving the order.
  # E.g. 1234 -> [1, 2, 3, 4]
  IArr = [int(d) for d in str(i)]
  for digit in range(0, len(IArr) / 2 + 1):
    if IArr[digit] != IArr[-(digit + 1)]:
      return False
  return True

if __name__ == "__main__":
  main()
