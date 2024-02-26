# 1411 - Convert Binary Number in a Linked List to Integer
# Date: 2022-11-18
# Runtime: 26 ms, Memory: 13.7 MB
# Submission Id: 845719108


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = (ans << 1) + head.val
            head = head.next
        return ans