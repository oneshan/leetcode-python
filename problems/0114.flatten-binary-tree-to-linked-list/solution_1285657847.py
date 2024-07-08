# 0114 - Flatten Binary Tree to Linked List
# Date: 2024-06-12
# Runtime: 44 ms, Memory: 16.6 MB
# Submission Id: 1285657847


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev_right = None

        def recur(node):
            if not node:
                return
            
            recur(node.right)
            recur(node.left)
            
            node.right = self.prev_right
            node.left = None
            self.prev_right = node
        
        recur(root)