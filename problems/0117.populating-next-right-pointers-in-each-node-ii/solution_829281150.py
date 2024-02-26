# 0117 - Populating Next Right Pointers in Each Node II
# Date: 2022-10-24
# Runtime: 64 ms, Memory: 15.3 MB
# Submission Id: 829281150


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
                
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                if curr.left:
                    if not prev:
                        leftmost = curr.left
                    else:
                        prev.next = curr.left
                    prev = curr.left
                    
                if curr.right:
                    if not prev:
                        leftmost = curr.right
                    else:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next
        return root