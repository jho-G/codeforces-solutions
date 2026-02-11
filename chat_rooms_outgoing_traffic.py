count=0
total_treafic=0

while True:
    try:
        line=input().strip()
        if not line:
            continue

        if line[0]=='+':
            count+=1
        elif line[0]=='-':
            count-=1
        else:
            parts=line.split(':',1)
            message_len=len(parts[1]) if len(parts)>1 else 0
            total_trafic+=len(part[1])*count
    except EOFError:
        break
print(total_trafic)

