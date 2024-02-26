# 0766 - Flatten a Multilevel Doubly Linked List
# Date: 2022-07-13
# Runtime: 79 ms, Memory: 15.3 MB
# Submission Id: 745617395


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
        dummy = Node(0, None, head, None)
        self.flatten_dfs(dummy, head)
        dummy.next.prev = None
        return head
    
    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev
        
        curr.prev = prev
        prev.next = curr
        
        next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, next)