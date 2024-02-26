# 0528 - Swapping Nodes in a Linked List
# Date: 2023-05-15
# Runtime: 1092 ms, Memory: 51 MB
# Submission Id: 950687252


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        p1 = p2 = dummy
        for _ in range(k-1):
            p2 = p2.next
        tmp = p2
        
        while p2.next and p2.next.next:
            p1, p2 = p1.next, p2.next
            
        # swap node
        tmp.next, p1.next = p1.next, tmp.next
        tmp.next.next, p1.next.next = p1.next.next, tmp.next.next
        
        return dummy.next
        