# 1790 - Lowest Common Ancestor of a Binary Tree III
# Date: 2023-10-28
# Runtime: 63 ms, Memory: 20.9 MB
# Submission Id: 1086039454


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        
        while q not in seen:
            q = q.parent
        
        return q