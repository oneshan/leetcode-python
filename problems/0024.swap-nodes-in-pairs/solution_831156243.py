# 0024 - Swap Nodes in Pairs
# Date: 2022-10-27
# Runtime: 42 ms, Memory: 13.9 MB
# Submission Id: 831156243


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_n, second_n = head, head.next
        
        # swap
        first_n.next = self.swapPairs(second_n.next)
        second_n.next = first_n
        
        return second_n