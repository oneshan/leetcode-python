# 0206 - Reverse Linked List
# Date: 2024-03-21
# Runtime: 39 ms, Memory: 17.7 MB
# Submission Id: 1209797565


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev