# 0766 - Flatten a Multilevel Doubly Linked List
# Date: 2022-07-13
# Runtime: 40 ms, Memory: 14.6 MB
# Submission Id: 745618286


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        while node:
            next = node.next
            if node.child:
                c_head = node.child
                c_tail = self.get_tail(node.child)
                c_head.prev = node
                c_tail.next = next
                node.next = c_head
                if next:  # corner case: node is the tail
                    next.prev = c_tail
                node.child = None
            node = node.next
        return head
    
    def get_tail(self, child):
        tail = child
        while tail.next:
            tail = tail.next
        return tail