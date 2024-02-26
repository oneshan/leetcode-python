# 2573 - Remove Nodes From Linked List
# Date: 2022-11-28
# Runtime: 3017 ms, Memory: 60.8 MB
# Submission Id: 850771040


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev, node = None, head
            while node:
                nxt = node.next
                node.next = prev
                prev, node = node, nxt
            return prev
        
        head = reverse(head)
        node = head
        while node.next:
            if node.val <= node.next.val:
                node = node.next
            else:
                node.next = node.next.next
                
        return reverse(head)