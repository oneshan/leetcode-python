# 0206 - Reverse Linked List
# Date: 2022-07-12
# Runtime: 50 ms, Memory: 15.5 MB
# Submission Id: 745217049


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            node = curr.next
            curr.next = prev
            prev, curr = curr, node
        return prev