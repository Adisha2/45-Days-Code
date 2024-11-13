# cook your dish h
for i in range(int(input())):

    n=int(input())

    s=list(map(int,input().split()))
    k=int(input())
    c=s[k-1]
    x=0
    for j in range(0,len(s)):
        if(c>s[j]):
            x+=1
    print(x+1)