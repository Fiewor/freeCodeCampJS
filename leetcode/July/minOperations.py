# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

import re
from typing import List

def minOperations(logs: List[str]) -> int:
    count = 0

    for log in logs:
        if bool(re.match(r"^\.{2}", log)):
            if count: count -= 1
        else:
            if not bool(re.match(r"^\.", log)):
                count += 1

    return count


logs = ["d1/","d2/","../","d21/","./"]
print(minOperations(logs))
