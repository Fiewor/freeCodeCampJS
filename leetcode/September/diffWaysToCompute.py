# https://leetcode.com/problems/different-ways-to-add-parentheses/description/?envType=daily-question&envId=2024-09-19

from typing import List

def diffWaysToCompute(expression: str) -> List[int]:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    def backtrack(left, right):
        res = []

        for i in range(left, right+1):
            op = expression[i]
            if op in operations:
                nums1 = backtrack(left, i-1)
                nums2 = backtrack(i+1, right)
                for n1 in nums1:
                    for n2 in nums2:
                        res.append(operations[op](n1, n2))
        if res == []:
            res.append(int(expression[left:right+1]))

        return res
    
    return backtrack(0, len(expression)-1)

expression = "2*3-4*5"
print(diffWaysToCompute(expression))