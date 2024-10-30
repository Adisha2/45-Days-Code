# cook your dish here
import math

# Read number of test cases
T = int(input())
results = []

for _ in range(T):
    # Read A, B, K for each test case
    A, B, K = map(int, input().split())
    
    # Calculate the distance
    distance = abs(A - B)
    
    # Calculate the minimum steps required
    if distance == 0:
        results.append(0)
    else:
        steps = math.ceil(distance / K)
        results.append(steps)

# Print all results for the test cases
for result in results:
    print(result)
