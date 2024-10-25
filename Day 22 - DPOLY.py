# cook your dish here
def find_degree_of_polynomial(test_cases):
    results = []
    
    for N, coefficients in test_cases:
        # Iterate through coefficients in reverse order
        for degree in range(N - 1, -1, -1):
            if coefficients[degree] != 0:
                results.append(degree)
                break
                
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))

# Get results
results = find_degree_of_polynomial(test_cases)

# Print results
for result in results:
    print(result)
    