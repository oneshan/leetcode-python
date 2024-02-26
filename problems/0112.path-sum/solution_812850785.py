# 0112 - Path Sum
# Date: 2022-10-02
# Runtime: 91 ms, Memory: 15.2 MB
# Submission Id: 812850785


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
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return (self.hasPathSum(root.left, targetSum)
                or self.hasPathSum(root.right, targetSum))