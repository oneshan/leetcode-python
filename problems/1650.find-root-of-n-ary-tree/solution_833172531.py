# 1650 - Find Root of N-Ary Tree
# Date: 2022-10-30
# Runtime: 390 ms, Memory: 25 MB
# Submission Id: 833172531


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        in_degree = set()
        for p in tree:
            for q in p.children:
                in_degree.add(q)
        
        for node in tree:
            if node not in in_degree:
                return node
        return None