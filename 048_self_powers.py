import math 
from tqdm import tqdm

if __name__ == "__main__": 

    output = 1
    for i in tqdm(range(2, 1001)): 
        cur_pow = i
        last10 = i
        for j in range(i-1):
            cur_pow = last10 * i
            last10 = cur_pow % 10000000000 

        output += last10
        output %= 10000000000
    print(output)

