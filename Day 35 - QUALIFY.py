# cook your dish here
# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read X, A, B for the current test case
    X, A, B = map(int, input().split())
    
    # Calculate the total points Chef scored
    total_points = A * 1 + B * 2
    
    # Check if Chef qualifies
    if total_points >= X:
        print("Qualify")
    else:
        print("NotQualify")
        