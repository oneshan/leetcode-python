# 0024 - Swap Nodes in Pairs
# Date: 2024-06-08
# Runtime: 33 ms, Memory: 16.5 MB
# Submission Id: 1281422554


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr and curr.next:
            n1, n2 = curr, curr.next

            prev.next = n2
            n1.next = n2.next
            n2.next = n1

            prev, curr = n1, n1.next

        return dummy.next