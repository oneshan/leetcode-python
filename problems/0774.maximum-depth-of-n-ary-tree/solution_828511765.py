# 0774 - Maximum Depth of N-ary Tree
# Date: 2022-10-23
# Runtime: 108 ms, Memory: 16.1 MB
# Submission Id: 828511765


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
        stack = [(root, 1)]
        ans = 0
        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            for child in node.children:
                if child:
                    stack.append((child, depth+1))
        return ans