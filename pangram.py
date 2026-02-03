num_of_chars=int(input())
chars=input().lower()

unique_chars=set(chars)
alphabets=set("abcdefghijklmnopqrstuvwxyz")

if alphabets.issubset(unique_chars):
    print("YES")
else:
    print("NO")