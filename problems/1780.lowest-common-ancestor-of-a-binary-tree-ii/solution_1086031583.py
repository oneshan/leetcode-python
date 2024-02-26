# 1780 - Lowest Common Ancestor of a Binary Tree II
# Date: 2023-10-28
# Runtime: 230 ms, Memory: 30.4 MB
# Submission Id: 1086031583


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def LCA(node, p, q):
            if node is None or node == p or node == q:
                return node
            left = LCA(node.left, p, q)
            right = LCA(node.right, p, q)
            if left and right:
                return node
            return left or right
        
        def dfs(node, target):
            if node == target:
                return True
            if node is None:
                return False
            return dfs(node.left, target) or dfs(node.right, target)
        
        node = LCA(root, p, q)
        if node == p:
            return p if dfs(node, q) else None
        if node == q:
            return q if dfs(node, p) else None
        return node