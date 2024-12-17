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


if __name__ == "__main__": 

    for i in tqdm(range(1001, 9999, 2)): 

        output = []

        # Generate all permutations
        str_i = str(i) 
        str_i = (str_i)
        str_i = itertools.permutations(str_i)
        perms = []
        for perm in str_i:
            perm = int(''.join(perm))
            # Limit to reduce futile loops
            if perm >= i and perm not in perms:
                perms.append(perm)

        perms = sorted(perms) 

        for perm in perms:
            if isPrime(perm):
                output.append(perm)
            
        if len(output) != 3: 
            continue 

        diff1 = output[1] - output[0]
        diff2 = output[2] - output[1]
        if diff1 == diff2: 
            print(output)


