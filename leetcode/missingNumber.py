# https://leetcode.com/problems/missing-number/?envType=daily-question&envId=2024-02-20

# loop
def missingNumber(nums: list[int]) -> int:
    for i in range(len(nums)+1):
        if i not in nums:
            return i

# XOR
def missingNumber(nums: list[int]) -> int:
    res = len(nums)
    for i in range(len(nums)):
        res ^= i
        res ^= nums[i]
    return res

nums = [3,0,1]
print(missingNumber(nums))