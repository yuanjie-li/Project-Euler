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

def cull_sample(l, item): 

    # After removing this item, only keep items less than 
    # remainder of 1,000,000 to reduce sample size 

    remainder = 1000000 - item 
    if remainder > item: 
        remainder = item 
    l = [x for x in l if x <= remainder]

    return l

if __name__ == "__main__": 

    starting_prime = [2,3,5,7,11,13]
    output = {}

    # Find all consecutive primes up to 1,000,000
    for prime in starting_prime:

        prime_list = [2,3,5,7,11,13]
        prime_list = [x for x in prime_list if x >= prime]
        next_prime = prime_list[-1] + 2
        output[1] = 41

        while True: 

            if isPrime(next_prime):
                prime_list.append(next_prime)
            else: 
                next_prime += 2
                continue 

            consec = sum(prime_list)
            if consec > 1000000:
                break
            if isPrime(consec): 
                output[len(prime_list)] = consec
            

            next_prime += 2
    
    print(output[sorted(output)[-1]])
