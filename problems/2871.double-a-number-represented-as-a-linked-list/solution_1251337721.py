# 2871 - Double a Number Represented as a Linked List
# Date: 2024-05-07
# Runtime: 234 ms, Memory: 19.1 MB
# Submission Id: 1251337721


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node):
            prev, curr = None, node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev, curr = curr, tmp
            return prev

        head = reverse(head)
        prev, curr = None, head
        carry = 0
        while curr:
            carry, curr.val = divmod(carry + curr.val * 2, 10)
            prev, curr = curr, curr.next
        if carry:
            prev.next = ListNode(carry)
            prev = prev.next

        return reverse(head)