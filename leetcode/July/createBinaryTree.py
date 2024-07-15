# https://leetcode.com/problems/create-binary-tree-from-descriptions/?envType=daily-question&envId=2024-07-15

# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes = {}
    children = set()

    for par, child, is_left in descriptions:
        children.add(child)

        if par not in nodes:
            nodes[par] = TreeNode(par)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        if is_left:
            nodes[par].left = nodes[child]
        else:
            nodes[par].right = nodes[child]

    for par, _, _ in descriptions:
        if par not in children:
            return nodes[par]

descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]  
print(createBinaryTree(descriptions))