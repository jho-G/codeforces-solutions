a1,a2,a3,a4=map(int,input().split())
strips=input()
count=0

for i in strips:
    if strips[i]=="1":
        count+=a1
    elif strips[i]=="2":
        count+=a2
    elif strips[i]=="3":
        count+=a3
    else:
        count+=a4
print(count)

# values=list(map(int,input()))
# strips=input()
# count=0

# for i in strips:
#     count+=values[int(i)-1]