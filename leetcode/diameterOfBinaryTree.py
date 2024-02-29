# https://leetcode.com/problems/diameter-of-binary-tree/?envType=daily-question&envId=2024-02-27

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    maxi = 0

    def dfs(root):
        nonlocal maxi
        
        if not root:
            return -1
        
        left = dfs(root.left)
        right = dfs(root.right)

        diameter = left + right + 2
        maxi = max(maxi, diameter)

        height = 1 + max(left, right)
        return height

    dfs(root)
    return maxi
