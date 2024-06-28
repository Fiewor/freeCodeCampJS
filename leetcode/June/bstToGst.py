# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/?envType=daily-question&envId=2024-06-25

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstToGst(root: TreeNode) -> TreeNode:
    currSum = 0

    def dfs(node):
        nonlocal currSum

        if not node:
            return
        
        dfs(node.right)
        
        currSum += node.val
        node.val = currSum
        
        dfs(node.left)
        
    dfs(root)
    return root