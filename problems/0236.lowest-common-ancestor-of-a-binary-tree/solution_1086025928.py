# 0236 - Lowest Common Ancestor of a Binary Tree
# Date: 2023-10-28
# Runtime: 59 ms, Memory: 20.9 MB
# Submission Id: 1086025928


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        stack = [root]
        parent = {root: None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        seen = set()
        while p:
            seen.add(p)
            p = parent[p]
        
        while q:
            if q in seen:
                return q
            q = parent[q]
        return None