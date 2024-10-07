# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07

def minLength(self, s: str) -> int:
    st = [] 

    for ch in s:
        if ch == 'B' and len(st) and st[-1] == 'A':
                st.pop()
        elif ch == 'D' and len(st) and st[-1] == 'C':
                st.pop()
        else:
            st.append(ch)

    return len(st)


s = "ABFCACDB"
print(minLength(s))