# cook your dish here
def atm_withdrawals(test_cases):
    results = []
    
    for case in test_cases:
        N, K = case[0]
        withdrawals = case[1]
        
        current_balance = K
        result = []
        
        for amount in withdrawals:
            if current_balance >= amount:
                result.append('1')
                current_balance -= amount
            else:
                result.append('0')
        
        results.append(''.join(result))
    
    return results

# Input handling
T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, K), A))

# Get the results
output = atm_withdrawals(test_cases)

# Print output
for res in output:
    print(res)
