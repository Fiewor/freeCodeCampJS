# https://leetcode.com/problems/find-common-characters/?envType=daily-question&envId=2024-06-05

from collections import Counter
from typing import List

def commonChars(words: List[str]) -> List[str]:
    res = []
    count = Counter(words[0])

    for word in words:
        curr_count = Counter(word)

        for char in count:
            count[char] = min(count[char], curr_count[char])
        
    for key in count:
        for _ in range(count[key]):
            res.append(key)

    return res

words = ["bella","label","roller"]
print(commonChars(words))
