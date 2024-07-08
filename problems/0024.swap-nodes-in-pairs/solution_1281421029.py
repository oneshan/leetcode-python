# 0024 - Swap Nodes in Pairs
# Date: 2024-06-08
# Runtime: 37 ms, Memory: 16.3 MB
# Submission Id: 1281421029


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n1, n2 = head, head.next        
        n1.next = self.swapPairs(n2.next)
        n2.next = n1
        return n2