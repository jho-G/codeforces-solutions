n=int(input())
count=0
coins=[100,20,10,5,1]

for coin in coins:
    count+=n//coin
    n=n%coin

print(count)