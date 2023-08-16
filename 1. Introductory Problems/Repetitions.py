# https://cses.fi/problemset/task/1069

# read the DNA sequence from input 
dna_sequence = input()

# initialize the counters 
current_count = 1 # to keep track of current streak of identical characters
max_count = 1 # store the maximmum streak

for i in range(1, len(dna_sequence)):
    # if current character is same as previous character:
    if dna_sequence[i] == dna_sequence[i - 1]:
        # increment current count 
        current_count += 1 
        # update max_count if current_count exceeds it
        max_count = max(max_count, current_count)
    else: 
        # reset current_count for a new character streak
        current_count = 1

print(max_count)
