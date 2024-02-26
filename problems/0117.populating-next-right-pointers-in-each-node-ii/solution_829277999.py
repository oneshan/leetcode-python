# 0117 - Populating Next Right Pointers in Each Node II
# Date: 2022-10-24
# Runtime: 101 ms, Memory: 15.3 MB
# Submission Id: 829277999


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
            curr_level = leftmost
            leftmost = prev = None
            while curr_level:
                if curr_level.left:
                    node = curr_level.left
                    if not leftmost:
                        leftmost = node
                    if prev:
                        prev.next = node
                    prev = node  
                if curr_level.right:
                    node = curr_level.right
                    if not leftmost:
                        leftmost = node
                    if prev:
                        prev.next = node
                    prev = node
                curr_level = curr_level.next
        return root