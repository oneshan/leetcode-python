# 0776 - N-ary Tree Postorder Traversal
# Date: 2022-10-22
# Runtime: 127 ms, Memory: 16 MB
# Submission Id: 827941076


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children)
        return ans[::-1]