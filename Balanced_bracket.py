def isValid(s):
    st = []
    mp = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mp.values():
            st.append(ch)
        else:
            if not st or st[-1] != mp[ch]:
                return False
            st.pop()
    return len(st) == 0
