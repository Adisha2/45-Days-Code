# cook your dish here
def is_possible_score_change(test_cases):
    results = []
    for A, B, C, D in test_cases:
        if C >= A and D >= B:
            results.append("POSSIBLE")
        else:
            results.append("IMPOSSIBLE")
    return results

# Read input
T = int(input().strip())
test_cases = []
for _ in range(T):
    A, B = map(int, input().strip().split())
    C, D = map(int, input().strip().split())
    test_cases.append((A, B, C, D))

# Get results and print them
results = is_possible_score_change(test_cases)
for result in results:
    print(result)
