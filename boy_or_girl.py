username = input().strip()  
unique_letters = set(username)

if len(unique_letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")