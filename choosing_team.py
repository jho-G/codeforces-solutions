n,k=map(int,input())
lists=list(map(int,input()))

count=0

for i in lists:
    if i+k<=5:
        count+=1

print(count//3)