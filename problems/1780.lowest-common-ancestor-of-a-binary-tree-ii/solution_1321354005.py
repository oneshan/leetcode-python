# 1780 - Lowest Common Ancestor of a Binary Tree II
# Date: 2024-07-15
# Runtime: 142 ms, Memory: 21.2 MB
# Submission Id: 1321354005


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_lca(root, p, q):
            if not root:
                return None
            
            if root == p or root == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            return left or right

        def find_child(root, p):
            if not root:
                return None
            if root == p:
                return root
            return find_child(root.left, p) or find_child(root.right, p)

        node = find_lca(root, p, q)
        if find_child(node, p) and find_child(node, q):
            return node
        return None