# cook your dish here
def can_group_people(test_cases):
    results = []
    for n, preferences in test_cases:
        count = {}
        
        # Count how many people prefer each group size
        for p in preferences:
            if p in count:
                count[p] += 1
            else:
                count[p] = 1
        
        # Check if we can form the groups according to their preferences
        possible = True
        for size, num_people in count.items():
            if num_people % size != 0:
                possible = False
                break
        
        results.append("YES" if possible else "NO")
    
    return results

# Reading input and processing
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []
index = 1

for _ in range(T):
    N = int(data[index])
    P = list(map(int, data[index + 1].split()))
    test_cases.append((N, P))
    index += 2

results = can_group_people(test_cases)

# Printing results
for result in results:
    print(result)
    