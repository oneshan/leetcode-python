# 1790 - Lowest Common Ancestor of a Binary Tree III
# Date: 2024-07-15
# Runtime: 49 ms, Memory: 20 MB
# Submission Id: 1321356274


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
        parents = set()
        
        while p:
            parents.add(p)
            p = p.parent
        
        while q:
            if q in parents:
                return q
            q = q.parent

        return None