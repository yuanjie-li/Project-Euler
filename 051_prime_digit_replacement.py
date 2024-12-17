import math 
from tqdm import tqdm
import itertools

def isPrime(n): 
    if n <= 0 or n % 2 == 0: return False 

    # Stop at the square root, round up 
    lim = int(n ** 0.5) + 1 
    for i in range(3, lim, 2):
        if n % i == 0:
            return False 
    
    return True 

def makeSingleFamily(n, idx):
    str_n = str(n)
    str_n = list(str_n)
    if idx == 0:
        start = 1
    else:
        start = 0
    
    output = []
    for i in range(start, 10):
        str_n[idx] = str(i)
        output.append(int(''.join(str_n)))
    
    return output

def makeFamily(n): 
    for idx in range(len(str(n))): 
        single = makeSingleFamily(n, idx) 
        single = [x for x in single if isPrime(x)]

        if len(single) == 8:
            print(single)
            print(n)
            return single

if __name__ == "__main__": 

    next_prime = 17

    # Find all consecutive primes up to 1,000,000
    while True: 

        if not isPrime(next_prime):
            next_prime += 2
            continue 

        makeFamily(next_prime)

        next_prime += 2


