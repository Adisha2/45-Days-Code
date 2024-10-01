# cook your dish here
def min_operations_to_make_same(t, test_cases):
    results = []
    for case in test_cases:
        n, array = case
        frequency = {}
        
        # Count the frequency of each element
        for num in array:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Find the maximum frequency
        max_frequency = max(frequency.values())
        
        # Minimum operations required
        min_operations = n - max_frequency
        results.append(min_operations)
    
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    test_cases.append((n, array))

# Get results
results = min_operations_to_make_same(t, test_cases)

# Output results
for result in results:
    print(result)
