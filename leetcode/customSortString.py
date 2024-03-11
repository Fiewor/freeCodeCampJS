# https://leetcode.com/problems/custom-sort-string/?envType=daily-question&envId=2024-03-11

# initial approach(works)
def customSortString(order: str, s: str) -> str:
    res = [""] * len(s)
    other = ""
    count = Counter(s)

    for char in s:
        i = order.find(char)

        if i != -1:
            res[i] = char * count[char]
        else:
            other += char

    return "".join(res) + other

# more straight-forward hashmap approach
def customSortString(order: str, s: str) -> str:
    res = ""
    count = Counter(s)

    for char in order:
        if char in count:
            res += char * count[char]
            del count[char]
    
    for char, count in count.items():
        res += char * count

    return res
