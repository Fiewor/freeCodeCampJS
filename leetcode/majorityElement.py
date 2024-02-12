# https://leetcode.com/problems/majority-element/?envType=daily-question&envId=2024-02-12

def majorityElement(nums: list[int]) -> int:
    return [num for num in set(nums) if nums.count(num) > len(nums)//2][0]