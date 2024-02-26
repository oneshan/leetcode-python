# 0528 - Swapping Nodes in a Linked List
# Date: 2023-05-15
# Runtime: 917 ms, Memory: 50.7 MB
# Submission Id: 950669995


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        p1 = p2 = head
        for _ in range(k-1):
            p2 = p2.next
        tmp = p2
        
        while p2.next:
            p1, p2 = p1.next, p2.next
        tmp.val, p1.val = p1.val, tmp.val
        return head
        