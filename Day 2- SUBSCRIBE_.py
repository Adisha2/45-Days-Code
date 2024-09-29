# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read N and X for each test case
    N, X = map(int, input().split())
    
    # Calculate the number of subscriptions needed
    subscriptions_needed = (N + 5) // 6
    
    # Calculate the total cost
    total_cost = subscriptions_needed * X
    
    # Print the result for this test case
    print(total_cost)

