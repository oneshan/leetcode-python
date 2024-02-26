# 0024 - Swap Nodes in Pairs
# Date: 2022-09-25
# Runtime: 26 ms, Memory: 13.9 MB
# Submission Id: 808360112


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev, curr = dummy, head
        while curr and curr.next:
            p1, p2 = curr, curr.next
            
            # Swap: dummy -> 2 -> 1 -> 3 -> ...
            prev.next = p2
            p1.next = p2.next
            p2.next = p1
            
            prev, curr = curr, curr.next
        return dummy.next