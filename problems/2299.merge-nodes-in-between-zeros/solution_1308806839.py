# 2299 - Merge Nodes in Between Zeros
# Date: 2024-07-04
# Runtime: 955 ms, Memory: 54.8 MB
# Submission Id: 1308806839


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = temp = head.next
        while curr:

            total, temp = 0, curr
            while temp.val:
                total += temp.val
                temp = temp.next
            curr.val = total

            curr.next = temp.next
            curr = curr.next

        return head.next