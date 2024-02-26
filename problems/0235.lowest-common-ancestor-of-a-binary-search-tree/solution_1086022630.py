# 0235 - Lowest Common Ancestor of a Binary Search Tree
# Date: 2023-10-28
# Runtime: 69 ms, Memory: 20.8 MB
# Submission Id: 1086022630


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val > root.val:
            return root
        return self.lowestCommonAncestor(root.left if p.val < root.val else root.right, p, q)