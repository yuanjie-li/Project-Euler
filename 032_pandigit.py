# coding=utf-8
"""

PROBLEM 032 - Pandigital Products

Written by: Yuanjie Li
Date: March 6, 2018

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

"""

def main():

    limit = 9876 # The largest an multiplicand can be

    check = ['1','2','3','4','5','6','7','8','9']

    prods = []
    for i in range(1, limit):
        stri = str(i)
        # No duplicates
        if len(stri) == len(set(list(stri))):

            for j in range(1, limit):
                # Early stop
                if i * j >= 9876:
                    break
                strj = str(j)
                # No duplicates
                if len(stri + strj) == len(set(list(stri) + list(strj))):

                    prod = i * j
                    strprod = str(prod)
                    # Check correctness
                    if check == sorted(list(strprod + stri + strj)):
                        prods.append(prod)

    print(sum(list(set(prods))))

if __name__ == "__main__":
    main()

