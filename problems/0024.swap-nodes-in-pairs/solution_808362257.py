# 0024 - Swap Nodes in Pairs
# Date: 2022-09-25
# Runtime: 37 ms, Memory: 13.9 MB
# Submission Id: 808362257


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p1, p2 = head, head.next
        
        p1.next = self.swapPairs(p2.next)
        p2.next = p1
        return p2
        