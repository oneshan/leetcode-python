# 0110 - Balanced Binary Tree
# Date: 2023-01-01
# Runtime: 60 ms, Memory: 18.6 MB
# Submission Id: 869096995


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(node):
            if not node:
                return True, -1
            is_valid, left = helper(node.left)
            if not is_valid:
                return False, 0
            is_valid, right = helper(node.right)
            if not is_valid:
                return False, 0
            return abs(left-right) < 2, max(left, right) + 1
        
        is_valid, height = helper(root)
        return is_valid