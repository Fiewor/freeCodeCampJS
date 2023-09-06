# https://leetcode.com/problems/maximum-subarray

# greedy solution
def maxSubArray(self, nums: list[int]) -> int:
    res = nums[0]
    total = 0

    for num in nums:
        total += num
        res = max(res, total)

        if total < 0:
            total = 0

    return res

# DP tabulation solution
def maxSubArrayTab(self, nums: list[int]) -> int:
    n = len(nums)
    tab = [0] * n
    tab[0] = max_sum = nums[0]

    for i in range(1, n):
        tab[i] = max(tab[i - 1] + nums[i], nums[i])
        max_sum = max(tab[i], max_sum)

    return max_sum