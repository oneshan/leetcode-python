# 0098 - Validate Binary Search Tree
# Date: 2022-10-03
# Runtime: 45 ms, Memory: 17 MB
# Submission Id: 814303716


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.prev = float('-inf')
        if not root:
            return True
        self.inorder(root)
        return self.ans
    
    def inorder(self, node):
        if node.left: self.inorder(node.left)
        if self.prev >= node.val:
            self.ans = False
        self.prev = node.val
        if node.right: self.inorder(node.right)
    