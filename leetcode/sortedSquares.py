# https://leetcode.com/problems/squares-of-a-sorted-array/?envType=daily-question&envId=2024-03-02

def sortedSquares(nums: list[int]) -> list[int]:
    return sorted([num**2 for num in nums])
