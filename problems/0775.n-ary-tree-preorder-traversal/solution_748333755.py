# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-07-16
# Runtime: 78 ms, Memory: 16.2 MB
# Submission Id: 748333755


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        self.recursion(root)
        return self.ans
    
    def recursion(self, node):
        if not node:
            return
        self.ans.append(node.val)
        for child in node.children:
            self.recursion(child)