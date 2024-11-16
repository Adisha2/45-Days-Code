# cook your dish here
def encode_message(N, S):
    # Step 1: Swap adjacent characters
    S_list = list(S)
    
    # Swap adjacent pairs
    for i in range(0, N - 1, 2):
        S_list[i], S_list[i + 1] = S_list[i + 1], S_list[i]
    
    # Step 2: Replace each letter with its "mirrored" counterpart
    for i in range(N):
        S_list[i] = chr(219 - ord(S_list[i]))  # 219 = ord('a') + ord('z')
    
    # Join the list into a string and return
    return ''.join(S_list)

# Read input
T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Length of the string (not really needed)
    S = input()  # The input string
    print(encode_message(N, S))
    