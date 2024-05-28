# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/?envType=daily-question&envId=2024-05-27


def specialArray(self, nums: List[int]) -> int:
    x = 0

    while x <= len(nums):
        count = len([num for num in nums if num >= x])
        if count == x: return x
        x += 1

    return -1