# 0002 - Add Two Numbers
# Date: 2022-07-12
# Runtime: 111 ms, Memory: 13.9 MB
# Submission Id: 745249407


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        head = node = ListNode()
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(val, 10)
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            node.next = ListNode(carry)
        return head.next