# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-06-07
# Runtime: 91 ms, Memory: 16.3 MB
# Submission Id: 716582075


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.traverse(root, ans)
        return ans
    
    def traverse(self, node, ans):
        if not node:
            return
        ans.append(node.val)
        for child in node.children:
            self.traverse(child, ans)
        