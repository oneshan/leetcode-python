# 0328 - Odd Even Linked List
# Date: 2022-07-12
# Runtime: 88 ms, Memory: 16.6 MB
# Submission Id: 745227029


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()
        
        node_o, node_e = odd_head, even_head
        while head and head.next:
            node_o.next = head
            node_e.next = head.next
            node_o = node_o.next
            node_e = node_e.next
            head = head.next.next
        if head:
            node_o.next = head
            node_o = node_o.next
        node_o.next = even_head.next
        node_e.next = None
        return odd_head.next