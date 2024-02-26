# 0019 - Remove Nth Node From End of List
# Date: 2022-07-12
# Runtime: 52 ms, Memory: 13.9 MB
# Submission Id: 745212686


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node = dummy
        for _ in range(n+1):
            node = node.next
        
        curr = dummy
        while node:
            node = node.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next