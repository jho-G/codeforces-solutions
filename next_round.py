n,k=map(int,input().split())
scores=list(map(int,input().split()))

count=0
index=scores[k-1]

for score in scores:
    if score>=index and score>0:
        count+=1
print(count)