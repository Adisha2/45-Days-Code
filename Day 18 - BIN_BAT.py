# cook your dish here
def total_event_time(T, test_cases):
    results = []
    for case in test_cases:
        N, A, B = case
        # Calculate the number of rounds
        rounds = N.bit_length() - 1
        
        # Calculate total time
        total_time = (rounds * A) + ((rounds - 1) * B)
        results.append(total_time)
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(tuple(map(int, input().split())))

# Get results
results = total_event_time(T, test_cases)

# Output results
for result in results:
    print(result)
    