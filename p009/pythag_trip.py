# coding=utf-8
"""
PROBLEM 9: Special Pythagorean Triplet
Written by: Yuanjie Li
Date Jan 19, 2017

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def main():
  Output = [1,2,3]

  # The sum of a, b, c must be less than 1001, so bound loops as such
  for i in range(1,334):
    for j in range(i+1, (1000 - i) / 2 + 1):
      for k in range(j+1, 1000 - i - j + 1):
        if i * i + j * j == k * k and i + j + k == 1000:
          Output = i * j * k

  print Output

if __name__ == "__main__":
  main()
