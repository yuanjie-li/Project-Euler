"""

PROBLEM 003 - Largest Prime Factor

Written by: Yuanjie Li
Date: Jan 19, 2017

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
# Arr of primes under 5
PrimeArr = [2, 3]

def main():

  Remaining = 600851475143
  NextLargest = 3

  while 1:
    # Set a breaking point
    if NextLargest * 2 > Remaining:
      break
    # See if current is a factor; increment current to next prime
    if Remaining % NextLargest == 0:
      Remaining /= NextLargest

    while 1:
      NextLargest += 2
      if isPrime(NextLargest):
        break

  print Remaining

# Helper to determine if a number is prime
def isPrime(Num):
  for Factor in PrimeArr:
    if Num % Factor == 0:
      return False
    elif Factor ** 2 > Num:
      break
  PrimeArr.append(Num)
  return True

if __name__ == "__main__":
  main()
