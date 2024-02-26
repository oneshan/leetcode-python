# 0138 - Copy List with Random Pointer
# Date: 2023-09-05
# Runtime: 56 ms, Memory: 17.2 MB
# Submission Id: 1041039049


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
        self.mapping = {old_node: new_node}
        
        while old_node:
            new_node.next = self.clone(old_node.next)
            new_node.random = self.clone(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return self.mapping[head]    
        
    def clone(self, node):
        if not node:
            return None
        if node not in self.mapping:
            self.mapping[node] = Node(node.val)
        return self.mapping[node]
