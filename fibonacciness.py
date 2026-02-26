n=int(input())

for _ in range(n):
    a1,a1,a4,a5=map(int,input().split())
    
    c1=a1+a2
    c2=a4-a2
    c3=a5-a4
    if c1==c2==c3:
        print(3)
    elif c1==c2 or c2==c3 or c1==c3:
        print(2)
    else:
        print(1)


