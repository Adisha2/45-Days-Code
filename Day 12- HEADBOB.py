# cook your dish here
# Read number of observations
T = int(input())

# Process each observation
for _ in range(T):
    N = int(input())
    gestures = input().strip()
    
    if 'I' in gestures:
        print("INDIAN")
    elif 'Y' in gestures:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
