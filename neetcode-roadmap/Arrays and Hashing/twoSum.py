# https://leetcode.com/problems/two-sum/

def twoSum(self, nums: List[int], target: int) -> list[int]:

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in nums and nums.index(diff) != i:
            return [i, nums.index(diff)]