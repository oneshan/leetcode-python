# 0543 - Diameter of Binary Tree
# Date: 2022-10-14
# Runtime: 72 ms, Memory: 16.4 MB
# Submission Id: 822342697


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.traverse(root)
        return self.ans
        
    def traverse(self, node):
        if node is None:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.ans = max(self.ans, left+right)
        return 1 + max(left, right)