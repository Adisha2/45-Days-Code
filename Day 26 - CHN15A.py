# cook your dish here
def count_wolverine_like_minions(test_cases):
    results = []
    for case in test_cases:
        N, K, initial_values = case
        count = 0
        for value in initial_values:
            if (value + K) % 7 == 0:
                count += 1
        results.append(count)
    return results

# Input handling
T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    initial_values = list(map(int, input().split()))
    test_cases.append((N, K, initial_values))

# Get the results
results = count_wolverine_like_minions(test_cases)

# Output the results
for result in results:
    print(result)
    