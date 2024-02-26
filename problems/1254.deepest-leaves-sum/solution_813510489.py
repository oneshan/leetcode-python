# 1254 - Deepest Leaves Sum
# Date: 2022-10-02
# Runtime: 196 ms, Memory: 17.7 MB
# Submission Id: 813510489


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
        next_level = deque([root])
        while next_level:
            curr_level, next_level = next_level, deque()
            for node in curr_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
        return sum(node.val for node in curr_level)