# cook your dish here
def max_tastiness(test_cases):
    results = []
    for case in test_cases:
        a, b, c, d = case
        tastiness1 = a + c
        tastiness2 = a + d
        tastiness3 = b + c
        tastiness4 = b + d
        max_tastiness = max(tastiness1, tastiness2, tastiness3, tastiness4)
        results.append(max_tastiness)
    return results

# Input Reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = max_tastiness(test_cases)

# Output Results
for result in results:
    print(result)
    