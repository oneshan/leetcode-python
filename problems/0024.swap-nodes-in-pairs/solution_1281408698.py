# 0024 - Swap Nodes in Pairs
# Date: 2024-06-08
# Runtime: 42 ms, Memory: 16.5 MB
# Submission Id: 1281408698


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr = head.next
        nxt = curr.next
        curr.next = head
        head.next = self.swapPairs(nxt)
        return curr