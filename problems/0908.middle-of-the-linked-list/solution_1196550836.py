# 0908 - Middle of the Linked List
# Date: 2024-03-07
# Runtime: 39 ms, Memory: 16.5 MB
# Submission Id: 1196550836


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
        return p2