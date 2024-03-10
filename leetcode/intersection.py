# https://leetcode.com/problems/intersection-of-two-arrays/?envType=daily-question&envId=2024-03-10

# array approach
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    [res.append(num) for num in nums1 if num in nums2 and num not in res]
    return res

# set approach
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1).intersection(set(nums2)))
