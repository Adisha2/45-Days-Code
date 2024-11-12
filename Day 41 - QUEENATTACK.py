# cook your dish here
def queen_attack(N, X, Y):
    # Horizontal and Vertical attacks
    horizontal_vertical_attacks = 2 * (N - 1)
    
    # Diagonal attacks
    top_left = min(X - 1, Y - 1)
    top_right = min(X - 1, N - Y)
    bottom_left = min(N - X, Y - 1)
    bottom_right = min(N - X, N - Y)
    
    diagonal_attacks = top_left + top_right + bottom_left + bottom_right
    
    # Total attacks (excluding the Queen's own position)
    total_attacks = horizontal_vertical_attacks + diagonal_attacks
    return total_attacks

# Input processing
T = int(input())  # Number of test cases
for _ in range(T):
    N, X, Y = map(int, input().split())
    print(queen_attack(N, X, Y))
    