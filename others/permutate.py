def permutate(s: str) -> list[str]:
    if(len(s) == 1):
        return [s]
    
    res = []

    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i + 1:]

        perms = permutate(rest)

        for perm in perms:
            res.append(char + perm)

    return res


result = permutate('abc')
print(result)