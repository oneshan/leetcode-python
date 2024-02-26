# 1411 - Convert Binary Number in a Linked List to Integer
# Date: 2023-09-07
# Runtime: 46 ms, Memory: 16.1 MB
# Submission Id: 1043131556


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        ans = 0
        while head:
            ans <<= 1
            ans += head.val
            head = head.next
        return ans