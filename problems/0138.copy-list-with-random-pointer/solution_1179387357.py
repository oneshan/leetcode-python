# 0138 - Copy List with Random Pointer
# Date: 2024-02-19
# Runtime: 38 ms, Memory: 17.5 MB
# Submission Id: 1179387357


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_node = head
        new_node = Node(head.val)
        mapping = {old_node: new_node}

        def clone(node):
            if not node:
                return None
            if node not in mapping:
                mapping[node] = Node(node.val)
            return mapping[node]

        while old_node:
            new_node.next = clone(old_node.next)
            new_node.random = clone(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return mapping[head]