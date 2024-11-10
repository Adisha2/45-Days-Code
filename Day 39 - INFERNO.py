# cook your dish here
for _ in range(int(input())):
    N,X = map(int,input().split())
    H = list(map(int,input().split()))
    sin_count=0
    mul_count=0
    for i in range(len(H)):
        if H[i]<=X:
            sin_count+=1
        else:
            temp = H[i]
            while temp>X or temp>0:
                sin_count+=1
                temp = temp-X
    mul_count = max(H)
    print(min(sin_count,mul_count))