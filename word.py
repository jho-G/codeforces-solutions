s=input()

num_of_upper=0
num_of_lower=0

for i in s:
    if i.isupper():
        num_of_upper+=1
    else:
        num_of_lower+=1


if num_of_upper>num_of_lower:
    print(s.upper())
else:
    print(s.lower())