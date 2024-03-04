# 0019 - Remove Nth Node From End of List
# Date: 2024-03-03
# Runtime: 39 ms, Memory: 16.6 MB
# Submission Id: 1192131202


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        p1 = p2 = dummy
        for _ in range(n+1):
            p1 = p1.next

        while p1:
            p1, p2 = p1.next, p2.next

        p2.next = p2.next.next
        return dummy.next