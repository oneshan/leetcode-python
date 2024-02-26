# 0086 - Partition List
# Date: 2023-08-15
# Runtime: 44 ms, Memory: 16.3 MB
# Submission Id: 1021714612


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        h1 = p1 = ListNode()
        h2 = p2 = ListNode()
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = h2.next
        p2.next = None
        return h1.next