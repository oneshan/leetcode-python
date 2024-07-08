# 0235 - Lowest Common Ancestor of a Binary Search Tree
# Date: 2024-05-14
# Runtime: 57 ms, Memory: 20.2 MB
# Submission Id: 1257813295


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

        while root:
            if p.val == root.val or q.val == root.val:
                return root
            if p.val < root.val < q.val:
                return root
            if root.val > p.val:
                root = root.left
            else:
                root = root.right