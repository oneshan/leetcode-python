# 0143 - Reorder List
# Date: 2024-03-23
# Runtime: 49 ms, Memory: 24.7 MB
# Submission Id: 1211265856


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        
        # reverse
        prev, curr = None, p2
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        # merge
        p1, p2 = head, prev
        while p2.next:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2