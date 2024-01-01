# https://leetcode.com/problems/assign-cookies/

def findContentChildren(g: list[int], s: list[int]) -> int:
    contentBrats = 0

    # satisfy higher needs first (using bogger cookies, of course)
    children = sorted(g, reverse=True)
    cookies = sorted(s, reverse=True)

    cookie_index = child_index = 0

    while cookie_index < len(s) and child_index < len(g):
        if cookies[cookie_index] >= children[child_index]: #cookie can satisfy current child
            contentBrats += 1 
            cookie_index += 1 # move to next cookie
            child_index += 1 # move to next child
        else: #cookie is smaller than current child's need so move to next less-greedier child
            child_index += 1

    print(contentBrats)

# g = [1,2,3]
# s = [1,1]
g = [1, 2]
s = [1, 2, 3]
findContentChildren(g, s)