# 0206 - Reverse Linked List
# Date: 2022-10-27
# Runtime: 43 ms, Memory: 20.4 MB
# Submission Id: 831362054


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node