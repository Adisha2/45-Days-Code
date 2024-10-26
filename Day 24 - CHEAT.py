# cook your dish here
def count_tuesdays(N):
    if N < 2:
        return 0
    return (N - 2) // 7 + 1

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    results.append(count_tuesdays(N))

print('\n'.join(map(str, results)))
