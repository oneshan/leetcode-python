# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-11-13
# Runtime: 51 ms, Memory: 16.3 MB
# Submission Id: 842613764


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
            return []
        
        ans = []
        
        def recur(node):
            ans.append(node.val)
            for child in node.children:
                if child:
                    recur(child)
                    
        recur(root)
        return ans