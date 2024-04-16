# https://leetcode.com/problems/add-one-row-to-tree/?envType=daily-question&envId=2024-04-16

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, left=root)

    q = [(root, 1)]

    while q:
        node, curr_depth = q.pop()

        if curr_depth == depth - 1:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        
        else:
            if node.left: q.append((node.left, curr_depth+1))
            if node.right: q.append((node.right, curr_depth+1))
    
    return root