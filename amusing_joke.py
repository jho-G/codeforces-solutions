guest=input().upper()
host=input().upper()
next_morning=input().upper()


if sorted(guest+host)==sorted(next_morning):
    print("YES")
else:
    print("NO")