# https://cses.fi/problemset/task/1070

# read the value of n 
n = int(input())

# if n is 1, the beautiful permutation is [1]
if n == 1: 
    print(1)

# if n is 2 or 3, there's no possible beautiful permutation
elif n == 2 or n == 3:
    print("NO SOLUTION")

# for n >= 4, print even numbers first, then odd numbers
else: 
    # print even numbers
    for i in range(2, n + 1, 2):
        print(i, end=" ")
    
    # print odd numbers 
    for i in range(1, n + 1, 2):
        print(i, end=" ")