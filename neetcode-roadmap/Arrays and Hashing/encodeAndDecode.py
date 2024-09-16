# https://leetcode.com/problems/encode-and-decode-strings/description/

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for str in strs:
            res += f"{len(str)}" + "#" + str
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) #count
            i = j + 1 # start of character after count
            j = i + length # end of character
            res.append(s[i:j])
            i = j #move i to next sequence of {count}#{characters}

        return res
    
