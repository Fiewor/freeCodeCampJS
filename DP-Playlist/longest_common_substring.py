# substring
# order must be maintained
# you're NOT allowed to jump characters i.e. it MUST be contiguous


def longest_common_substring(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    tab = [[0] * (m + 1) for _ in range(n + 1)]
    
    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if i >= 1 and j - 1 >= 1:
                if s2[i - 1] == s1[j - 1]:
                    tab[i][j] = 1 + tab[i - 1][j - 1]
                    ans = max(ans, tab[i][j])
    return ans


# space-optimized
def longest_common_substring(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)

    prev = curr = [0] * (m + 1)
    
    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if i >= 1 and j - 1 >= 1:
                if s2[i - 1] == s1[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    ans = max(ans, curr[j])

        prev = curr
    return ans

print(f'tab: {longest_common_substring("abcjklp", "acjkp")}')
print(f'space-optimized: {longest_common_substring("abcjklp", "acjkp")}')