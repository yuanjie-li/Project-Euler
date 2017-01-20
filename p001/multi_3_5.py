"""

PROBLEM 001 - Multiples of 3 and 5

Written by: Yuanjie Li
Date: Jan 19, 2017

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def main():
  Output = 0

  for i in range(3,1000):
    if i % 5 == 0:
      Output += i
    elif i % 3 == 0:
      Output += i

  print Output

if __name__ == "__main__":
  main()

