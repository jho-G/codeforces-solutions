n,t=map(int,input().split())
orientation=list(map(str,input().strip()))

for _ in range(t):
    i=0
    while i<n-1:
        if orientation[i]=="B" and orientation[i+1]=="G":
            orientation[i],orientation[i+1]=orientation[i+1],orientation[i]
            i+=2
        else:
            i+=1
print("".join(orientation))
            