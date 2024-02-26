# 0019 - Remove Nth Node From End of List
# Date: 2023-01-02
# Runtime: 38 ms, Memory: 13.8 MB
# Submission Id: 869499221


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = p2 = dummy
        for _ in range(n+1):
            p1 = p1.next
            
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next