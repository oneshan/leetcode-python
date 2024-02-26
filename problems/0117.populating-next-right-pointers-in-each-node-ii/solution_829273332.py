# 0117 - Populating Next Right Pointers in Each Node II
# Date: 2022-10-24
# Runtime: 61 ms, Memory: 15.4 MB
# Submission Id: 829273332


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            queue_len = len(queue)
            prev = None
            for _ in range(queue_len):
                node = queue.popleft()
                if prev: prev.next = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                prev = node
        return root