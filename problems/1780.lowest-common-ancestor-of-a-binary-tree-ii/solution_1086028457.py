# 1780 - Lowest Common Ancestor of a Binary Tree II
# Date: 2023-10-28
# Runtime: 205 ms, Memory: 21.1 MB
# Submission Id: 1086028457


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        if p not in parent or q not in parent:
            return None
        
        seen = set()
        while p:
            seen.add(p)
            p = parent[p]
            
        while q not in seen:
            q = parent[q]
        return q
        