# 0019 - Remove Nth Node From End of List
# Date: 2024-03-03
# Runtime: 39 ms, Memory: 16.6 MB
# Submission Id: 1192130230


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = curr = ListNode(0, head)

        size = 0
        while curr:
            curr = curr.next
            size += 1

        curr = dummy
        for _ in range(size-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next