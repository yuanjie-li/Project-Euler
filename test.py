def main():
    total = 0
    # For numbers in range 3 to 999, inclusive
    for i in range(3, 1000):
        # Is number divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            # Sum
            total += i

    # Print the sum
    print total

def fibonacci():
    total = 2
    sequence = [1,1,2]
    # Keep going until newnum > 4,000,000
    while (sequence[2] < 4000000):
        # move sliding window
        sequence[0] = sequence[1]
        sequence[1] = sequence[2]
        # Generate the next number in the sequence.
        sequence[2] = sequence[0] + sequence[1]

        # Is number even
        if sequence[2] % 2 == 0:
            #sum
            total += sequence[2]
    print total

if __name__ == "__main__":
    fibonacci()

