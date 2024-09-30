def can_obtain_stick(N, X):
    """
    Determine if a stick of length X can be obtained from a stick of length N
    while maintaining the same parity.

    :param N: Length of the original stick
    :param X: Desired length of the stick
    :return: "YES" if X can be obtained, "NO" otherwise
    """
    if N % 2 == 0:  # N is even
        return "YES"
    else:  # N is odd
        return "YES" if X % 2 == 1 else "NO"

# Read input
T = int(input())
results = []

for _ in range(T):
    N, X = map(int, input().split())
    result = can_obtain_stick(N, X)
    results.append(result)

# Output results
for res in results:
    print(res)
