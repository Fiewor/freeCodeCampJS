# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import Counter
from typing import List

def uniqueOccurrences(self, arr: List[int]) -> bool:
    vals = Counter(arr).values()
    return len(vals) == len(set(vals))