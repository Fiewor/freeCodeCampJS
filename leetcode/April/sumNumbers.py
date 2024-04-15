# https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/1233184769/?envType=daily-question&envId=2024-04-15

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        total_sum = 0

        while q:
            node = q.pop()

            if not node.left and not node.right:
                total_sum += node.val

            if node.left:
                node.left.val += node.val * 10
                q.append(node.left)

            if node.right:
                node.right.val += node.val * 10
                q.append(node.right)

        return total_sum