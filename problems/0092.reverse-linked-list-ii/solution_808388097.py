# 0092 - Reverse Linked List II
# Date: 2022-09-26
# Runtime: 53 ms, Memory: 14 MB
# Submission Id: 808388097


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        p1 = dummy
        for _ in range(left-1):
            p1 = p1.next
            
        prev, curr = None, p1.next
        for i in range(left, right+1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        p1.next.next = curr
        p1.next = prev
        return dummy.next
