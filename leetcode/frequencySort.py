# https://leetcode.com/problems/sort-characters-by-frequency/?envType=daily-question&envId=2024-02-07

from collections import Counter
import heapq

def frequencySort(s: str) -> str:
    freq = Counter(s)
    res = ''
    arr = sorted(list(freq.items()), key=lambda x:x[1], reverse=True)

    for key, val in arr:
        count = val

        while count > 0:
            res += key
            count -= 1

    return res

def frequencySort(s: str) -> str:
    freq = Counter(s)
    arr = list(sorted(freq.items(), key=lambda x:x[1], reverse=True))
    return ''.join(char * freq for char, freq in arr)

def frequencySort(s: str) -> str:
    res = ''
    freq = Counter(s)
    pq = [(-freq, char) for char, freq in freq.items()]
    heapq.heapify(pq)

    while pq:
        freq, char = heapq.heappop(pq)
        res += char * -freq

    return res

# s = "tree"
s = "loveleetcode"
print(frequencySort(s))