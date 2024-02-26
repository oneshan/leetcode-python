# 1816 - Lowest Common Ancestor of a Binary Tree IV
# Date: 2023-10-28
# Runtime: 119 ms, Memory: 22 MB
# Submission Id: 1086042897


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        
        def dfs(node):
            if not node:
                return None
            if node in nodes:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right
        
        return dfs(root)