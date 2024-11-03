# cook your dish here
def find_winner_and_lead(n, scores):
    cumulative_score1 = 0
    cumulative_score2 = 0
    max_lead = 0
    winner = 0
    
    for score in scores:
        Si, Ti = score
        cumulative_score1 += Si
        cumulative_score2 += Ti
        
        if cumulative_score1 > cumulative_score2:
            lead = cumulative_score1 - cumulative_score2
            if lead > max_lead:
                max_lead = lead
                winner = 1
        else:
            lead = cumulative_score2 - cumulative_score1
            if lead > max_lead:
                max_lead = lead
                winner = 2

    return winner, max_lead

# Read input
N = int(input().strip())
scores = [tuple(map(int, input().strip().split())) for _ in range(N)]

# Get the result
W, L = find_winner_and_lead(N, scores)

# Print the output
print(W, L)
