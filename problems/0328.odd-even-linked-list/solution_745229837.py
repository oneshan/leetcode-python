# 0328 - Odd Even Linked List
# Date: 2022-07-12
# Runtime: 74 ms, Memory: 16.5 MB
# Submission Id: 745229837


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        even_head = head.next
        
        odd, even = head, head.next
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head