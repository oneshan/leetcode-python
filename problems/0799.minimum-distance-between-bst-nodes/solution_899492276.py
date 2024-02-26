# 0799 - Minimum Distance Between BST Nodes
# Date: 2023-02-17
# Runtime: 43 ms, Memory: 13.9 MB
# Submission Id: 899492276


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.ans