# cook your dish here
def max_trace(N, matrix):
    max_trace_value = -float('inf')  # To track the maximum trace
    
    # Iterate over all possible submatrix sizes from 1x1 to NxN
    for l in range(1, N + 1):
        # Iterate over all possible top-left corners (r, c) for the submatrix
        for r in range(N - l + 1):
            for c in range(N - l + 1):
                # Calculate the trace of the submatrix of size l starting at (r, c)
                trace = 0
                for i in range(l):
                    trace += matrix[r + i][c + i]  # Sum the diagonal elements
                # Update the maximum trace found so far
                max_trace_value = max(max_trace_value, trace)
    
    return max_trace_value

# Input handling
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())  # Size of the matrix
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # Calculate and print the maximum trace for this test case
    print(max_trace(N, matrix))
