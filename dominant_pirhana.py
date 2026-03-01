#csec_cpd_b_1
t=int(input())
n=int(input())

a=list(map(int,input()))

for i in a:
    if a[i-1]<a[i] and a[i+1]<a[i]:
        a[i]=a[i]+1
        print(a[i])
    else:
        print(-1)