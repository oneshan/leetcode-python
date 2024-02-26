# 0110 - Balanced Binary Tree
# Date: 2022-12-06
# Runtime: 105 ms, Memory: 19 MB
# Submission Id: 855454338


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return True, -1
            
            is_balanced ,left_height = helper(node.left)
            if not is_balanced:
                return False, 0
            
            is_balanced, right_height = helper(node.right)
            if not is_balanced:
                return False, 0
            
            return (abs(left_height - right_height) < 2,
                    1 + max(left_height, right_height))
        
        return helper(root)[0]