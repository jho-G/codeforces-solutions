t=int(input())

for _ in range(t):

    n,k=map(int,input().split())
    I=0

    x=list(map(int,input().split()))
    seen=set()

    for i in x:
        if k-i in seen:
            I+=1
        seen.add(i)
    print(I)










    


