# https://cses.fi/problemset/task/1094

# number of elements in the array
n = int(input())

# read the array 
arr = list(map(int, input().split()))

# initialize the number of moves to 0
moves = 0 

for i in range(1, n):
    # if current element is smaller than its predecessor 
    if arr[i] < arr[i - 1]:
        # add the difference to moves and update the current element
        moves += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]

print(moves)