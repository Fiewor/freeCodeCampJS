# https://leetcode.com/problems/number-of-good-pairs/

def numIdenticalPairs(self, nums: List[int]) -> int:
    #--- using formula
    # count = {}
    # for i in range(len(nums)):
    #     if nums[i] in count:
    #         count[nums[i]] += 1
    #     else:
    #         count[nums[i]] = 1

    # res = 0
    # seen = {}
    
    # for num in nums:
    #     n = count[num]
    #     if num not in seen and n > 1:
    #         res += n * (n - 1) // 2
    #         seen[num] = True
    
    # return res

    #---simpler approach
    ans = 0
    count = {}
    for num in nums:
        if num in count:
            ans += count[num]
            count[num] += 1
        else:
            count[num] = 1
    return ans
