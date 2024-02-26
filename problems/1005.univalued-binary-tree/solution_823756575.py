# 1005 - Univalued Binary Tree
# Date: 2022-10-16
# Runtime: 30 ms, Memory: 13.9 MB
# Submission Id: 823756575


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def recursion(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            left = recursion(node.left)
            right = recursion(node.right)
            return left and right
        
        return recursion(root)