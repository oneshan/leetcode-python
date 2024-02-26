# 0024 - Swap Nodes in Pairs
# Date: 2022-10-27
# Runtime: 58 ms, Memory: 13.7 MB
# Submission Id: 831155307


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(head.next.next)
        return head