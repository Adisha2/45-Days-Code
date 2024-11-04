# cook your dish here
# Read the number of test cases
T = int(input())

# Initialize a list to store results
results = []

# Process each test case
for _ in range(T):
    N = int(input())
    
    # Check if N is divisible by 4
    if N % 4 == 0:
        results.append("Good")
    else:
        results.append("Not Good")

# Output all results
print("\n".join(results))
