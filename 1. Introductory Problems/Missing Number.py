# https://cses.fi/problemset/task/1083

# read the number n from input 
n = int(input())

# read the list of n - 1 numbers from input 
numbers = list(map(int, input().split()))

# sum of first n numbers 
expected_sum = n * (n + 1) // 2 

# sum of given numbers 
actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum
print(missing_number)