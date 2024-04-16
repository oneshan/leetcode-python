# 0758 - Convert Binary Search Tree to Sorted Doubly Linked List
# Date: 2024-04-15
# Runtime: 35 ms, Memory: 17.2 MB
# Submission Id: 1232782418


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        head = self.prev = Node(0)

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            self.prev.right = node
            node.left = self.prev
            self.prev = node

            inorder(node.right)

        inorder(root)
        self.prev.right = head.right
        head.right.left = self.prev
        return head.right