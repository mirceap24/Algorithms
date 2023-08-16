# https://cses.fi/problemset/task/1068

def collatz_sequence(n):
    # initialize the result list with the starting value of n 
    result = [n]

    # continue until n becomes 1 
    while n != 1: 
        # if n is even, divide it by 2 
        if n % 2 == 0:
            n //= 2 
        # if n is odd, multiply it by 3 and add 1 
        else: 
            n = n * 3 + 1 
        # append the new value of n to the result list 
        result.append(n)
    
    return n 

n = int(input())
sequence = collatz_sequence(n)
print(' '.join(map(str, sequence)))
