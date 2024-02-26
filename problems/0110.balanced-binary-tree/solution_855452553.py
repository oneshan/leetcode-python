# 0110 - Balanced Binary Tree
# Date: 2022-12-06
# Runtime: 140 ms, Memory: 18.6 MB
# Submission Id: 855452553


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(node):
            if not node:
                return 0
            left = get_height(node.left)
            right = get_height(node.right)
            if abs(left - right) > 1:
                return float('inf')
            return 1 + max(left, right)
        
        return get_height(root) != float('inf')