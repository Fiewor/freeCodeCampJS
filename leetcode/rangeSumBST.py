# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive approach
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    if root.val > high:
        return self.rangeSumBST(root.left, low, high)
    if root.val < low:
        return self.rangeSumBST(root.right, low, high)
    return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# iterative solution (using BFS)
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    # traverse tree (BFS or DFS)
    # if node val within range, add to count
    # return count

    count = 0
    q = []
    q.append(root)
    while len(q) > 0:
        node = q[0]

        if node.val >= low and node.val <= high:
            count += node.val
        if node.left:
            q.append(node.left)        
        if node.right:
            q.append(node.right)

        q.pop(0)

    return count  