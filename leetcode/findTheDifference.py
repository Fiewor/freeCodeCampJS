# https://leetcode.com/problems/find-the-difference/?envType=daily-question&envId=2023-09-25

def findTheDifference(self, s: str, t: str) -> str:
    # --- hash-map
    # t_map = {}

    # for char in t:
    #     if char in t_map:
    #         t_map[char] += 1
    #     else:
    #         t_map[char] = 1
    
    # for char in s:
    #     if t_map[char] == 1:
    #         del t_map[char]
    #     else:
    #         t_map[char] -= 1
    
    # return list(t_map.keys())[0]


    # --- trick to pass diff - didn't pass large testcase
    # for i in range(len(s)):
    #     diff = ord(t[i]) - ord(s[i])
    #     t = t[:i+1] + chr(diff % 0x110000) + t[i+1:]
    # return t[-1]

    # --- diff between sum
    # s_sum = t_sum = 0

    # for char in s:
    #     s_sum += ord(char)

    # for char in t:
    #     t_sum += ord(char)

    # return chr(t_sum - s_sum)


    # --- less readable, one-line sum
    return chr(sum(ord(char) for char in t) - sum(ord(char) for char in s))