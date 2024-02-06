# https://leetcode.com/problems/group-anagrams/?envType=daily-question&envId=2024-02-06

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    map = {}

    for str in strs:
        key = ''.join(sorted(str))
        if key in map:
            map[key].append(str)
        else:
            map[key] = [str]

    return list(map.values())
    
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))