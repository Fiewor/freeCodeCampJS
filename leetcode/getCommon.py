# https://leetcode.com/problems/minimum-common-value/?envType=daily-question&envId=2024-03-09

from typing import List

def getCommon(nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        res = float('inf')

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return res if res != float('inf') else -1

nums1 = [1, 2, 3]
nums2 = [2, 4]

print(getCommon(nums1, nums2))
