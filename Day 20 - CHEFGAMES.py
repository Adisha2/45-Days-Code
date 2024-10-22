# cook your dish here
def tennis_ball_decision(test_cases):
    results = []
    for decisions in test_cases:
        if all(decision == 0 for decision in decisions):
            results.append("IN")
        else:
            results.append("OUT")
    return results

# Input reading
T = int(input(" "))
test_cases = []

for _ in range(T):
    decisions = list(map(int, input().split()))
    test_cases.append(decisions)

# Get results
results = tennis_ball_decision(test_cases)

# Output results
for result in results:
    print(result)
    