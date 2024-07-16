# 1816 - Lowest Common Ancestor of a Binary Tree IV
# Date: 2024-07-15
# Runtime: 86 ms, Memory: 21.4 MB
# Submission Id: 1321357923


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def find_lca(root):
            if not root:
                return None
            if root in nodes:
                return root
            
            left = find_lca(root.left)
            right = find_lca(root.right)
            if left and right:
                return root
            return left or right

        return find_lca(root)