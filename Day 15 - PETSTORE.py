# cook your dish here
def can_alice_and_bob_have_same_multiset(test_cases):
    results = []
    for animals in test_cases:
        from collections import Counter
        count = Counter(animals)
        
        # Check if all counts are even
        if all(c % 2 == 0 for c in count.values()):
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    animals = list(map(int, input().split()))
    test_cases.append(animals)

# Process and output results
results = can_alice_and_bob_have_same_multiset(test_cases)
for result in results:
    print(result)
    