# coding=utf-8
"""

PROBLEM 010 - Summation of Primes

Written by: Yuanjie Li
Date Jan 19, 2017

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import sys
import math
sys.path.insert(0, "../p003")
import largest_prime as lp

def main():
  # Starting from 5
  Output = 5
  for i in range(5, 2000000):
    # Print something to know it hasn't crashed
    if i > 999 and i % 1000 == 0:
      print i
    if lp.isPrime(i):
      Output += i

  print "Solution: " + str(Output)

if __name__ == "__main__":
  main()
