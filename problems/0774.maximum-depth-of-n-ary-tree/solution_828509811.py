# 0774 - Maximum Depth of N-ary Tree
# Date: 2022-10-23
# Runtime: 83 ms, Memory: 16.1 MB
# Submission Id: 828509811


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.recursion(root, 0)
        
    def recursion(self, node, depth):
        if not node:
            return depth
        
        ans = 0
        for child in node.children:
            ans = max(ans, self.recursion(child, depth+1))
        return ans + 1