# https://leetcode.com/problems/group-anagrams/?envType=daily-question&envId=2024-02-06

from collections import defaultdict
from typing import List

# time complexity -> O(m.nlogn) where m is the number of strings in strs and n is the average length of a string in strs
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    map = {}

    for str in strs:
        key = ''.join(sorted(str))
        if key in map:
            map[key].append(str)
        else:
            map[key] = [str]

    return list(map.values())

# time complexity -> O(m.n)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        res[tuple(count)].append(s)

    return res.values()

    
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))