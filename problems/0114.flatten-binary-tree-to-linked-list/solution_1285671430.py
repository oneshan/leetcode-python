# 0114 - Flatten Binary Tree to Linked List
# Date: 2024-06-12
# Runtime: 49 ms, Memory: 16.8 MB
# Submission Id: 1285671430


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
        
        if not root:
            return None

        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            node = node.right