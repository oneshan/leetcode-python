# 0112 - Path Sum
# Date: 2022-10-23
# Runtime: 48 ms, Memory: 15.2 MB
# Submission Id: 828506006


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = deque([(root, 0)])
        while queue:
            node, curr_sum = queue.popleft()
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            if node.left: queue.append((node.left, curr_sum))
            if node.right: queue.append((node.right, curr_sum))
        return False