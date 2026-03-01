#csec_cpd_E_2

n=int(input())
a=list(map(int,input().split()))


count=0
sorted_a=a.sort()
max_a=sorted_a[-1]

for i in a:
    if max_a-a[i]<=5:
        count+=1
        
print(count)

