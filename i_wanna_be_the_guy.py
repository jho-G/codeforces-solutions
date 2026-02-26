n=int(input())
p=list(map(int,input()).split()[1:])
q=list(map(int,input()).split()[1:])

all_levels=p|q
if len(all_levels)==n:
    print("I became the guy.")
else:
    print("oh,my keyboard!")
