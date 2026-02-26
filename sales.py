n,m=map(int,input())
pricess=list(map(int,input().split()))

negative_prices=[p for p in prices if p<0]

negatie_prices.sort()

max_take=negative_prices[:m]

money=abs(sum(max_take))

print(money)


