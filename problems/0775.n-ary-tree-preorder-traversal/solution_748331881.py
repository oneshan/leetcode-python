# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-07-16
# Runtime: 114 ms, Memory: 16 MB
# Submission Id: 748331881


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            for child in node.children[::-1]:
                if child:
                    stack.append(child)
            ans.append(node.val)
        return ans