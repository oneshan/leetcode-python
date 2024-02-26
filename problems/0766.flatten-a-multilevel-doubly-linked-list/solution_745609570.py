# 0766 - Flatten a Multilevel Doubly Linked List
# Date: 2022-07-13
# Runtime: 63 ms, Memory: 14.6 MB
# Submission Id: 745609570


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
        node = head
        while node:
            next = node.next
            if node.child:
                child_head, child_tail = self.search(node.child)
                child_head.prev = node
                child_tail.next = next
                node.next = child_head
                if next:
                    next.prev = child_tail
                node.child = None
            node = node.next
        return head
    
    def search(self, child):
        head = tail = child
        while head.prev:
            head = head.prev
        while tail.next:
            tail = tail.next
        return head, tail