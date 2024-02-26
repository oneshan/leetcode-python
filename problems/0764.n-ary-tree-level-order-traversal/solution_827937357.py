# 0764 - N-ary Tree Level Order Traversal
# Date: 2022-10-22
# Runtime: 109 ms, Memory: 16.1 MB
# Submission Id: 827937357


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        
        def traverse(node, level):
            if len(ans) == level:
                ans.append([])
            ans[level].append(node.val)
            for child in node.children:
                traverse(child, level+1)
        
        if root:
            traverse(root, 0)
        return ans