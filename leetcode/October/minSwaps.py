# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/?envType=daily-question&envId=2024-10-08

def minSwaps(self, s: str) -> int:
    max_count = 0
    count_closing = 0

    for char in s:
        if char == '[':
            count_closing -= 1
        else:
            count_closing += 1
        max_count = max(max_count, count_closing)

    return (max_count + 1)//2

print(minSwaps(s = "][]["))