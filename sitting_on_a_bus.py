t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    occupied = set()
    valid = True
    
    for i, seat in enumerate(a):
        if i == 0:
            occupied.add(seat)
        else:
            if seat - 1 in occupied or seat + 1 in occupied:
                occupied.add(seat)
            else:
                valid = False
                break
    
    print("YES" if valid else "NO")
