# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/?envType=daily-question&envId=2024-01-10

from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    graph = defaultdict(list)
    stack = [(root, None)]

    while stack:
        node, parent = stack.pop()

        if parent:
            graph[parent.val].append(node.val)
            graph[node.val].append(parent.val)
        
        if node.left:
            stack.append((node.left, node))
        
        if node.right:
            stack.append((node.right, node))
        
    time = -1
    visited = {start}
    queue = deque([start])

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        time += 1
    
    return time