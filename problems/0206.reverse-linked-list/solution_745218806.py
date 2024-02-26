# 0206 - Reverse Linked List
# Date: 2022-07-12
# Runtime: 61 ms, Memory: 20.5 MB
# Submission Id: 745218806


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