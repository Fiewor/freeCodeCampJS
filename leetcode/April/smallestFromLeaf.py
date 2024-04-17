# https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17


from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    q = deque([root])
    arr = []

    while q:
        node = q.pop()

        if not node.left and not node.right:
            if isinstance(node.val, str):
                ls = list(map(int, node.val.split('.')))
                res = [chr(97 + i) for i in ls]
                arr.append("".join(res))
            else:
                arr.append(chr(97+node.val))

        if node.left:
            node.left.val = str(node.left.val) + '.' + str(node.val)
            q.append(node.left)
        
        if node.right:
            node.right.val = str(node.right.val) + '.' + str(node.val)
            q.append(node.right)
    
    return min(arr)

def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    ans = None

    def dfs(node, path):
        nonlocal ans
        if not node:
            return
        
        path += [chr(ord('a') + node.val)]

        if not node.left and not node.right:
            curr_str = "".join(path[::-1])

            if ans is None or curr_str < ans:
                ans = curr_str
            
        dfs(node.left, path)    
        dfs(node.right, path)    
        
        path.pop()

    dfs(root, [])
    return ans