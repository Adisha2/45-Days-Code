# cook your dish here
def determine_service(T, cases):
    results = []
    for P, Q in cases:
        total_points = P + Q
        # Determine the group of serves
        serve_group = total_points // 2
        if serve_group % 2 == 0:
            results.append("Alice")
        else:
            results.append("Bob")
    return results

# Read input
T = int(input())
cases = []
for _ in range(T):
    P, Q = map(int, input().split())
    cases.append((P, Q))

# Get results and print them
results = determine_service(T, cases)
for result in results:
    print(result)
