# 0766 - Flatten a Multilevel Doubly Linked List
# Date: 2022-07-13
# Runtime: 31 ms, Memory: 14.5 MB
# Submission Id: 745623161


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        dummy = prev = Node(0, None, head, None)
        stack = [head]
        while stack:
            node = stack.pop()
            prev.next = node
            node.prev = prev
            
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
            
            prev = node
            
        dummy.next.prev = None
        return dummy.next
            