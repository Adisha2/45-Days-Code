# cook your dish here
# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read Dragon's scores
    dragon_scores = list(map(int, input().split()))
    # Read Sloth's scores
    sloth_scores = list(map(int, input().split()))
    
    # Calculate total scores
    dragon_total = sum(dragon_scores)
    sloth_total = sum(sloth_scores)
    
    # Determine the rank based on the given rules
    if dragon_total > sloth_total:
        print("Dragon")
    elif sloth_total > dragon_total:
        print("Sloth")
    else:
        # If total scores are tied, check DSA scores
        if dragon_scores[0] > sloth_scores[0]:
            print("Dragon")
        elif sloth_scores[0] > dragon_scores[0]:
            print("Sloth")
        else:
            # If DSA scores are tied, check TOC scores
            if dragon_scores[1] > sloth_scores[1]:
                print("Dragon")
            elif sloth_scores[1] > dragon_scores[1]:
                print("Sloth")
            else:
                # If everything is tied
                print("Tie")
