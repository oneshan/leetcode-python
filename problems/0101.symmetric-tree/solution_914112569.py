# 0101 - Symmetric Tree
# Date: 2023-03-13
# Runtime: 35 ms, Memory: 14 MB
# Submission Id: 914112569


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.recur(root.left, root.right)
        
    def recur(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.recur(left.left, right.right) and self.recur(left.right, right.left)