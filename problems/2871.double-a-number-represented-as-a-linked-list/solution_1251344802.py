# 2871 - Double a Number Represented as a Linked List
# Date: 2024-05-07
# Runtime: 240 ms, Memory: 20.4 MB
# Submission Id: 1251344802


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recur(node):
            if not node:
                return 0
            value = node.val * 2 + recur(node.next)
            value, node.val = divmod(value, 10)
            return value

        carry = recur(head)
        if carry:
            head = ListNode(carry, head)
        return head