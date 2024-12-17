# coding=utf-8
"""

PROBLEM 007 - 10,001st Prime

Written by: Yuanjie Li
Date Jan 19, 2017

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

"""
import sys
sys.path.insert(0, "../p003")
import largest_prime as lp

def main():
  End = 10001
  Prime = 3
  Output = 0
  # Starting prime number at 3.
  while End > 1:
    if lp.isPrime(Prime):
      Output = Prime
      End -= 1
    Prime += 2

  print Output

if __name__ == "__main__":
  main()
