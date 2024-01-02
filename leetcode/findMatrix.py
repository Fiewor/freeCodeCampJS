# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/submissions/?envType=daily-question&envId=2024-01-02

def findMatrix(nums: list[int]) -> list[list[int]]:
    # solution 1
    mat = []
    new = []
    left = []

    for num in nums:
        if num in new:
            left.append(num)
        else:
            new.append(num)
    mat.append(new)

    if len(left) > 0:
        mat += findMatrix(left)
    
    return mat

    # solution 2
    freq = [0] * (len(nums) + 1)

    res = []

    for num in nums:
        if freq[num] >= len(res):
            res.append([])
        
        res[freq[num]].append(num)
        freq[num] += 1

    return res

nums = [1,3,4,1,2,3,1]
ans = findMatrix(nums)
print(ans)