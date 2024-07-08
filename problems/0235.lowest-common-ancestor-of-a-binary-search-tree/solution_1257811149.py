# 0235 - Lowest Common Ancestor of a Binary Search Tree
# Date: 2024-05-14
# Runtime: 49 ms, Memory: 20.4 MB
# Submission Id: 1257811149


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

        if p == root or q == root:
            return root

        if p.val < root.val < q.val:
            return root

        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)