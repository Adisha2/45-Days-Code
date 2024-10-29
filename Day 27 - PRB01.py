# cook your dish here
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    if is_prime(N):
        print("yes")
    else:
        print("no")
