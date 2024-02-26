# 1254 - Deepest Leaves Sum
# Date: 2022-12-03
# Runtime: 205 ms, Memory: 18 MB
# Submission Id: 853842619


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
        curr_level, next_level = deque([root]), deque()
        while curr_level:
            total = 0
            for _ in range(len(curr_level)):
                node = curr_level.popleft()
                total += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            curr_level, next_level = next_level, curr_level
        return total