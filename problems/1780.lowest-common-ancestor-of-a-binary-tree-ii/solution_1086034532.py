# 1780 - Lowest Common Ancestor of a Binary Tree II
# Date: 2023-10-28
# Runtime: 227 ms, Memory: 30.2 MB
# Submission Id: 1086034532


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if not node:
                return 0
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)    
            mid = (node == p) or (node == q)
            if left + right + mid >= 2:
                self.ans = node
            return left or right or mid

        self.ans = None
        dfs(root, p, q)
        return self.ans