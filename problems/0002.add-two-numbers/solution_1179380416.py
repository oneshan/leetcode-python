# 0002 - Add Two Numbers
# Date: 2024-02-19
# Runtime: 66 ms, Memory: 16.6 MB
# Submission Id: 1179380416


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next                
            carry, num = divmod(carry, 10)
            curr.next = ListNode(num)
            curr = curr.next

        return head.next