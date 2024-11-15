# cook your dish here
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the inputs for the test case
    N, A, B = map(int, input().split())
    
    # Calculate the number of odd and even indexed episodes
    odd_count = (N + 1) // 2  # Odd indexed episodes: positions 1, 3, 5, ...
    even_count = N // 2       # Even indexed episodes: positions 2, 4, 6, ...
    
    # Calculate total duration
    total_duration = odd_count * B + even_count * A
    
    # Output the result
    print(total_duration)
    