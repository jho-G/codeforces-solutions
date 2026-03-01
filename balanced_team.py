n = int(input())
a = list(map(int, input().split()))

a.sort()

l = 0
max_team = 0

for r in range(n):
    while a[r] - a[l] > 5:
        l += 1
    max_team = max(max_team, r - l + 1)

print(max_team)