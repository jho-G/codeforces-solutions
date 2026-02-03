n=int(input())
db={}
for _ in range(n):
    user_name=input().strip()
    if user_name not in db:
        db[user_name] = 1
        print("OK")
    else:
        print(f"{user_name}{db[user_name]}")
        db[user_name] += 1