# https://leetcode.com/problems/even-odd-tree/?envType=daily-question&envId=2024-02-29 

# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isEvenOddTree(root: Optional[TreeNode]) -> bool:
    q = deque([root])
    even = True

    while q:
        prev = float('-inf') if even else float('inf')

        for _ in range(len(q)):
            node = q.popleft()
            
            if even and (node.val % 2 == 0 or node.val <= prev):
                return False
            
            elif not even and (node.val % 2 == 1 or node.val >= prev):
                return False
            
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
    
            prev = node.val

        even = not even
    return True

treeNode = TreeNode()
treeNode.val = 1
treeNode.left = TreeNode(10, TreeNode(3))
treeNode.left = TreeNode(4, TreeNode(7), TreeNode(9))
        #        1
        #     10   4
        # 3      7     9
print(isEvenOddTree(treeNode))