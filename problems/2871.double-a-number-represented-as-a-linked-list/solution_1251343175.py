# 2871 - Double a Number Represented as a Linked List
# Date: 2024-05-07
# Runtime: 310 ms, Memory: 19.9 MB
# Submission Id: 1251343175


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        new_tail = None
        value = 0
        while stack or value:
            if stack:
                value += stack.pop() * 2
            value, digit = divmod(value, 10)
            new_tail = ListNode(digit, new_tail)
            
        return new_tail