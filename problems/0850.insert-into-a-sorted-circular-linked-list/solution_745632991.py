# 0850 - Insert into a Sorted Circular Linked List
# Date: 2022-07-13
# Runtime: 41 ms, Memory: 14.8 MB
# Submission Id: 745632991


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:  # 1 3 5
                break
            if prev.val > curr.val:
                if prev.val <= insertVal >= curr.val:  # 3 5 1
                    break
                if prev.val >= insertVal <= curr.val:  # 5 1 3
                    break
            prev, curr = curr, curr.next
            if prev == head:
                break
        
        prev.next = Node(insertVal, curr)
        return head