# https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative DFS
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    sum = 0
    q = deque([root])
    
    while q:
        node = q.pop()

        if node.left:
            if not node.left.left and not node.left.right: # is leaf node
                sum += node.left.val
            q.append(node.left)
        
        if node.right:
            q.append(node.right)

    return sum
    

# recursive DFS
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    sum = 0

    if root.left:
        if not root.left.left and not root.left.right: # is leaf node
            sum += root.left.val
        else:
            sum += sumOfLeftLeaves(root.left)
    
    sum += sumOfLeftLeaves(root.right)

    return sum