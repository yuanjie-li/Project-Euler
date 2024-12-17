# coding=utf-8
"""

PROBLEM 005 - Smallest Multiple

Written by: Yuanjie Li
Date Jan 19, 2017

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""
import sys
import math
sys.path.insert(0, "../p003")
import largest_prime as lp

def main():
  # Just do the primes.  Solution expanded to allow for more complex solutions
  Start = 1
  End = 20
  Output = 1
  for i in range(Start, End + 1):
    # If the number is prime
    if lp.isPrime(i):
      Output *= i
      # Or if the number has a square / cube / etc. less than the end value
      exp = 2
      while i > 1 and math.pow(i, exp) < End:
        Output *= i
        exp += 1

  print Output

if __name__ == "__main__":
  main()
