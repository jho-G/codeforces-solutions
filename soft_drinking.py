n,k,l,c,d,p,nl,np=map(int,input().split())

total_drink=k*l
drink=total_drink//nl

total_limes=c*d
salt=p/np

max_toast=min(drink,total_limes,salt)
print(max_toast//n)