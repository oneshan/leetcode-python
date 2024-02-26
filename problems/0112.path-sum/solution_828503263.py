# 0112 - Path Sum
# Date: 2022-10-23
# Runtime: 100 ms, Memory: 15.1 MB
# Submission Id: 828503263


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)
        return left or right