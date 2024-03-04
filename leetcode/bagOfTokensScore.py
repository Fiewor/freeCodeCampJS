# https://leetcode.com/problems/bag-of-tokens/?envType=daily-question&envId=2024-03-04

def bagOfTokensScore(tokens: list[int], power: int) -> int:
    n = len(tokens)
    score = max_score = 0
    i, j = 0, n - 1

    while i <= j:
        if power >= tokens[i]:
            power -= tokens[i]
            i += 1
            score += 1
            max_score = max(max_score, score)

        else:
            if score > 0:
                power += tokens[j]
                j -= 1
                score -= 1
            else: break

    return max_score

        
# tokens = [200, 100]
# power = 150
# tokens = [100]
# power = 50
tokens = [100,200,300,400]
power = 200
# tokens = [26]
# power = 51
# tokens = [71,55,82]
# power = 54
print(bagOfTokensScore(tokens, power))