# coding=utf-8
"""

PROBLEM 006 - Sum Square Difference

Written by: Yuanjie Li
Date Jan 19, 2017

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""
def main():
  SqSum = 0
  SumSq = 0

  for i in range(1, 100 + 1):
    SqSum += i * i
    SumSq += i

  Output = SumSq * SumSq - SqSum

  print Output

if __name__ == "__main__":
  main()
