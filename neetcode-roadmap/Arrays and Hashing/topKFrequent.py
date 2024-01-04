#  https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {num:nums.count(num) for num in nums}
    res = sorted(count, key=lambda x:count[x], reverse=True)
    return res[:k]

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))