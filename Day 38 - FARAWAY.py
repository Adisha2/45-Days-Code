# cook your dish here
# cook your dish here

for i in range(int(input())):

    n,m=map(int,input().split())
    lst=list(map(int, input().split()))
    lst.sort()
    sm=0
    for j in lst:
        ele=max(abs(1-j),abs(m-j))
        sm+=ele
    print(sm)