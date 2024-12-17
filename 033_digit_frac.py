# coding=utf-8
"""

PROBLEM 033 - Digit Cancelling Fractions

Written by: Yuanjie Li
Date: March 6, 2018

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""
import math

def main():
    outnum = 1
    outdenom = 1

    for i in range(11,99):
        if i % 10 == 0:
            continue
        for j in range(i+1, 100):
            stri = str(i)
            strj = str(j)
            simpi = [x for x in stri if x not in strj]
            simpj = [x for x in strj if x not in stri]

            # len 2 == no match; len 0 == too many
            if len(simpi) == 1 and len(simpj) == 1:
                num = int(simpi[0])
                denom = int(simpj[0])
                wrong_factor = simplify(num, denom)
                simpnum = num / wrong_factor
                simpdenom = denom / wrong_factor
                factor = simplify(i,j)
                simpi = i / factor
                simpj = j / factor

                if simpnum == simpi and simpdenom == simpj:
                    print("Original:")
                    print(str(i) + "/" + str(j))
                    print("Simplified:")
                    print(str(simpnum) + "/" + str(simpdenom))
                    print

                    # Join to output
                    outnum *=i
                    outdenom *=j
    factor = simplify(outnum, outdenom)

    print "OUTPUT:",outdenom / factor


# Simplify fractions
def simplify(m, n):
    m_divs = getDivs(m)
    n_divs = getDivs(n)

    div_smaller = m_divs if len(m_divs) <= len(n_divs) else n_divs
    div_larger = m_divs if len(m_divs) > len(n_divs) else n_divs

    # Iterate through the larger one first (hope for early stop)
    for factor in reversed(div_larger):
        if factor in div_smaller:
            return factor
    return 1

# Get all divisors of n (non-prime)
def getDivs(n):

    maxF = n # Maximum factor, stopping condition
    output = [1,n]
    if n == 4:
        return [1,2,4] # Fails for loop

    for x in xrange(2, n // 2):
        if x + 1 == maxF:
            break
        if n % x == 0:
            output.append(x)
            output.append(n / x)

            maxF = n / x

    output = sorted(output)
    return output

if __name__ == "__main__":
    main()

