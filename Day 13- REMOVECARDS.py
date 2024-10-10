# cook your dish here
def min_moves_to_uniform_cards(test_cases):
    results = []
    for case in test_cases:
        N = case[0]
        cards = case[1]
        
        # Count frequencies of card values (1 to 10)
        frequency = [0] * 11  # Index 0 to 10, where index corresponds to card value
        for card in cards:
            frequency[card] += 1
        
        # Find the maximum frequency
        max_frequency = max(frequency)
        
        # Minimum moves required is total cards minus the max frequency
        min_moves = N - max_frequency
        results.append(min_moves)
    
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    test_cases.append((N, cards))

# Calculate results
results = min_moves_to_uniform_cards(test_cases)

# Output results
for result in results:
    print(result)
