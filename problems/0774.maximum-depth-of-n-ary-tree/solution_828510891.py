# 0774 - Maximum Depth of N-ary Tree
# Date: 2022-10-23
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 828510891


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child) for child in root.children) + 1