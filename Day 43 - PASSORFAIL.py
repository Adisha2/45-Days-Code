# cook your dish here
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the inputs for each test case
    N, X, P = map(int, input().split())
    
    # Calculate the score
    score = 4 * X - N
    
    # Check if the score is greater than or equal to the passing marks
    if score >= P:
        print("PASS")
    else:
        print("FAIL")
        