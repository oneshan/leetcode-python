# 1254 - Deepest Leaves Sum
# Date: 2022-12-03
# Runtime: 201 ms, Memory: 17.7 MB
# Submission Id: 853842879


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return total