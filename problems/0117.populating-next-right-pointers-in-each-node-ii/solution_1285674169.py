# 0117 - Populating Next Right Pointers in Each Node II
# Date: 2024-06-12
# Runtime: 45 ms, Memory: 17.4 MB
# Submission Id: 1285674169


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
            return root

        queue = deque([root])
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if prev:
                    prev.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev = node

        return root