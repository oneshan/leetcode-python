# 0530 - Minimum Absolute Difference in BST
# Date: 2022-10-03
# Runtime: 99 ms, Memory: 16.2 MB
# Submission Id: 814285488


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev = None
        self.inorder(root)
        return self.ans
        
    def inorder(self, node):
        if node.left: self.inorder(node.left)
        
        if self.prev is not None:
            self.ans = min(self.ans, node.val - self.prev)
        self.prev = node.val
        
        if node.right: self.inorder(node.right)