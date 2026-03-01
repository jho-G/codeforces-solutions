t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_val = max(a)
    
    if a.count(max_val) == n:
        print(-1)
        continue
    
    for i in range(n):
        if a[i] == max_val:
            if (i > 0 and a[i-1] < a[i]) or (i < n-1 and a[i+1] < a[i]):
                print(i + 1)   # 1-based index
                break