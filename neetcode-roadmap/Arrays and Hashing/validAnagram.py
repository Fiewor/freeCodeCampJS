# https://leetcode.com/problems/valid-anagram

# one map
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map = {i:s.count(i) for i in s}

    for i in t:
        if i not in map:
            return False
        map[i] -= 1
    
    for val in map.values():
        if val != 0:
            return False
    
    return True

# two maps
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    c_s = {i:s.count(i) for i in s}
    c_t = {i:t.count(i) for i in t}
    
    for key, val in c_t.items():
        if key not in c_s or c_s[key] != val:
            return False
    
    return True
