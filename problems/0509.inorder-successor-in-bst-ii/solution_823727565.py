# 0509 - Inorder Successor in BST II
# Date: 2022-10-16
# Runtime: 184 ms, Memory: 21.5 MB
# Submission Id: 823727565


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        successor = None
        if node.right:
            curr = node.right
            while curr.left:
                curr = curr.left
            return curr
        
        parent = node.parent
        while parent:
            if parent.val > node.val:
                return parent
            parent = parent.parent
        return None