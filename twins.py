n=int(input())
coins=list(int,input().split())

coins.sort(reverse=True)
total=sum(coins)

my_coins=0
count=0

for coin in coins:
    my_coins+=coin
    count+=1
    if my_coins>total-my_coins:
        break
print(count)

