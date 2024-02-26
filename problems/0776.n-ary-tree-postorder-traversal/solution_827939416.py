# 0776 - N-ary Tree Postorder Traversal
# Date: 2022-10-22
# Runtime: 66 ms, Memory: 16.3 MB
# Submission Id: 827939416


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def recur(node):
            if not node:
                return
            for child in node.children:
                recur(child)    
            ans.append(node.val)
            
        recur(root)
        return ans