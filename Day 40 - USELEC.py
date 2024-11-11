# cook your dish here
for t in range(int(input())):

    n,x = map(int,input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    cnt = 0
    for i in range(n):
        if B[i]>=A[i]:
            C.append(B[i]-A[i]+1)
        else:
            cnt += 1
    C.sort()
    for i in C:
        x -= i 
        if x>=0:
            cnt += 1 
    print('YES' if cnt>(n//2) else 'NO')
    
        