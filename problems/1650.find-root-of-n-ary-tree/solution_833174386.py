# 1650 - Find Root of N-Ary Tree
# Date: 2022-10-30
# Runtime: 463 ms, Memory: 24.3 MB
# Submission Id: 833174386


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        value = 0
        for node in tree:
            value ^= node.val
            for child in node.children:
                value ^= child.val
        
        for node in tree:
            if node.val == value:
                return node