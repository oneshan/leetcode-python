# 2299 - Merge Nodes in Between Zeros
# Date: 2024-07-04
# Runtime: 945 ms, Memory: 56.1 MB
# Submission Id: 1308804130


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prev, curr = dummy, dummy.next
        while head:
            curr.val += head.val
            if head.val == 0 and curr.val:
                prev, curr = curr, ListNode()
                prev.next = curr
            head = head.next
        
        if curr.val == 0:
            prev.next = None
        return dummy.next