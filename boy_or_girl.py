user_name = input().lower()

distinct_letters = set(user_name)

if len(distinct_letters) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
