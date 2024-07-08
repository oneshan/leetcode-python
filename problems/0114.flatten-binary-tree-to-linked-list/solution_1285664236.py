# 0114 - Flatten Binary Tree to Linked List
# Date: 2024-06-12
# Runtime: 37 ms, Memory: 16.6 MB
# Submission Id: 1285664236


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
        
        def recur(node):
            if not node:
                return
            
            if not node.left and not node.right:
                return node

            left_tail = recur(node.left)
            right_tail = recur(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail
        
        recur(root)