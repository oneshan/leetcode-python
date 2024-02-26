# 0328 - Odd Even Linked List
# Date: 2023-01-03
# Runtime: 68 ms, Memory: 16.7 MB
# Submission Id: 870448281


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()
        
        ptr_o, ptr_e = odd_head, even_head
        while head:
            ptr_o.next = head
            ptr_o = ptr_o.next
            head = head.next
    
            if head:
                ptr_e.next = head
                ptr_e = ptr_e.next
                head = head.next
        
        ptr_o.next = even_head.next
        ptr_e.next = None
        return odd_head.next