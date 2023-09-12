# def helper(n: int, k: int, arr: list[int]) -> bool:
#     prev = [False] * (k + 1)
#     curr = [False] * (k + 1)

#     prev[0] = True
#     curr[0] = True

#     if(arr[0] <= k):
#         prev[arr[0]] = True

#     for i in range(1, n):
#         for target in range(1, k+1):
#             take = False if arr[i] > target else prev[target - arr[i]]
#             noTake = prev[target]

#             curr[target] = take or noTake
        
#         prev = curr
    
#     return prev[k]


# def canPartition(arr: list[int]) -> bool:
#     n = len(arr)
#     total_sum = 0

#     for item in arr:
#         total_sum += item
    
#     if(total_sum % 2): #if odd, it can't be split into two equal subsets/partitions
#         return False
    
#     target = total_sum // 2 

#     return helper(n - 1, target, arr) # checks if subset of given arr contains target

# res = canPartition([2, 3, 3, 3, 4, 5])

def helper(self, n, k, nums):
    if k == 0:
        return True
    if n == 0:
        return nums[0] == k

    notTake = self.helper(n - 1, k, nums)
    take = False
    if(nums[n] <= k):
        take = self.helper(n - 1, k - nums[n], nums)
    
    return take or notTake            
        
def canPartition(nums: list[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    target = total_sum // 2

    if target % 2 != 0:
        return False

    return helper(n-1, target, nums)

# res = canPartition([1, 2, 3, 5])
res = canPartition([1, 5, 11, 5])
print(res)
