num_of_game=int(input())
str1=input().strip()
count_A=str1.count('A')
count_D=str1.count('D')
if count_A>count_D:
    print("Anton")
elif count_D>count_A:
    print("Danik")
else:
    print("Friendship")

# n=int(input())
# games=input().strip()
# count_a=games.count('A')
# count_d=games.count('D')
# if count_a>count_d:
#     print("Anton")
# elif count_d>count_a:
#     print("Danik")
# else:
#     print("friendship")
