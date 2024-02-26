# 0002 - Add Two Numbers
# Date: 2024-02-19
# Runtime: 53 ms, Memory: 16.7 MB
# Submission Id: 1179381921


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0
        while l1 or l2:
            carry += l1.val if l1 else 0
            carry += l2.val if l2 else 0
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return head.next